from backend.core import run_llm
import streamlit as st
from streamlit_chat import message
from typing import Set

# Add sidebar with user information
with st.sidebar:
    st.title("사용자 프로필")
    
    # Create input fields for user information
    user_name = st.text_input("이름", placeholder="이름을 입력하세요")
    user_email = st.text_input("이메일", placeholder="이메일을 입력하세요")
    
    if user_name or user_email:
        st.write("👤 **사용자 정보**")
        if user_name:
            st.write(f"**이름:** {user_name}")
        if user_email:
            st.write(f"**이메일:** {user_email}")
    
    # Add a divider for visual separation
    st.divider()

# Main content
st.header("LangChain 유데미 코스 문서 도우미 봇")

prompt = st.text_input("프롬프트", placeholder="여기에 프롬프트를 입력하세요...")

# Initialize session state
if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []

def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    source_list = list(source_urls)
    source_list.sort()
    source_string = "출처:\n"
    for i, source in enumerate(source_list):
        source_string += f"{i+1}. {source}\n"
    return source_string

if prompt:
    with st.spinner("생성 중..."):
        generated_response = run_llm(query=prompt, chat_history=st.session_state["chat_history"])
        sources = set([doc.metadata["source"]for doc in generated_response["source_documents"]])
        formatted_response = f"{generated_response['result']} \n\n {create_sources_string(sources)}"

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", generated_response["result"]))


if st.session_state['chat_answers_history']:
    for generated_response, user_query in zip(st.session_state["chat_answers_history"], st.session_state["user_prompt_history"]):
        message(user_query, is_user=True)
        message(generated_response)
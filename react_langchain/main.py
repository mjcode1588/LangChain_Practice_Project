from dotenv import load_dotenv
from langchain.agents import tool
from langchain.prompts.prompt import PromptTemplate
from langchain.agents.output_parsers import ReActJsonSingleInputOutputParser
from langchain.tools.render import render_text_description
from langchain_openai import ChatOpenAI
load_dotenv()


@tool
def get_text_length(text:str)->int:
    """
    텍스트의 글자 수를 반환합니다.
    """
    return len(text)

if __name__ == "__main__":
    print("Hello React LangChain!")
    tools = [get_text_length]

    template = """
    다음 질문에 최선을 다해 답변하세요. 다음 도구들을 사용할 수 있습니다:

    {tools}

    다음 형식을 사용하세요:

    Question: 답변해야 할 입력 질문
    Thought: 무엇을 해야 할지 항상 생각해야 합니다
    Action: 취할 조치, [{tool_names}] 중 하나여야 합니다
    Action Input: 조치에 대한 입력
    Observation: 조치의 결과
    ... (이 Thought/Action/Action Input/Observation 과정은 N번 반복될 수 있습니다)
    Thought: 이제 최종 답변을 알게 되었습니다
    Final Answer: 원본 입력 질문에 대한 최종 답변

    시작합니다!

    Question: {input}
    Thought:
    """

    prompt = PromptTemplate.from_template(
        template=template,).partial(tools=render_text_description(tools=tools), tools_name=", ".join([t.name for t in tools]))

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", stop=["\nObservation"])

    agent = {"input": lambda x: x["input"]} | prompt | llm | ReActJsonSingleInputOutputParser()

    res = agent.invoke({"input" : "What is the length of 'Dog' in characters?"})
    print(res)


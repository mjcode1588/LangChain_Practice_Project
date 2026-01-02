import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup(name:str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini"
    )
    # llm = OllamaLLM(
    #     temperature=0,
    #     model="llama3.2:1b"
    # )
    template = """주어진 전체 이름 {name_of_person}에 대해서, 그들의 LinkedIn 프로필 페이지 링크를 찾아주세요.
                    당신의 답변은 오직 URL만 포함해야 합니다."""
    
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crwal Google 4 linkedin profile page", ## Tool 지칭 할때 사용할 이름, 추론엔진에 제공 및 로그에 표시
            func=get_profile_url_tavily, ## 실행될 함수 
            description="LinkedIn 페이지 URL을 가져와야 할 때 유용합니다." ## LLM이 이 도구를 사용할지 말지 결정하는 기준이됨
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    ## Ract 에이전트를 만들고 agent_excutor를 만드는 이유는
    ## create_react_agent 레시피고
    ## AgentExecutor는 모든 걸 조율하고 python을 호출
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True,handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={"input" : prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url= result["output"]
    return linked_profile_url

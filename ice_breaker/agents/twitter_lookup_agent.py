from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup(name:str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini",
    )
    template = """
        주어진 이름 {name_of_person}에 대해 사용자의 소셜 미디어 링크를 찾아주세요.
        최종 답변에는 해당 인물의 사용자 이름(username)만 포함되어야 합니다.
    """
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tool_for_agent = [
        Tool(
            name="Crawl Google 4 Twitter profile page",
            func=get_profile_url_tavily,
            description="Twitter 페이지 URL을 가져와야 할 때 유용합니다."
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tool_for_agent,prompt=react_prompt)
    agent_excutor = AgentExecutor(agent=agent, tools=tool_for_agent,verbose=True)

    result = agent_excutor.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )
    twitter_username = result["output"]
    return twitter_username
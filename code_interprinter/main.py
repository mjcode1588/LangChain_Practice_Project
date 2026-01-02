from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.agents.agent_toolkits import create_csv_agent
import os
from typing import Any
load_dotenv()

base_prompt = hub.pull("langchain-ai/react-agent-template")

def py_agent_main(original_prompt):
    print("Start...")
    instructions = """당신은 질문에 답하기 위해 Python 코드를 작성하고 실행하는 에이전트입니다.
    Python REPL에 접근하여 Python 코드를 실행할 수 있습니다.
    오류가 발생하면 코드를 디버깅하고 다시 시도하세요.
    질문에 대한 답변으로 코드의 출력값만 사용하세요.
    코드를 실행하지 않고도 답을 알 수 있더라도, 반드시 코드를 실행하여 답을 얻어야 합니다.
    코드를 작성하여 질문에 답할 수 없을 것 같다면, 그냥 "모르겠습니다"라고 답변하세요.
    """


    prompt = base_prompt.partial(instructions=instructions)

    tools = [PythonREPLTool()]
    agent = create_react_agent(
        prompt=prompt,
        llm=ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),
        tools=tools
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor.invoke({"input": original_prompt})
# def python_agent_executor_wrapper(original_prompt: str) -> dict[str, Any]:
#     return python_agent_executor.invoke({"input": original_prompt})

def csv_agent_executror_wrapper(original_prompt:str) -> dict[str, Any]:
    csv_agent = create_csv_agent(
        llm=ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),
        path="episode_info.csv",
        verbose=True,
        allow_dangerous_code=True
    )
    return csv_agent.invoke(input={
        "input": original_prompt
    })

def route_agent_main():
    tools =[
        Tool(
            name="Python Agent",
            func=py_agent_main,
            description="""자연어를 Python으로 변환하고 Python 코드를 실행하여,
                          코드 실행 결과를 반환해야 할 때 유용합니다.
                          입력으로 코드를 받지 않습니다."""
        ),
        Tool(
            name="CSV Agent",
            func=csv_agent_executror_wrapper,
            description="""episode_info.csv 파일에 대한 질문에 답해야 할 때 유용합니다.
                         질문 전체를 입력으로 받아 pandas 계산을 수행한 후 답을 반환합니다.""",
        )
    ]
    prompt = base_prompt.partial(instructions="")
    grand_agent = create_react_agent(
        prompt=prompt,
        llm=ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),
        tools=tools,
    )
    grand_agent_executor = AgentExecutor(agent=grand_agent, tools=tools, verbose=True)

    print(
        grand_agent_executor.invoke(
            {
                "input": "which season has the most episodes?"
            }
        )
    )
    print(
        grand_agent_executor.invoke(
            {
                "input": "Generate and save in current working directory 15 qrcodes that point to `www.udemy.com/course/langchain`",
            }
        )
    )

if __name__ == "__main__":
    route_agent_main()

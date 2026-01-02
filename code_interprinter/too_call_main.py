from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

## langchain의 Tool를 사용해서 제어하려면,
## OPENAI에 기본적으로 종속되어 사용되어왔지만,
## create_tool_calling_agent를 사용하면 쉽게 사용이 가능함

load_dotenv()

@tool
def multiply(x: float, y: float) -> float:
    """Multiply 'x' times 'y'."""
    return x * y


if __name__ == "__main__":
    print("Hello Tool Calling")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "you're a helpful assistant"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    tools = [TavilySearchResults(), multiply]
    # llm = ChatOpenAI(model="gpt-4-turbo")
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)

    res = agent_executor.invoke(
        {
            "input": "what is the weather in dubai right now? compare it with San Fransisco, output should in in celsious",
        }
    )

    print(res)

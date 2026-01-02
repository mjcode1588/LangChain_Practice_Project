from typing import Tuple
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from output_parsers import summary_parser, Summary
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter import scrape_user_tweets


def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_username, mock=True
    )

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username, mock=True)

    summary_template = """
    LinkedIn의 정보 {information}와 최신 Twitter 게시물 {twitter_posts}를 바탕으로 다음을 작성해 주세요:
    1. 짧은 요약
    2. 그들에 대한 흥미로운 사실 두 가지

    Twitter와 LinkedIn의 정보를 모두 사용하세요.
    \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    # llm = OllamaLLM(temperature=0, model="llama3.2:1b")

    chain = summary_prompt_template | llm | summary_parser

    res:Summary = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})

    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_break_with(name="Harrison Chase")
from autogen_agentchat.agents import AssistantAgent
from config.llm_config import llm_config

def create_isolater():
    return AssistantAgent(
        name="IsolaterAgent",
        system_message="""
        You generate the final precise answer.

        Use ONLY the provided context.
        Do not hallucinate.
        """,
        llm_config=llm_config
    )
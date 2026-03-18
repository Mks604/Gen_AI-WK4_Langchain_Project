from autogen_agentchat.agents import AssistantAgent
from config.llm_config import llm_config

def create_select_context():
    return AssistantAgent(
        name="SelectContextAgent",
        system_message="""
        You select ONLY relevant information from context.

        Remove noise and keep important points only.
        """,
        llm_config=llm_config
    )
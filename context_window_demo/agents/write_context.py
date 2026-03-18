from autogen_agentchat.agents import AssistantAgent
from config.llm_config import llm_config

def create_write_context():
    return AssistantAgent(
        name="WriteContextAgent",
        system_message="""
        You generate detailed context.

        Include:
        - Background
        - Key facts
        - Examples
        """,
        llm_config=llm_config
    )
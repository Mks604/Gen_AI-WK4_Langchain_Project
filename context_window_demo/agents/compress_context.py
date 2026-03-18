from autogen_agentchat.agents import AssistantAgent
from config.llm_config import llm_config

def create_compress_context():
    return AssistantAgent(
        name="CompressContextAgent",
        system_message="""
        You compress context into a short, meaningful summary.
        Keep it concise and informative.
        """,
        llm_config=llm_config
    )
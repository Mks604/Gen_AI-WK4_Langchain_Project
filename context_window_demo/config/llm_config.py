import os
from dotenv import load_dotenv

load_dotenv()

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "temperature": 0.7
}
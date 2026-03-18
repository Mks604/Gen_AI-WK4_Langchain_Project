from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_code(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content


def explain_code(code):
    prompt = f"Explain the following code in simple terms:\n{code}"
    return generate_code(prompt)


def fix_code(code):
    prompt = f"Fix bugs in the following code:\n{code}"
    return generate_code(prompt)
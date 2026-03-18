import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email(prompt, tone):
    full_prompt = f"""
    Write a professional email based on:
    Topic: {prompt}
    Tone: {tone}

    Include:
    - Subject line
    - Email body
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
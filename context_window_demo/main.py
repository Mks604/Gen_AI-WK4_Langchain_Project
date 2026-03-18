import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------------------
# SIMPLE AGENT FUNCTION
# ---------------------------
def run_agent(system_prompt, user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content


# ---------------------------
# PIPELINE
# ---------------------------
def run_pipeline(query):
    
    print("\n🧠 STEP 1: WRITE CONTEXT")
    context = run_agent(
        "Generate detailed context with background, key facts, examples.",
        query
    )
    print(context)

    print("\n🎯 STEP 2: SELECT CONTEXT")
    selected = run_agent(
        "Select only relevant information from the context.",
        f"{query}\n\n{context}"
    )
    print(selected)

    print("\n📦 STEP 3: COMPRESS CONTEXT")
    compressed = run_agent(
        "Summarize the content into a short version.",
        selected
    )
    print(compressed)

    print("\n✅ STEP 4: FINAL ANSWER")
    final = run_agent(
        "Answer using only the given context.",
        f"{query}\n\n{compressed}"
    )
    print(final)


if __name__ == "__main__":
    query = input("Enter your query: ")
    run_pipeline(query)
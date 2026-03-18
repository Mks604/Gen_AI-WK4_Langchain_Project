import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Page config
st.set_page_config(page_title="Mock Interview AI", layout="wide")

# ✅ FIXED DARK THEME (TEXT ALWAYS WHITE)
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

/* Input box */
.stTextInput > div > div > input {
    background-color: #1e1e1e;
    color: white;
}

/* AI message (Question) */
.question-box {
    background-color: #111;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: white !important;
    font-size: 16px;
}

/* User message */
.response-box {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: white !important;
    font-size: 16px;
}

/* Fix markdown text color */
div[data-testid="stMarkdownContainer"] {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 Mock Interview AI")
st.write("Practice interviews powered by AI")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "role" not in st.session_state:
    st.session_state.role = None

# Role selection
role = st.selectbox(
    "Select Job Role",
    [
        "Frontend Developer",
        "Backend Developer",
        "Data Scientist",
        "Python Developer",
        "Hardware Engineer"
    ]
)

# Start Interview
if st.button("Start Interview"):
    st.session_state.role = role
    st.session_state.messages = []

    prompt = f"""
    You are a professional interviewer for a {role} role.
    Ask one question at a time.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    first_question = response.choices[0].message.content
    st.session_state.messages.append(("AI", first_question))

# Display chat
for sender, msg in st.session_state.messages:
    if sender == "AI":
        st.markdown(
            f"<div class='question-box'>🤖 {msg}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='response-box'>🧑 {msg}</div>",
            unsafe_allow_html=True
        )

# User input
user_input = st.text_input("Your Answer")

# Submit Answer
if st.button("Submit Answer"):
    if user_input.strip() != "":
        st.session_state.messages.append(("User", user_input))

        # Build conversation
        conversation = [
            {"role": "system", "content": f"You are interviewing for {st.session_state.role}"}
        ]

        for sender, msg in st.session_state.messages:
            role_type = "assistant" if sender == "AI" else "user"
            conversation.append({"role": role_type, "content": msg})

        # AI response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation + [{
                "role": "system",
                "content": """
                Evaluate the answer.
                Give feedback and score.
                Then ask next question.

                Format:
                Feedback:
                Score: X/10
                Next Question:
                """
            }]
        )

        ai_reply = response.choices[0].message.content
        st.session_state.messages.append(("AI", ai_reply))

        st.rerun()
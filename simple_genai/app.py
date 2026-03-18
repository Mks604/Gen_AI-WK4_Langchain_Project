import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import uuid

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ Please set OPENAI_API_KEY in .env file")
    st.stop()

client = OpenAI(api_key=api_key)

# Page config
st.set_page_config(page_title="AI Chat Pro", page_icon="💬", layout="wide")

# 🧠 Session state
if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat" not in st.session_state:
    chat_id = str(uuid.uuid4())
    st.session_state.current_chat = chat_id
    st.session_state.chats[chat_id] = []

# 👉 Track highlight state
if "highlight" not in st.session_state:
    st.session_state.highlight = False

# 🎨 Dynamic text color
text_color = "#6b7280" if not st.session_state.highlight else "#ffffff"

st.markdown(f"""
<style>

/* Background */
.stApp {{
    background: linear-gradient(135deg, #0f172a, #020617);
}}

/* Chat bubble */
.stChatMessage {{
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 10px;
}}

/* 🔥 Dynamic TEXT COLOR CHANGE */
.stChatMessage p {{
    color: {text_color} !important;
    transition: color 0.5s ease;
}}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background: #020617;
}}

/* Input box */
.stChatInputContainer textarea {{
    background: #020617;
    color: white;
}}

/* Title */
h1 {{
    color: white;
}}

</style>
""", unsafe_allow_html=True)

st.title("💬 AI Chat (Highlight UI)")

# 📂 Sidebar
with st.sidebar:
    st.header("💬 Chats")

    if st.button("➕ New Chat"):
        new_chat_id = str(uuid.uuid4())
        st.session_state.current_chat = new_chat_id
        st.session_state.chats[new_chat_id] = []
        st.session_state.highlight = False
        st.rerun()

    for i, chat_id in enumerate(st.session_state.chats.keys()):
        if st.button(f"Chat {i+1}"):
            st.session_state.current_chat = chat_id
            st.rerun()

    st.divider()
    mode = st.selectbox("Mode", ["Summarizer", "Q&A"])
    max_tokens = st.slider("Response Length", 50, 300, 150)

# System prompt
system_prompt = (
    "Summarize clearly and concisely."
    if mode == "Summarizer"
    else "Answer clearly and helpfully."
)

messages = st.session_state.chats[st.session_state.current_chat]

# Display messages
for msg in messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Type your message...")

if user_input:
    # Reset highlight before response
    st.session_state.highlight = False

    messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    *messages
                ],
                max_tokens=max_tokens
            )

            reply = response.choices[0].message.content
            st.markdown(reply)

    messages.append({"role": "assistant", "content": reply})

    # ✅ After response → highlight text (white)
    st.session_state.highlight = True
    st.rerun()
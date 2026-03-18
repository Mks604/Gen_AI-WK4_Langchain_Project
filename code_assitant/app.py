import streamlit as st
from utils import generate_code, explain_code, fix_code

st.set_page_config(page_title="AI Code Assistant", layout="wide")

st.title("🤖 AI Code Assistant")

option = st.selectbox(
    "Choose Task",
    ["Generate Code", "Explain Code", "Fix Code"]
)

user_input = st.text_area("Enter your prompt or code here:", height=200)

if st.button("Run"):
    if user_input.strip() == "":
        st.warning("Please enter input!")
    else:
        with st.spinner("Processing..."):
            if option == "Generate Code":
                output = generate_code(user_input)
            elif option == "Explain Code":
                output = explain_code(user_input)
            else:
                output = fix_code(user_input)

        st.subheader("Output")
        st.code(output, language="python")
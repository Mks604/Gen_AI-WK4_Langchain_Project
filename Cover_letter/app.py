import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# ==============================
# OPENAI SETUP
# ==============================
# Make sure you set your API key in environment variables
# Example (Windows): setx OPENAI_API_KEY "your_api_key_here"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ==============================
# FUNCTION
# ==============================
def generate_cover_letter(name, role, company, skills, experience):
    prompt = f"""
    Write a professional, ATS-friendly cover letter.

    Candidate Name: {name}
    Job Role: {role}
    Company: {company}
    Skills: {skills}
    Experience: {experience}

    Structure:
    - Strong opening
    - Skills alignment with role
    - Experience highlights
    - Confident closing

    Keep it concise and impactful.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # ✅ FIXED MODEL
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content


# ==============================
# STREAMLIT UI
# ==============================
st.set_page_config(
    page_title="AI Cover Letter Generator",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Cover Letter Generator")
st.markdown("Generate professional cover letters instantly 🚀")

# Input fields
name = st.text_input("👤 Your Name")
role = st.text_input("💼 Job Role")
company = st.text_input("🏢 Company Name")
skills = st.text_area("🛠 Skills (comma separated)")
experience = st.text_area("📄 Experience Summary")

# Generate button
if st.button("✨ Generate Cover Letter"):
    if not all([name, role, company, skills, experience]):
        st.warning("⚠️ Please fill all fields")
    else:
        with st.spinner("Generating your cover letter..."):
            try:
                letter = generate_cover_letter(
                    name, role, company, skills, experience
                )

                st.success("✅ Cover Letter Generated!")

                # Output box
                st.text_area("📄 Your Cover Letter", letter, height=350)

                # Download button
                st.download_button(
                    label="📥 Download as TXT",
                    data=letter,
                    file_name="cover_letter.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
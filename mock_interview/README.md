# 🤖 Mock Interview AI

An AI-powered mock interview application built using **OpenAI LLM**, **Streamlit**, and **Prompt Engineering**.
This tool helps users practice job interviews with real-time feedback, scoring, and dynamic questioning.

---

## 🚀 Features

* 🎯 Role-based mock interviews (Frontend, Backend, Data Science, Hardware, etc.)
* 🤖 AI-generated interview questions
* 🧠 Smart answer evaluation using LLM
* 📊 Instant feedback with score (out of 10)
* 🔄 Continuous interview flow (question → answer → feedback → next question)
* 🎨 Clean dark UI (ChatGPT-style)

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – UI Framework
* **OpenAI API** – LLM for interview & evaluation
* **Prompt Engineering** – Structured responses

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mock-interview-ai.git
cd mock-interview-ai
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install streamlit openai
```

---

## 🔑 Set OpenAI API Key

### Windows (PowerShell)

```bash
set OPENAI_API_KEY=your_api_key_here
```

### Mac/Linux

```bash
export OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Select a job role
2. Click **Start Interview**
3. AI asks a question
4. You submit your answer
5. AI:

   * Evaluates your response
   * Gives feedback
   * Assigns a score
   * Asks the next question

---

## 🧠 Prompt Design

The system uses structured prompts like:

```
Evaluate the answer.
Give feedback and score.

Format:
Feedback:
Score: X/10
Next Question:
```

---

## 📊 Example Output

```
🤖 What is REST API?

🧑 It is a communication method between client and server...

🤖 Feedback: Good explanation but missing HTTP methods.
Score: 7/10
Next Question: What is JWT?
```

---

## 🔥 Future Enhancements

* 🎤 Voice-based interview (Speech-to-Text)
* 📄 Resume-based interview (RAG)
* 📊 Final performance dashboard
* 🧠 Difficulty levels (Beginner → Advanced)
* 💾 Save interview history
* 🌐 Deploy on cloud (Streamlit Cloud / AWS)

---

## ⚠️ Common Issues

### ❌ API Key Error

```
openai.AuthenticationError
```

✅ Fix:
Make sure your API key is set correctly in environment variables.

---

### ❌ Model Not Found Error

```
model_not_found
```

✅ Fix:
Use:

```
model="gpt-4o-mini"
```

---

## 📁 Project Structure

```
mock-interview-ai/
│── app.py        # Main Streamlit app
│── README.md     # Documentation
```

---


---

## 📜 License

This project is open-source and available under the MIT License.

---


## 👨‍💻 Author

Developed by **Kumar K** 🚀

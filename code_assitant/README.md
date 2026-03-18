# 🤖 AI Code Assistant

A modern AI-powered coding assistant that helps developers **generate code, fix bugs, and understand logic** using natural language.

Built with **Python, Streamlit, and OpenAI**, this project provides a simple ChatGPT-like interface for developers to boost productivity.

---

## 🚀 Features

✨ **Code Generation**
Generate complete code snippets from simple prompts

🛠 **Bug Fixing**
Automatically detect and fix errors in your code

📖 **Code Explanation**
Understand complex code with clear explanations

⚡ **Fast & Lightweight UI**
Minimal and responsive interface using Streamlit

🧠 **AI-Powered**
Uses OpenAI GPT models for intelligent responses

---

## 🖥️ Demo Preview

A clean interface where users can:

* Select task (Generate / Fix / Explain)
* Enter prompt or code
* Get instant AI-generated output

---

## 📁 Project Structure

```
code-assistant/
│── app.py              # Streamlit UI
│── utils.py            # Core AI logic
│── requirements.txt    # Dependencies
│── .env                # API key (not pushed to GitHub)
│── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/code-assistant.git
cd code-assistant
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add OpenAI API Key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ **Important:** Never share your API key publicly.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

After running, open your browser at:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User selects a task:

   * Generate Code
   * Explain Code
   * Fix Code

2. Input is sent to OpenAI API

3. Model processes the request using prompt engineering

4. Output is displayed in a formatted code block

---

## 📌 Example Use Cases

✔ Generate Python scripts
✔ Debug errors quickly
✔ Learn new programming concepts
✔ Convert logic into working code
✔ Improve productivity for developers

---

## 🔐 Environment Variables

| Variable       | Description         |
| -------------- | ------------------- |
| OPENAI_API_KEY | Your OpenAI API Key |

---

## 📦 Requirements

* Python 3.8+
* Streamlit
* OpenAI Python SDK

Install all with:

```bash
pip install -r requirements.txt
```

---

## 🌟 Future Enhancements

🚀 Chat history memory
📂 Upload and analyze code files
🌐 Multi-language support
🔍 RAG-based code search
🎨 Advanced UI (dark mode like ChatGPT)
🧪 Unit testing support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 🐛 Issues

If you find any bugs or issues, feel free to open an issue in the repository.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* OpenAI for providing powerful AI models
* Streamlit for rapid UI development

---

## 💡 Author

**Your Name**
Muthukumar K



---

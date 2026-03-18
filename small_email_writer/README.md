# ✉️ Smart Email Writer AI

An AI-powered web application that generates professional emails instantly using customizable templates like **HR, Sales, Support, and General**.

---

## 🚀 Features

* ✍️ Generate emails from simple prompts
* 🎯 Tone selection (Formal, Casual, Friendly, Apology, Request)
* 📂 Pre-built templates:

  * HR Emails
  * Sales Emails
  * Support Emails
  * General Emails
* 📩 Auto subject line generation
* ⚡ Fast AI-powered responses
* 🎨 Clean and modern UI (Dark theme)

---

## 🧠 Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **AI:** OpenAI API
* **Environment Management:** python-dotenv

---

## 📁 Project Structure

```
smart-email-writer/
│── app.py
│── utils.py
│── requirements.txt
│── .env
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/smart-email-writer.git
cd smart-email-writer
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the Application

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧩 How It Works

1. User enters email topic, tone, and template
2. Frontend sends request to Flask backend
3. Backend selects appropriate template (HR / Sales / Support)
4. Prompt is sent to OpenAI API
5. AI generates email content
6. Response is displayed in UI

---

## 📌 Example Use Cases

### 🧑‍💼 HR Email

* Leave approval
* Policy updates
* Interview scheduling

### 💰 Sales Email

* Product promotion
* Lead conversion
* Follow-ups

### 🛠️ Support Email

* Customer issue resolution
* Apology emails
* Technical support replies

---

## 💡 Future Enhancements

* 🧠 Auto template detection using AI
* 📊 Email quality scoring
* 🧾 Save email history (Database)
* 🌐 Multi-language support
* 🔊 Voice-to-email input
* 📱 Convert to mobile-friendly UI

---

## 🛑 Common Issues & Fixes

### ❌ requirements.txt not found

Create the file manually:

```
flask
openai
python-dotenv
```

---

### ❌ API Key Error

Make sure `.env` file contains:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 📄 License

This project is licensed under the MIT License.

---


---

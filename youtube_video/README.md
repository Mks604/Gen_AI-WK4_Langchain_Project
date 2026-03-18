# 🎥 YouTube Transcript Summarizer

An AI-powered web app that extracts transcripts from YouTube videos and generates concise summaries using OpenAI.

---

## 🚀 Features

* 🎥 Extract transcript from YouTube videos
* 🧠 Generate AI-based summaries
* ⚡ Fast and simple Streamlit UI
* 🌍 Supports English transcripts
* 🔁 Fallback handling for transcript errors
* 📜 Preview transcript before summarizing

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenAI API
* youtube-transcript-api

---

## 📂 Project Structure

```
youtube_summarizer/
│── app.py              # Main Streamlit application
│── README.md           # Project documentation
│── requirements.txt    # Dependencies
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
```

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Set your OpenAI API key as an environment variable:

### Windows (PowerShell)

```
setx OPENAI_API_KEY "your_api_key_here"
```

Restart your terminal after setting the key.

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## 🎥 Example Working Video

Use this test video (transcript enabled):

👉 https://www.youtube.com/watch?v=_uQrJ0TkZlc

---

## ⚠️ Common Issues & Fixes

### ❌ Transcript Error: `no element found`

* Cause: Network restriction or YouTube blocking requests
* Fix:

  * Use VPN or different network
  * Ensure video has captions enabled
  * Use fallback transcript or Whisper

---

### ❌ ModuleNotFoundError

```
pip install youtube-transcript-api
```

---

### ❌ OpenAI API Error

* Check API key is set correctly
* Restart terminal

---



## 📜 License

This project is open-source and available under the MIT License.

---


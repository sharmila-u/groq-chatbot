# Dronacharya — AI CLI Chatbot (Powered by Groq + Llama)

Dronacharya is a terminal-based AI chatbot built with Python and the Groq API. It supports real-time streaming responses, conversation memory, persistent chat history, and a customizable AI mentor persona.

This project is part of my AI Engineering learning journey, where I am building AI applications from scratch while learning core concepts such as APIs, prompt engineering, memory management, and LLM-based applications.

---

## ✨ Features

* **Streaming Responses** — AI replies appear in real time, token by token
* **Conversation Memory** — remembers previous messages during a session
* **Persistent Chat History** — conversations are saved and restored automatically
* **Custom AI Persona** — configurable through a system prompt
* **Rich Terminal UI** — colorful interface powered by Rich
* **Slash Commands** — `/help`, `/clear`, `/history`, `/model`
* **Environment Configuration** — secure API key management with `.env`
* **Free to Use** — powered by Groq's free API tier

---

## 🛠 Tech Stack

* Python 3.11
* Groq API
* Llama 3.3 70B Versatile
* Rich
* python-dotenv
* JSON Persistence
* Git & GitHub

---

## 🚀 Quick Start

```bash
git clone https://github.com/sharmila-u/groq-chatbot.git
cd groq-chatbot

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
MAX_HISTORY=20
```

Run the chatbot:

```bash
python chatbot.py
```

---

## 🏗 Architecture

```text
User (Terminal)
        │
        ▼
Dronacharya CLI
        │
        ▼
Conversation Memory
        │
        ▼
Groq API
        │
        ▼
Llama Model
        │
        ▼
Streaming Response
        │
        ▼
JSON Chat History
```

---

## 📚 What I Learned

* How AI APIs work
* Prompt engineering with system prompts
* Conversation memory and state management
* Streaming AI responses
* JSON serialization and persistence
* Environment variable management
* Error handling in Python
* Building real-world CLI applications
* Git and GitHub workflow

---

## 🎯 Future Improvements

* Multi-model support
* PDF chat and document Q&A
* Retrieval-Augmented Generation (RAG)
* Web UI using FastAPI and React
* Voice input and output
* Docker deployment
* Cloud hosting

---

## 👩‍💻 Author

Sharmila

Learning AI Engineering through hands-on projects and public building.

# CrewAI Local Automation App

A local automation project using **CrewAI**, **OpenAI API**, and **Gmail API** to process emails, summarize key insights, generate reports, and send alerts for urgent issues. Built with **FastAPI** for potential web integration.

---

## 🚀 Features

- ✅ Fetch and process emails from Gmail (supports filtering by date)
- ✅ Summarize emails and extract actionable insights
- ✅ Generate daily reports automatically
- ✅ Detect urgent issues and generate alert messages
- ✅ Designed with specialized AI agents using **CrewAI**
- ✅ Extensible for additional business workflows

---

## 🛠 Tech Stack

- **Python 3.10+**
- **CrewAI** – AI agent orchestration
- **OpenAI API** – NLP and text summarization
- **Google Gmail API** – Read emails securely
- **FastAPI** – Optional web interface
- **Python-dotenv** – Environment configuration
- **Uvicorn** – ASGI server for FastAPI

---

## ⚡ Installation

python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows


## Install dependencies
pip install -e .[dev]

## Create a .env file int the root folder
OPENAI_API_KEY=sk-your-openai-api-key
GMAIL_CREDENTIALS_PATH=credentials.json
MANAGER_EMAIL=manager@example.com


## Run The CrewAI workflow locally
python main.py

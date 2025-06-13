# 😎 ChaiDocs Web Query Assistant 

An AI-powered browser extension that allows users to query the ChaiDocs website contextually. It integrates a FastAPI backend, Google embeddings, OpenAI ChatBot and Qdrant vector database to return section-wise answers from documentation. Designed for developers, learners, and contributors to quickly fetch relevant content from ChaiDocs without leaving the webpage.

---

## 🚀 Features

* 🔍 Ask natural language questions about ChaiDocs
* 🔗 Get contextual answers with section/subsection and documentation links
* 🤖 Animated bot experience with interactive UI
* 🌈 Responsive design with Bootstrap
* 💬 Retains chat history within session
* 🎯 Loads only on relevant ChaiDocs domain pages

---

## 🧱 Tech Stack

### Frontend (Browser Extension)

* Manifest v3 Chrome/Edge Extension
* HTML, CSS (Bootstrap 5)
* JavaScript

### Backend

* Python 3
* FastAPI
* BeautifulSoup (For Web scrapping doc links)
* Qdrant (Docker for locally running)
* GoogleGenAI Embeddings
* OpenAI SDK via Gemini-Flash (For resolving query)
* Langchain for parsing and chunking

---

## 📦 Project Structure

```
WebQuery_RAG/
├── backend/                  # FastAPI backend
│   ├── chat.py               # Core API logic and Query Processing
|   ├── docker-compose.yml    # For locally running QdrantDB       
│   ├── indexing.py           # Query processor (embedding + Qdrant)
|   ├── list_urls.py          # Fetching all urls from chaidocs
│   ├── .env                  # Environment variables
│   └── requirements.txt
├── extension/                # Chrome Extension
│   ├── popup.html
│   ├── popup.js
│   ├── styles.css
│   ├── content.js
│   ├── injectIcon.js
│   ├── injectIcon.css
│   ├── assets/               # Bot icons and images
│   └── manifest.json
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions (Local Setup)
Follow these steps to set up and run the WebQuery project locally:

📁 1. Clone the Repository
```bash

git clone https://github.com/sbndAbhijeet/WebQuery_RAG.git
cd WebQuery_RAG
```
### ⚙️ 2. Start the FastAPI Backend

Navigate to the backend folder:

```bash

cd backend
```
Run the FastAPI server:
```bash
python chat.py
Make sure your Python environment is activated and required packages are installed (pip install -r requirements.txt).
```
### 🐳 3. Start Qdrant with Docker
In a new terminal window (while backend is still running):

```bash

docker compose up
✅ Ensure Docker Desktop is installed and running before this step.
```
### 🌐 4. View the Full HTML Demo

If you're testing the UI separately (outside the extension), right-click the index.html file and choose:

- "Open with Live Server" (VS Code extension recommended)


### 🧩 5. Load the Chrome Extension
Go to chrome://extensions

- Enable Developer Mode (top right)

- Click "Load Unpacked"

- Select the extension/ folder inside your project

The ChaiDocs Assistant icon will now appear in your toolbar

### 🚀 6. Use the Extension on ChaiDocs
Now, navigate to:
👉 https://docs.chaicode.com

You’ll see the assistant icon appear. Click it and start asking your queries directly on the docs page!


## ✨ Example Query Flow

1. Navigate to `https://docs.chaicode.com`
2. Click on the extension icon (bottom corner or popup)
3. Ask a question like:

   > "How do I use Tailwind CSS in Django?"

   > " How create a express app?"
4. You'll receive a detailed answer, code snippet (if any), and a link to the section.

---

## 🧠 Behind the Scenes

* **Langchain** handles document parsing & chunking
* **GoogleGenAI Embeddings** generate vector representation
* **Qdrant** indexes and searches relevant chunks
* **FastAPI** handles user queries and returns structured JSON
* **Chrome Extension** renders the response with UI animations

---

## 📎 License

MIT License @ Abhijeet

---

# Project 2: Website Documentation Bot (RAG on Docs)
Goal:
Build a chatbot that:

Ingests documentation from an existing site (e.g., ReactJS docs, internal cohort site).

Answers questions like "How to use useState?" or "Where is routing discussed?".

Optionally provides a navigation link to the correct doc page.

🧠 Flow Overview:
Scrape/Parse Docs Website:

Use tools like BeautifulSoup or Selenium (for dynamic content).

Store content per section/page.

Chunk + Embed Page Content

One vector per section or paragraph.

Store in Qdrant (or any Vector DB)

User Query Input → Embed → Vector Search

Search Results

Get top K relevant chunks.

Use the link (scraped) + content to:

Answer the question.

Provide URL to relevant section/page.

Send to OpenAI GPT for final answer.

🔧 Tech Stack
Web Scraping: requests, BeautifulSoup4, Selenium

Chunking & Embedding: langchain, openai

Vector DB: Qdrant

Frontend: Streamlit or simple chatbot UI

LLM: OpenAI

🔥 Additional Features You Can Add:
Citation links in the response (like "Answer sourced from useState docs")

Highlighting matched chunks

Toggle: "Show source chunks"

🧪 Suggested Demo Structure:
📂 PDF QA Demo
Upload PDF

Ask: "What are the main points from Chapter 2?"

Result: Summary/Answer from PDF

🌐 Docs Chatbot Demo
Ask: "How to use useState in React?"

Output: Explanation + Link to doc section


# 🧠 PDF RAG Chatbot with Persistent Memory

> Chat with your PDFs using a local LLM, vector search, and SQLite-powered memory.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange)
![Ollama](https://img.shields.io/badge/LLM-Ollama-purple)
![SQLite](https://img.shields.io/badge/Memory-SQLite-red)

---

## 🚀 Overview

This project is an end-to-end Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDFs and ask natural language questions about their content.

Unlike basic RAG implementations, this chatbot includes:

✅ Local LLM Inference using Ollama

✅ Semantic Search using ChromaDB

✅ Embedding Generation with Nomic Embed

✅ Persistent Conversation Memory using SQLite

✅ Multi-turn Question Answering

✅ Fully Offline Execution

The system combines document retrieval with conversational memory to provide context-aware answers.

---

## 🎯 Features

### 📄 PDF Understanding

Upload any PDF and instantly make it searchable.

- Academic Papers
- Research Documents
- Technical Documentation
- Notes
- Books

---

### 🔍 Semantic Search

Instead of keyword matching, the chatbot understands meaning using embeddings.

Example:

Question:

```text
How do I reverse a list?
```

Retrieved Context:

```python
arr[::-1]
```

Even if the exact wording differs.

---

### 🧠 Persistent Memory

The chatbot remembers previous conversations.

Example:

```text
You: My name is Pruthvik

Bot: Nice to meet you Pruthvik.
```

Later:

```text
You: What is my name?

Bot: Your name is Pruthvik.
```

Memory is stored inside:

```text
memory.db
```

using SQLite.

---

### 💻 Fully Local AI

No OpenAI API.

No Gemini API.

No Claude API.

Everything runs locally using Ollama.

---

## 🏗️ System Architecture

```

PDF
│
▼
PyPDFLoader
│
▼
Text Chunking
│
▼
Embeddings
(Nomic Embed)
│
▼
ChromaDB
(Vector Database)
│
▼
Retriever
│
▼
Relevant Context
│
▼
LLM (Phi/Mistral)
│
▼
Response
│
▼
SQLite Memory

```

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| LLM | Ollama |
| Embeddings | Nomic Embed |
| Framework | LangChain |
| Vector DB | ChromaDB |
| Memory | SQLite |
| PDF Processing | PyPDFLoader |
| Language | Python |

---

## 📂 Project Structure

```text
pdf_rag_chatbot/
│
├── app.py
├── rag.py
├── memory.py
├── memory.db
│
├── chroma_db/
│
├── data/
│
├── utils.py
│
└── README.md
```

---

## ⚡ Installation

### Clone Repository

```bash
git clone https://github.com/Pruthvik1111/pdf-rag-chatbot-memory.git
cd pdf-rag-chatbot-memory
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download:

https://ollama.com

Pull Models:

```bash
ollama pull phi
```

```bash
ollama pull nomic-embed-text
```

---

## ▶️ Run Project

```bash
streamlit run app.py
```

---

## 📸 Demo

### Upload PDF

Upload any PDF document.

### Ask Questions

```text
Explain reverse a list
```

```text
What is dynamic programming?
```

```text
Give me the complexity of merge sort
```

---

## 🔥 Future Improvements

- [ ] Long-Term Semantic Memory
- [ ] Multi-PDF Support
- [ ] User Authentication
- [ ] Chat Export
- [ ] Voice Interface
- [ ] Agentic Retrieval
- [ ] Web Search Integration
- [ ] Hybrid Memory (SQLite + Vector Memory)

---

## 🧠 What I Learned

Building this project helped me understand:

- Retrieval-Augmented Generation (RAG)
- Embedding Models
- Vector Databases
- Semantic Search
- Memory Architectures
- Local LLM Deployment
- Prompt Engineering
- LangChain Pipelines

---

## 👨‍💻 Author

**Pruthvik R**

AI Engineer | GenAI Developer | Machine Learning Enthusiast

GitHub:
https://github.com/Pruthvik1111

---

⭐ If you found this project useful, consider giving it a star.
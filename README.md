# 🧠 AI-Powered RAG System for PDF Question Answering

This repository demonstrates a simple and efficient **Retrieval-Augmented Generation (RAG)** pipeline using:

- ✅ **LlamaIndex** for document parsing and query engine  
- 🦙 **Ollama** with `llama3` for natural‐language answering  
- 🧠 **BAAI/bge-large-en-v1.5** embedding model for semantic search  
- 📄 Automatic PDF directory loading and querying through vector search  

---

## 📌 What is Retrieval-Augmented Generation (RAG)?

RAG improves language‑model responses by combining two stages:

1. **Retrieval** – fetch the most relevant passages from a knowledge base.  
2. **Generation** – give that context to an LLM so it can produce accurate, grounded answers.

This lets models deliver factual, context‑aware, and up‑to‑date replies even when the knowledge is stored only in your documents.

> 💡 Perfect for querying private PDFs, HTML files, Markdown notes, etc.

### 🖼️ Architecture Overview

![RAG architecture diagram](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*9v9cSlHXvfBdRMfLpCwJ3g.png)

---

## ⚙️ Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/rag-pdf-qa.git
cd rag-pdf-qa
```

### 2. Install dependencies

Ensure Python 3.10+ and `pip` are available.

```bash
pip install -r requirements.txt
```

<details>
<summary>Manual install (if you prefer)</summary>

```bash
pip install llama-index
pip install llama-index-embeddings-huggingface
pip install llama-index-llms-ollama
```
</details>

### 3. Add your PDFs and run

1. Drop your `.pdf` files into the `database/` folder.  
2. Launch:

```bash
python app.py
```

---

## 📁 Project Structure

```
rag-pdf-qa/
│
├── database/            # All PDF files live here
├── app.py               # Main script (load, embed, query)
├── requirements.txt     # Python deps
└── README.md            # You’re reading it!
```

---

## 💬 Prompt Template (Agriculture QA)

```
You are an expert in agriculture.
Please provide a concise and clear explanation based on the context below.
If you don't know the answer, say "I don't know".
```

---

## 💡 Example Use

```python
response = query_engine.query("Can you tell me about agriculture?")
print(response)
```

---

## 🚀 Tech Stack

| Layer | Tool / Model | Purpose |
|-------|--------------|---------|
| **Ingestion & Query** | LlamaIndex | Load PDFs, build vector index, query |
| **Embeddings** | BAAI/bge-large-en-v1.5 | High-quality sentence embeddings |
| **LLM** | Ollama + Llama 3 | Local inference with streaming |
| **Prompting** | PromptTemplate | Domain-specific answer style |

---

## 📃 License

MIT – free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [LlamaIndex](https://github.com/jerryjliu/llama_index)  
- [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5)  
- [Ollama](https://ollama.com)  
- RAG concept image by *Medium* article author (linked above)

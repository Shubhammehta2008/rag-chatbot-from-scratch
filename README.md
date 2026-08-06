# 🤖 GenAI Learning: RAG Chatbot & Experiments

A hands-on collection of Generative AI / Retrieval-Augmented Generation (RAG)
building blocks in Python — text chunking, embeddings, a vector store, prompt
engineering, and a memory-enabled chatbot UI — powered by [Groq](https://groq.com/)
(LLaMA 3.3 70B), [ChromaDB](https://www.trychroma.com/), and
[Sentence-Transformers](https://www.sbert.net/).

This repo is meant as a learning/reference project: each script isolates one
RAG concept so you can run and inspect it independently, and `rag_pipeline.py`
ties them all together into a full retrieval → generation flow.

## Features

- 💬 **Chat UI with memory** — Streamlit chat interface that remembers the
  full conversation within a session (`src/chatbot_app.py`)
- ✂️ **Text chunking** — fixed-size chunking with configurable overlap
  (`src/chunking.py`)
- 🧠 **Embeddings** — sentence embeddings + cosine similarity demo
  (`src/embedding_demo.py`)
- 🗄️ **Vector store** — store and query documents in ChromaDB
  (`src/vector_store_demo.py`)
- 📝 **Prompt engineering** — context-grounded prompt template that reduces
  hallucination (`src/prompts.py`)
- 🔗 **End-to-end RAG pipeline** — load → chunk → embed → retrieve → prompt →
  generate (`src/rag_pipeline.py`)

## Tech Stack

| Purpose         | Tool                                        |
|------------------|---------------------------------------------|
| LLM inference    | Groq API (LLaMA 3.3 70B Versatile)          |
| Web UI           | Streamlit                                   |
| Vector database  | ChromaDB                                    |
| Embeddings       | Sentence-Transformers (`all-MiniLM-L6-v2`)  |
| Config/secrets   | python-dotenv                               |

## Project Structure

```
genai-learning/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── data/
│   └── sample.txt            # sample source document for the RAG demo
└── src/
    ├── chatbot_app.py        # Streamlit chatbot with conversation memory
    ├── rag_pipeline.py       # full RAG pipeline (chunk -> store -> retrieve -> generate)
    ├── chunking.py           # chunk_text() utility
    ├── embedding_demo.py     # embeddings + cosine similarity demo
    ├── vector_store_demo.py  # standalone ChromaDB demo
    └── prompts.py            # build_prompt() RAG prompt template
```

## Prerequisites

- Python 3.10+
- A free [Groq API key](https://console.groq.com/keys)

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd genai-learning
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and paste in your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

**Run the chatbot (Streamlit UI):**
```bash
streamlit run src/chatbot_app.py
```
Opens in your browser at `http://localhost:8501`.

**Run the full RAG pipeline (command line):**
```bash
python src/rag_pipeline.py
```
Loads `data/sample.txt`, chunks it, stores the chunks in ChromaDB, retrieves
the chunks relevant to a sample question, and asks Groq to answer using only
that retrieved context.

**Run an individual concept demo:**
```bash
python src/chunking.py
python src/embedding_demo.py
python src/vector_store_demo.py
```

## How It Works

1. **Chunking** — long documents are split into overlapping character chunks
   so retrieval can operate on small, relevant pieces of text instead of the
   whole document.
2. **Storage & retrieval** — chunks are stored in a ChromaDB collection,
   which embeds them and indexes them for similarity search.
3. **Retrieval** — for a given question, ChromaDB returns the most
   semantically similar chunks.
4. **Prompting** — the retrieved chunks are inserted into a prompt template
   that instructs the model to answer *only* from that context (and say so
   when it can't), which reduces hallucination.
5. **Generation** — the final prompt is sent to Groq's LLaMA 3.3 70B model
   for a fast, low-latency response.
6. **Memory (chatbot only)** — the Streamlit app keeps the full message
   history in `st.session_state` and resends it with every request so the
   model retains context across turns.

## Roadmap / Ideas

- [ ] Persist ChromaDB to disk instead of an in-memory client
- [ ] Support uploading your own documents in the Streamlit UI
- [ ] Add automated tests for `chunk_text()` and `build_prompt()`
- [ ] Add a `Dockerfile` for one-command setup

## License

This project is for learning purposes. Add a license (e.g. MIT) if you plan
to share or reuse it publicly.

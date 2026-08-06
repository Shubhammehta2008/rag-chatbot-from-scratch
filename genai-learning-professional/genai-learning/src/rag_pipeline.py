"""End-to-end RAG (Retrieval-Augmented Generation) demo.

Pipeline: load a text file -> chunk it -> embed & store in ChromaDB ->
retrieve chunks relevant to a query -> build a grounded prompt -> ask Groq.

Run with:
    python src/rag_pipeline.py
"""

import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from groq import Groq

from chunking import chunk_text
from prompts import build_prompt

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "sample.txt"
MODEL_NAME = "llama-3.3-70b-versatile"
QUERY = "Which programming language is used in AI?"


def main() -> None:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise SystemExit(
            "GROQ_API_KEY is not set. Copy .env.example to .env and add your key."
        )

    # 1. Load and chunk the source document
    text = DATA_FILE.read_text(encoding="utf-8")
    chunks = chunk_text(text, chunk_size=100, overlap=20)
    print(f"Total chunks: {len(chunks)}")

    # 2. Store chunks in a ChromaDB collection
    client = chromadb.Client()
    collection = client.create_collection("rag_collection")
    collection.add(
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))],
    )
    print(f"Chunks stored in ChromaDB: {collection.count()}")

    # 3. Retrieve the chunks most relevant to the query
    results = collection.query(query_texts=[QUERY], n_results=2)
    retrieved_chunks = results["documents"][0]

    print("\nQuestion:", QUERY)
    print("\nRetrieved chunks:")
    for i, doc in enumerate(retrieved_chunks, start=1):
        print(f"\nResult {i}\n{'-' * 40}\n{doc}")

    # 4. Build a context-grounded prompt
    context = "\n".join(retrieved_chunks)
    prompt = build_prompt(context=context, query=QUERY)

    # 5. Ask the LLM (Groq / LLaMA 3.3 70B)
    groq_client = Groq(api_key=api_key)
    response = groq_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )

    print("\nAnswer:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

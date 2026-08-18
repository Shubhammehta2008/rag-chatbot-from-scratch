"""End-to-end RAG (Retrieval-Augmented Generation) demo.

Pipeline: load a text file -> chunk it -> embed & store in ChromaDB ->
retrieve chunks relevant to a query -> build a grounded prompt -> ask Groq.

Run with:
    python src/rag_pipeline.py
"""

# rag_pipeline.py

import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from groq import Groq

from chunking import chunk_text
from embedding import embed_texts, embed_query
from prompts import build_prompt



MODEL_NAME = "qwen/qwen3.6-27b"

DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "sample.txt"
)


def create_rag_collection():
    """Document ko load, chunk aur ChromaDB mein store karta hai."""

    text = DATA_FILE.read_text(encoding="utf-8")
  # chunks document
    chunks = chunk_text(
        text,
        chunk_size=100,
        overlap=20,
    )
     # 3. Generate embeddings
    embeddings = embed_texts(chunks)

     # 4. Create ChromaDB
    client = chromadb.Client()

    collection = client.get_or_create_collection(
        name="rag_collection"
    )
     # 5. Store chunks + vectors
    
    if collection.count() == 0:

        collection.add(
            documents=chunks,

            embeddings=embeddings.tolist(),

            ids=[
                f"chunk_{i}"
                for i in range(len(chunks))
            ],
        )


    return collection

   

def ask_rag(query: str) -> str:
   #api key
    load_dotenv()

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is not set."
        )

    # 1. ChromaDB collection
    collection = create_rag_collection()

    # 3. Convert query → embedding
    # -----------------------------

    query_embedding = embed_query(query)

   # 2. Relevant chunks retrieve karo
    results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=2,
    )
 
    retrieved_chunks = results["documents"][0]

    # 3. Context banao
    context = "\n".join(retrieved_chunks)

    # 4. Prompt banao
    prompt = build_prompt(
        context=context,
        query=query,
    )

    # 5. LLM call
    groq_client = Groq(
        api_key=api_key
    )

    response =( groq_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
   )   

    # 6. Answer return karo
    return response.choices[0].message.content

if __name__ == "__main__":
    print(ask_rag("What is Python?"))
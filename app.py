
# open file and read text
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

#    text chunking
def chunk_text(text, chunk_size, overlap):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks


chunks = chunk_text(text, chunk_size=100, overlap=20)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-" * 40)
    print(chunk)

#   vector database integration
import chromadb

client = chromadb.Client()

collection = client.create_collection("rag_collection")
collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print(collection.count())

#   user query and retrieve relevant chunks
query = "Which programming language is used in AI?"

results = collection.query(
    query_texts=[query],
    n_results=2
)

print("\nQuestion:")
print(query)

print("\nRetrieved Chunks:")
for i, doc in enumerate(results["documents"][0], start=1):
    print(f"\nResult {i}")
    print("-" * 40)
    print(doc)

    #promt engineering

context = "\n".join(results["documents"][0])

prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

print(prompt)

#  gemini integration
from groq import Groq
import os

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)
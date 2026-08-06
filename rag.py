with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

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


import chromadb

client = chromadb.Client()

collection = client.create_collection("rag_collection")
collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print(collection.count())


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

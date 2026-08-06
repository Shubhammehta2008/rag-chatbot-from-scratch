#   vector database integration
import chromadb

client = chromadb.Client()

collection = client.create_collection("rag_collection")
collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print(collection.count())

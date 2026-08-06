"""Minimal demo: store documents in ChromaDB and query them by similarity.

Run with:
    python src/vector_store_demo.py
"""

import chromadb


def main() -> None:
    client = chromadb.Client()
    collection = client.create_collection(name="my_collection")

    collection.add(
        documents=[
            "Python is a programming language.",
            "C++ is used for high performance applications.",
            "RAG combines retrieval with generation.",
        ],
        ids=["doc1", "doc2", "doc3"],
    )

    results = collection.query(
        query_texts=["which language is used for high performance?"],
        n_results=1,
    )

    print("Query results:", results)
    print("Collection name:", collection.name)
    print("Documents stored:", collection.count())


if __name__ == "__main__":
    main()

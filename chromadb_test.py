import chromadb
clint = chromadb.Client()
collection = clint.create_collection(name="my_collection")
collection.add(
    documents=[ "Python is a programming language.",
                "C++ is used for high performance applications.",
                "RAG combines retrieval with generation."
                 ],
                ids=["doc1", "doc2", "doc3"]
                )
results =collection.query(
   query_texts=["which language is used for high performance ?"],
     n_results=1,
    
)
print(results)

print("Collection created:", collection.name)
print("Documents added:", collection.count())
"""Minimal demo: generate sentence embeddings and compare them with cosine similarity.

Run with:
    python src/embedding.py
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_NAME = "all-MiniLM-L6-v2"



model = SentenceTransformer(MODEL_NAME)


def embed_texts(texts: list[str]):
    """Convert multiple texts into embedding vectors."""
    return model.encode(texts)

def embed_query(query: str):
    """Convert one user query into an embedding vector."""
    return model.encode([query])

def calculate_similarity(
    embedding1,
    embedding2,
):
    """Calculate cosine similarity between two embeddings."""
    return cosine_similarity(
        embedding1,
        embedding2,
    )



if __name__ == "__main__":

    text1 = "I love Python"
    text2 = "The weather is very cold today"

    embedding1 = model.encode([text1])
    embedding2 = model.encode([text2])

    similarity = cosine_similarity(embedding1, embedding2)

    print("Embedding type:", type(embedding1))
    print("Embedding shape:", embedding1.shape)
    print(
        f"Similarity : {similarity[0][0]:.4f}"
        )
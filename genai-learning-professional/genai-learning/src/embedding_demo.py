"""Minimal demo: generate sentence embeddings and compare them with cosine similarity.

Run with:
    python src/embedding_demo.py
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_NAME = "all-MiniLM-L6-v2"


def main() -> None:
    model = SentenceTransformer(MODEL_NAME)

    text1 = "I love Python"
    text2 = "The weather is very cold today"

    embedding1 = model.encode([text1])
    embedding2 = model.encode([text2])

    similarity = cosine_similarity(embedding1, embedding2)

    print("Embedding type:", type(embedding1))
    print("Embedding shape:", embedding1.shape)
    print(f"Similarity between:\n  '{text1}'\n  '{text2}'\n-> {similarity[0][0]:.4f}")


if __name__ == "__main__":
    main()

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

text1 = "I love Python"
text2 = "The weather is very cold today"

embedding1 = model.encode([text1])
embedding2 = model.encode([text2])

similarity = cosine_similarity(embedding1, embedding2)

print(type(embedding1))
print(type(embedding2))
print("Shape:", embedding1.shape)
print("Similarity:", similarity)

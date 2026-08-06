def build_prompt(context, query):
    return f"""
You are a helpful AI assistant.

Use ONLY the provided context to answer the question.
If the answer is not present in the context, reply:
"I don't know based on the provided document."

Context:
{context}

Question:
{query}

Answer:
"""
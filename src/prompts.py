"""Prompt-construction helpers for the RAG pipeline."""


def build_prompt(context: str, query: str) -> str:
    """Build a context-grounded RAG prompt.

    The model is instructed to answer only from the supplied context and to
    say so explicitly when the answer isn't present, which reduces
    hallucination.
    """
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

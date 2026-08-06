"""Simple fixed-size text chunking with overlap."""


def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
    """Split `text` into overlapping chunks.

    Args:
        text: The text to split.
        chunk_size: Number of characters per chunk.
        overlap: Number of overlapping characters between consecutive chunks.

    Returns:
        A list of text chunks.
    """
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(text), step):
        chunks.append(text[i : i + chunk_size])
    return chunks


if __name__ == "__main__":
    document = """
    Python is a programming language.
    It is widely used in AI and Machine Learning.
    Python is also used in Web Development.
    It has a simple syntax.
    Millions of developers use Python every day.
    """
    result = chunk_text(document, chunk_size=100, overlap=20)
    print(f"Total chunks: {len(result)}")
    for i, c in enumerate(result, start=1):
        print(f"\nChunk {i}\n{'-' * 40}\n{c}")

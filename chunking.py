
document = """
Python is a programming language.
It is widely used in AI and Machine Learning.
Python is also used in Web Development.
It has a simple syntax.
Millions of developers use Python every day.
"""
def chunk_text(text, chunk_size, overlap):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks


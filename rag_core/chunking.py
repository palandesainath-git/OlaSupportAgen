import re

def fixed_size_chunks(text, chunk_size=300, overlap=50):
    """Split text into overlapping fixed-size chunks."""
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
        if i + chunk_size >= len(text):
            break
    return chunks

def sentence_chunks(text):
    """Split text into sentence-based chunks."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences


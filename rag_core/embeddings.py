from sentence_transformers import SentenceTransformer

def get_model():
    """Load local embedding model."""
    return SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    """Return embeddings for list of texts."""
    model = get_model()
    return model.encode(texts, show_progress_bar=False)


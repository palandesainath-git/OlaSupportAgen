import chromadb
from chromadb.utils import embedding_functions
from embeddings import embed_texts
from chunking import fixed_size_chunks, sentence_chunks

def build_collections(docs):
    """Create two ChromaDB collections for both chunking strategies."""
    client = chromadb.Client()
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

    fixed_coll = client.create_collection("fixed_chunks", embedding_function=ef)
    sent_coll = client.create_collection("sentence_chunks", embedding_function=ef)

    for i, doc in enumerate(docs):
        fixed_chunks = fixed_size_chunks(doc)
        sent_chunks = sentence_chunks(doc)
        fixed_coll.add(documents=fixed_chunks, ids=[f"F{i}_{j}" for j in range(len(fixed_chunks))])
        sent_coll.add(documents=sent_chunks, ids=[f"S{i}_{j}" for j in range(len(sent_chunks))])

    return fixed_coll, sent_coll

def retrieve_answer(query, collection, top_k=3, threshold=0.65):
    """Retrieve top-k chunks and generate grounded answer."""
    results = collection.query(query_texts=[query], n_results=top_k)
    if not results["documents"]:
        return {"answer": "I don't know.", "confidence": 0.0}

    # Simple similarity-based groundedness
    scores = results["distances"][0]
    best_score = min(scores)
    if best_score > threshold:
        return {"answer": "I don't know.", "confidence": 0.0}

    context = " ".join(results["documents"][0])
    return {"answer": context, "confidence": round(1 - best_score, 2)}


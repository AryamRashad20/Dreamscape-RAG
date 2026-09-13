import json

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from backend.app.core.config import settings


# Load the embedding model
embedding_model = SentenceTransformer(
    settings.EMBEDDING_MODEL_NAME
)


# Load the persisted FAISS index
index = faiss.read_index(
    str(settings.INDEX_PATH)
)


# Load chunk metadata
with open(settings.METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)


def retrieve_chunks(query: str, top_k: int | None = None):
    """
    Retrieve the most relevant Dreamscape chunks for a question.
    """

    if top_k is None:
        top_k = settings.TOP_K

    # Convert the question into an embedding
    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    # Normalize for cosine similarity with IndexFlatIP
    faiss.normalize_L2(query_embedding)

    # Search the persisted FAISS index
    scores, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue

        chunk = metadata[idx]

        results.append({
            "score": float(score),
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "text": chunk["text"]
        })

    return results
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "document_chunks"
MODEL_NAME = "all-MiniLM-L6-v2"


def _client(persist_directory: str) -> chromadb.PersistentClient:
    Path(persist_directory).mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=persist_directory)


def build_index(chunks: list[str], persist_directory: str = "storage") -> int:
    if not chunks:
        raise ValueError("At least one non-empty document chunk is required")
    client = _client(persist_directory)
    try:
        client.delete_collection(COLLECTION_NAME)
    except ValueError:
        pass
    collection = client.create_collection(COLLECTION_NAME)
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(chunks).tolist()
    collection.add(
        ids=[f"chunk-{index}" for index in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings,
        metadatas=[{"chunk_number": index + 1} for index in range(len(chunks))],
    )
    return collection.count()


def semantic_search(query: str, persist_directory: str = "storage", limit: int = 3) -> list[dict]:
    client = _client(persist_directory)
    collection = client.get_collection(COLLECTION_NAME)
    count = collection.count()
    if count == 0:
        return []
    model = SentenceTransformer(MODEL_NAME)
    response = collection.query(
        query_embeddings=[model.encode(query).tolist()],
        n_results=min(limit, count),
        include=["documents", "distances", "metadatas"],
    )
    return [
        {
            "chunk_number": metadata["chunk_number"],
            "text": document,
            "distance": round(float(distance), 4),
        }
        for document, distance, metadata in zip(
            response["documents"][0], response["distances"][0], response["metadatas"][0]
        )
    ]

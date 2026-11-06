import chromadb
from .config import CHROMA_DIR, COLLECTION_NAME

def get_client():
    return chromadb.PersistentClient(path=str(CHROMA_DIR))

def get_collection():
    return get_client().get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )

def upsert_records(records, embeddings, reset: bool = False):
    if len(records) != len(embeddings):
        raise ValueError("Jumlah record dan embedding tidak sama")
    client = get_client()
    if reset:
        try:
            client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass
        collection = client.create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )
    else:
        collection = client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )
    batch_size = 400
    for start in range(0, len(records), batch_size):
        batch = records[start:start + batch_size]
        vectors = embeddings[start:start + batch_size]
        collection.upsert(
            ids=[r["id"] for r in batch],
            embeddings=vectors,
            documents=[r["text"] for r in batch],
            metadatas=[r["metadata"] for r in batch],
        )
    return collection

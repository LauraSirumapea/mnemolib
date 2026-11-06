import json
from src.config import DATA_PROCESSED, CHUNK_SIZE_WORDS, CHUNK_OVERLAP_WORDS, EMBEDDING_MODEL
from src.document_loader import load_documents
from src.text_cleaner import clean_text
from src.chunking import chunk_documents
from src.embedding import embed_texts
from src.vector_store import upsert_records

def main():
    docs = load_documents()
    if not docs:
        raise SystemExit("Tidak ada dokumen PDF/TXT terbaca. Periksa data/raw.")
    for doc in docs:
        doc["text"] = clean_text(doc["text"])
    print(f"Dokumen berhasil dibaca: {len(docs)}")
    for doc in docs:
        print(f" - {doc['source']}: {len(doc['text'])} karakter")
    records = chunk_documents(docs, CHUNK_SIZE_WORDS, CHUNK_OVERLAP_WORDS)
    if not records:
        raise SystemExit("Tidak ada chunk yang dihasilkan.")
    print(f"Total chunk: {len(records)}")
    vectors = embed_texts([record["embedding_text"] for record in records])
    collection = upsert_records(records, vectors, reset=True)
    manifest = {
        "documents": len(docs), "chunks": len(records),
        "collection": collection.name, "embedding_model": EMBEDDING_MODEL,
        "chunk_size_words": CHUNK_SIZE_WORDS,
        "chunk_overlap_words": CHUNK_OVERLAP_WORDS,
        "sources": [doc["source"] for doc in docs],
    }
    path = DATA_PROCESSED / "ingestion_manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Ingestion selesai. ChromaDB berisi {collection.count()} chunk.")
    print(f"Manifest: {path}")

if __name__ == "__main__":
    main()

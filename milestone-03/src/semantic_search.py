
import re

from .config import DEFAULT_TOP_K, OOD_THRESHOLD
from .embedding import embed_query
from .vector_store import get_collection


STOPWORDS = {
    "yang", "dan", "di", "ke", "dari", "pada", "untuk", "dengan", "atau",
    "apa", "bagaimana", "saya", "ingin", "mau", "cara", "bisa", "ini", "itu",
    "tentang", "pernah", "adalah", "dalam", "sebuah", "suatu", "agar",
    "the", "a", "an", "of", "to", "is", "are", "how", "what"
}

# Normalisasi variasi istilah perpustakaan.
TERM_ALIASES = {
    "keanggotaan": "anggota",
    "keanggotaan": "anggota",
    "pendaftaran": "daftar",
    "mendaftar": "daftar",
    "terdaftar": "daftar",
    "peminjaman": "pinjam",
    "meminjam": "pinjam",
    "dipinjam": "pinjam",
    "pengembalian": "kembali",
    "mengembalikan": "kembali",
    "dikembalikan": "kembali",
    "persyaratan": "syarat",
    "persyaratannya": "syarat",
    "persyaratan": "syarat",
    "persyaratannya": "syarat",
}


def normalize_token(word: str) -> str:
    """Normalize selected Indonesian library-domain terms."""
    return TERM_ALIASES.get(word, word)


def tokenize(text):
    words = re.findall(r"[a-z0-9]+", (text or "").lower())

    return {
        normalize_token(word)
        for word in words
        if len(word) > 1 and word not in STOPWORDS
    }


def semantic_search(
    query: str,
    top_k: int = DEFAULT_TOP_K,
    threshold: float = OOD_THRESHOLD
):
    if not query or not query.strip():
        raise ValueError("Query tidak boleh kosong")

    if top_k <= 0:
        raise ValueError("top_k harus lebih besar dari 0")

    collection = get_collection()
    count = collection.count()

    if count == 0:
        raise RuntimeError(
            "Database kosong. Jalankan python ingest.py terlebih dahulu."
        )

    candidate_k = min(count, max(top_k * 5, 20))

    vector = embed_query(query)

    found = collection.query(
        query_embeddings=[vector],
        n_results=candidate_k,
        include=["documents", "metadatas", "distances"]
    )

    documents = found["documents"][0]
    metadatas = found["metadatas"][0]
    distances = found["distances"][0]

    query_terms = tokenize(query)

    results = []
    semantic_scores = []

    for body, metadata, distance in zip(
        documents, metadatas, distances
    ):
        semantic = max(
            0.0,
            min(1.0, 1.0 - float(distance))
        )

        semantic_scores.append(semantic)

        body_terms = tokenize(body)

        title_text = (
            metadata.get("title", "")
            + " "
            + metadata.get("source", "")
        )

        title_terms = tokenize(title_text)

        lexical = (
            len(query_terms & body_terms)
            / max(1, len(query_terms))
        )

        title = (
            len(query_terms & title_terms)
            / max(1, len(query_terms))
        )

        hybrid = (
            0.65 * semantic
            + 0.20 * lexical
            + 0.15 * title
        )

        results.append({
            "text": body,
            "metadata": metadata,
            "similarity": semantic,
            "lexical_score": lexical,
            "title_score": title,
            "hybrid_score": hybrid,
        })

    results.sort(
        key=lambda item: item["hybrid_score"],
        reverse=True
    )

    top_semantic = (
        max(semantic_scores)
        if semantic_scores else 0.0
    )

    return {
        "query": query,
        "status": (
            "IN-DOMAIN"
            if top_semantic >= threshold
            else "OUT-OF-DOMAIN"
        ),
        "top_score": top_semantic,
        "threshold": threshold,
        "results": results[:top_k],
    }

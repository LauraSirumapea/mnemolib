from functools import lru_cache
from typing import List
from sentence_transformers import SentenceTransformer
from .config import EMBEDDING_MODEL

@lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer(EMBEDDING_MODEL)

def embed_texts(texts: List[str]):
    if not texts:
        return []
    vectors = get_model().encode(
        texts, batch_size=32, show_progress_bar=True,
        convert_to_numpy=True, normalize_embeddings=True
    )
    return vectors.tolist()

def embed_query(text: str):
    return get_model().encode(
        [text], convert_to_numpy=True, normalize_embeddings=True
    )[0].tolist()

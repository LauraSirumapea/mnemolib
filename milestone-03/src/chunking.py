import re
from typing import Dict, List
from .text_cleaner import clean_text

def title_from_filename(filename: str) -> str:
    stem = filename.rsplit(".", 1)[0]
    return re.sub(r"\s+", " ", re.sub(r"[_-]+", " ", stem)).strip()

def chunk_text(text: str, chunk_size: int = 140, overlap: int = 30) -> List[str]:
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("chunk_size harus > 0 dan overlap harus >= 0 serta < chunk_size")
    words = clean_text(text).split()
    if not words:
        return []
    step = chunk_size - overlap
    chunks = []
    for start in range(0, len(words), step):
        part = " ".join(words[start:start + chunk_size]).strip()
        if part:
            chunks.append(part)
        if start + chunk_size >= len(words):
            break
    return chunks

def chunk_documents(documents: List[Dict], chunk_size: int = 140,
                    overlap: int = 30) -> List[Dict]:
    records = []
    for doc in documents:
        title = title_from_filename(doc["source"])
        for index, body in enumerate(chunk_text(doc["text"], chunk_size, overlap), start=1):
            records.append({
                "id": f'{doc["id"]}__chunk_{index:04d}',
                "text": body,
                "embedding_text": f"Judul dokumen: {title}. Isi dokumen: {body}",
                "metadata": {
                    "source": doc["source"],
                    "title": title,
                    "document_id": doc["id"],
                    "chunk_index": index,
                    "file_type": doc.get("file_type", "unknown"),
                },
            })
    return records

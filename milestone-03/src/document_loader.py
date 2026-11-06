from pathlib import Path
from typing import Dict, List
from pypdf import PdfReader
from .config import DATA_RAW

SUPPORTED_EXTENSIONS = {".pdf", ".txt"}

def load_documents(directory: Path = DATA_RAW) -> List[Dict]:
    """Load PDF/TXT corpus files. Empty or unreadable files are skipped with a warning."""
    directory = Path(directory)
    if not directory.exists():
        raise FileNotFoundError(f"Folder korpus tidak ditemukan: {directory}")
    documents = []
    for path in sorted(directory.iterdir()):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        try:
            if path.suffix.lower() == ".pdf":
                reader = PdfReader(str(path))
                page_text = []
                for page_number, page in enumerate(reader.pages, start=1):
                    text = page.extract_text() or ""
                    if text.strip():
                        page_text.append(f"[Halaman {page_number}]\n{text}")
                content = "\n\n".join(page_text)
            else:
                content = path.read_text(encoding="utf-8", errors="replace")
            if not content.strip():
                print(f"PERINGATAN: tidak ada teks yang dapat diekstrak dari {path.name}")
                continue
            documents.append({
                "id": path.stem,
                "source": path.name,
                "text": content,
                "file_type": path.suffix.lower().lstrip("."),
            })
        except Exception as exc:
            print(f"PERINGATAN: gagal membaca {path.name}: {exc}")
    return documents

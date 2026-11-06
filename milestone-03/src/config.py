from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
CHROMA_DIR = PROJECT_ROOT / "chroma_db"
EVALUATION_DIR = PROJECT_ROOT / "evaluation"
REPORTS_DIR = PROJECT_ROOT / "reports"

EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
COLLECTION_NAME = "mnemolib_milestone3_hybrid"
CHUNK_SIZE_WORDS = 140
CHUNK_OVERLAP_WORDS = 30
DEFAULT_TOP_K = 5
OOD_THRESHOLD = 0.30

for path in (DATA_RAW, DATA_PROCESSED, CHROMA_DIR, EVALUATION_DIR, REPORTS_DIR):
    path.mkdir(parents=True, exist_ok=True)

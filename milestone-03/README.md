# MnemoLib — Milestone 3 (Complete Source)

## Isi
Implementasi document loading PDF/TXT, text cleaning, word-aware chunking, Sentence-Transformers embedding, persistent ChromaDB, title-aware hybrid semantic search, OOD threshold baseline, benchmark dan evaluasi.

## Persiapan
- Python 3.11 atau 3.12 direkomendasikan.
- Letakkan 10–15 PDF/TXT korpus asli di `data/raw/`.
- Pastikan PDF berisi teks yang dapat diseleksi; PDF hasil scan memerlukan OCR yang belum disertakan.

## Instalasi Windows PowerShell
Jalankan dari folder milestone-03:
```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Jalankan pipeline
```powershell
python -m pytest -q
python ingest.py
python search.py "Bagaimana prosedur mencari dan mengakses jurnal ilmiah?"
python benchmark.py
```

`ingest.py` membaca seluruh PDF/TXT dari `data/raw`, membersihkan teks, membuat chunk 140 kata dengan overlap 30 kata, membuat embedding, lalu membangun ulang koleksi ChromaDB secara persisten. Jalankan ulang ingestion setelah menambah/mengubah dokumen atau konfigurasi chunking.

## Evaluasi
Edit `evaluation/test_queries.csv`. Untuk setiap kueri in-domain, isi `expected_doc` dengan nama file target yang benar-benar diverifikasi dari isi korpus, misalnya `LAYANAN-JURNAL-DAN-MAJALAH-CETAK.pdf`. Jangan mengarang ground truth. Kueri OOD diberi kategori `ood` dan expected_doc boleh kosong.
Lalu jalankan:
```powershell
python benchmark.py
```
Hasil tersimpan di `reports/evaluation_results.csv`. Precision@1, Precision@5, Recall@5, dan MRR@5 hanya dihitung dari kueri yang memiliki expected_doc.

## Struktur
- `src/`: seluruh modul inti.
- `data/raw/`: dokumen korpus asli milik pengguna.
- `data/processed/`: manifest ingestion.
- `chroma_db/`: database vektor persisten.
- `evaluation/`: kueri benchmark.
- `reports/`: hasil evaluasi.

## Catatan metodologis
Hybrid score merupakan skor pemeringkatan (bukan probabilitas). Bobot awal 0.65 semantic, 0.20 lexical, 0.15 title harus dievaluasi, bukan dianggap optimal. Ambang OOD 0.30 adalah baseline dan harus dikalibrasi dengan data kueri berlabel. Metrik retrieval tidak valid tanpa ground truth yang telah diperiksa.

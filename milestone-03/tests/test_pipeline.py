from src.text_cleaner import clean_text
from src.chunking import chunk_text, chunk_documents, title_from_filename
from src.semantic_search import tokenize

def test_clean_text_normalizes_whitespace():
    assert clean_text("A   B\r\n\r\n\r\nC") == "A B\n\nC"

def test_chunk_size_respected():
    chunks = chunk_text(" ".join(f"kata{i}" for i in range(450)), 100, 20)
    assert len(chunks) > 1
    assert all(len(chunk.split()) <= 100 for chunk in chunks)

def test_overlap_preserved():
    chunks = chunk_text(" ".join(f"w{i}" for i in range(150)), 100, 20)
    assert chunks[0].split()[-20:] == chunks[1].split()[:20]

def test_invalid_chunk_parameters():
    try:
        chunk_text("teks", 10, 10)
        assert False
    except ValueError:
        assert True

def test_title_derived_from_pdf_filename():
    assert title_from_filename("LAYANAN-JURNAL-DAN-MAJALAH-CETAK.pdf") == "LAYANAN JURNAL DAN MAJALAH CETAK"

def test_chunk_documents_embeds_title_context():
    docs = [{"id":"DOC1","source":"LAYANAN-KEANGGOTAAN.pdf","text":" ".join(["anggota"]*35),"file_type":"pdf"}]
    chunks = chunk_documents(docs, 20, 5)
    assert chunks[0]["metadata"]["title"] == "LAYANAN KEANGGOTAAN"
    assert "Judul dokumen: LAYANAN KEANGGOTAAN" in chunks[0]["embedding_text"]

def test_tokenize_keeps_domain_words():
    assert "jurnal" in tokenize("Bagaimana layanan jurnal dan majalah?")

def test_tokenize_normalizes_library_terms():
    assert "anggota" in tokenize("keanggotaan")
    assert "anggota" in tokenize("anggota")
    assert "daftar" in tokenize("pendaftaran")
    assert "pinjam" in tokenize("peminjaman")
    assert "kembali" in tokenize("pengembalian")

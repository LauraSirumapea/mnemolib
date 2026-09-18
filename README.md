# MnemoLib: Enterprise AI Assistant & Library Copilot

> **Sistem Katalog Perpustakaan Cerdas Berbasis Contextual Match & Semantic Search untuk Identifikasi Buku dan Jurnal Melalui Potongan Ingatan Pengguna**
> 
> *Mata Kuliah: 10S3001 - Artificial Intelligence / Kecerdasan Buatan (3 SKS)*  
> *Program Studi Sarjana Sistem Informasi — Fakultas Informatika dan Teknik Elektro*  
> *Institut Teknologi Del — Semester Gasal 2026/2027*

---

## 1. Anggota Tim & Pembagian Peran Profesional

Proyek dikerjakan secara kolaboratif mengadopsi standar tim rekayasa AI enterprise:

| Nama | Akun GitHub | Peran Rekayasa (PjBL Professional Role) | Tanggung Jawab Utama |
|---|---|---|---|
| **Laura Sirumapea** | [@LauraSirumapea](https://github.com/LauraSirumapea) | **AI Architect & Model Lead** | Desain arsitektur agen, siklus penalaran ReAct, formulasi ruang keadaan & search, perancangan system prompt, integrasi Google GenAI SDK. |
| **Desnita Pardosi** | [@DesnitaPardosi](https://github.com/DesnitaPardosi) | **Data & Knowledge Engineer** | Kurasi korpus dokumen, strategi pemotongan teks (*Word-aware Chunking*), pembuatan dense embeddings, pengelolaan ChromaDB, dan ekstraksi OCR. |
| **Mia Sibuea** | [@MiaSibuea](https://github.com/MiaSibuea) | **Integration & Interface Engineer** | Pembangunan tool server FastMCP (JSON-RPC), integrasi API katalog, antarmuka web interaktif Gradio, streaming token, dan isolasi sesi multi-turn. |
| *Kolaboratif Tim* | *Seluruh Anggota* | **QA, Evaluation & Ethics Lead** | Evaluasi mutu respons (*LLM-as-a-Judge*), pengujian otomatis pytest, audit kepatuhan UU PDP No. 27/2022, dan evaluasi *Prompt Injection*. |

---

## 2. Profil Organisasi & Problem Framing

* **Organisasi Mitra**: Perpustakaan & Pusat Informasi Institut Teknologi Del (IT Del Library & Information Center).
* **Konteks Masalah**: Civitas akademika (mahasiswa dan peneliti) sering kali mengalami fenomena *Tip-of-the-Tongue*, di mana mereka membutuhkan literatur tertentu namun hanya mengingat potongan cerita, latar studi kasus, atau nama karakter tanpa mengingat judul atau penulis eksak.
* **Kelemahan Sistem Eksisting**: Sistem katalog OPAC konvensional menggunakan pencocokan leksikal kaku (*exact string match*), yang menghasilkan kegagalan penelusuran (*zero search results*) ketika kueri pengguna bersifat naratif parsial. Akibatnya, pustakawan menghabiskan rata-rata 10–20 menit per pengguna untuk wawancara referensi manual.
* **Justifikasi AI**: MnemoLib mengombinasikan penalaran graf simbolik (UCS) untuk seleksi jalur komputasi berlatensi minimum, *Dense Vector Embeddings* (*Sentence-Transformers* + ChromaDB) untuk pencarian kemiripan semantik, serta *Agentic ReAct Loop* ter-grounded untuk dialog rekomendasi cerdas.

> Dokumen analisis lengkap dapat diakses pada: [`docs/milestone-01/problem-framing.md`](docs/milestone-01/problem-framing.md).

---

## 3. Spesifikasi Formal PEAS

| Komponen PEAS | Rincian Terukur & Spesifikasi Kuantitatif |
|---|---|
| **Performance Measure**<br>*(Ukuran Kinerja)* | • **Retrieval Precision@5**: $\ge 85\%$ pada kueri ingatan parsial.<br>• **Mean Reciprocal Rank (MRR)**: $\ge 0.75$.<br>• **Search Traversal Latency**: $\le 50\text{ ms}$ untuk seleksi jalur ruang keadaan.<br>• **End-to-End Latency**: $\le 1.5\text{ detik}$ hingga hasil disajikan di antarmuka.<br>• **Query Success Rate**: $\ge 90\%$ kueri parsial berhasil diarahkan ke buku target.<br>• **Relevance Guardrail**: Ambang batas relevansi kosinus $\tau \ge 0.70$. |
| **Environment**<br>*(Lingkungan)* | • Korpus $\ge 15.000$ rekaman metadata buku dan $\ge 5.000$ dokumen karya ilmiah/skripsi.<br>• Basis data vektor ChromaDB dan database relasional sistem perpustakaan.<br>• Antarmuka web Gradio multi-turn dan protokol komunikasi FastMCP (JSON-RPC). |
| **Actuators**<br>*(Aktuator)* | • Menampilkan kartu rekomendasi buku/jurnal lengkap dengan skor relevansi.<br>• Menampilkan panel sitasi dan kutipan rujukan faktual (*Grounding Citations Panel*).<br>• Menampilkan jejak pemikiran agen (*Thought Trace Accordion*).<br>• Mengirimkan perintah eksekusi alat bisnis ke server FastMCP. |
| **Sensors**<br>*(Sensor)* | • Masukan teks pengguna (potongan judul, tema, alur cerita, konteks kejadian).<br>• Riwayat sesi percakapan multi-turn pengguna.<br>• Tanggapan dan kode status dari server alat FastMCP.<br>• Nilai kemiripan kosinus dari basis data vektor ChromaDB. |

### Klasifikasi 6 Dimensi Lingkungan Operasional:
1. **Partially Observable**: Masukan pengguna bersifat parsial/samar; membutuhkan inferensi semantik.
2. **Single-Agent**: MnemoLib berperan sebagai satu entitas cerdas terpusat dalam penalaran.
3. **Stochastic**: Kueri bersifat non-deterministik dan multitafsir; diatasi dengan *guardrails*.
4. **Sequential**: Setiap aksi inferensi bergantung pada status kognitif langkah sebelumnya.
5. **Dynamic**: Koleksi dokumen dan status ketersediaan buku dapat berubah sewaktu-waktu.
6. **Discrete**: Ruang keadaan, aksi, entitas token kata, dan metadata buku bersifat diskrit.

> Rincian lengkap tersedia pada: [`docs/milestone-01/peas.md`](docs/milestone-01/peas.md).

---

## 4. Arsitektur Sistem 5-Lapis (Enterprise AI Copilot)

Purwarupa MnemoLib dibangun di atas arsitektur modular 5-lapis terstandarisasi:

```mermaid
flowchart TD
    subgraph Layer1["1. Data & Document Layer"]
        D1[Koleksi Buku & Jurnal PDF/TXT] --> D2[Text Cleaner & OpenCV OCR]
    end

    subgraph Layer2["2. Knowledge & RAG Layer"]
        D2 --> K1[Word-aware Chunking with Overlap]
        K1 --> K2[Sentence-Transformers Embeddings]
        K2 --> K3[(ChromaDB Persistent Store)]
    end

    subgraph Layer3["3. Agent & Tool Layer"]
        USER[Input Pengguna: Potongan Ingatan] --> R1[ReAct Reasoning Loop]
        R1 <--> G1[Google Gemini 2.5 Flash via GenAI SDK]
        R1 <--> M1[FastMCP Business Tool Server / JSON-RPC]
        K3 <--> M1
    end

    subgraph Layer4["4. Interface Layer"]
        R1 --> UI1[Gradio Interactive Web UI]
        UI1 --> UI2[Thought Trace Accordion]
        UI1 --> UI3[Grounding Citations Panel]
    end

    subgraph Layer5["5. Observability & Guardrails Layer"]
        SEC1[Strict Delimiter: <<<USER_INPUT>>>] --> R1
        R1 --> SEC2[Relevance Threshold Guardrail: tau >= 0.70]
        R1 --> OBS1[Tracing Log & LLM-as-a-Judge Evaluation]
    end
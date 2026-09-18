# MnemoLib

## Sistem Katalog Perpustakaan Cerdas Berbasis Contextual Match & Semantic Search untuk Identifikasi Buku dan Jurnal Melalui Potongan Ingatan Pengguna

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![Manajer Paket](https://img.shields.io/badge/Manajer%20Paket-Astral%20uv-purple.svg)](https://github.com/astral-sh/uv)
[![Pengujian](https://img.shields.io/badge/Pengujian-pytest-yellow.svg)](https://pytest.org)
[![Lisensi](https://img.shields.io/badge/Lisensi-MIT-green.svg)](LICENSE)
[![Kampus](https://img.shields.io/badge/Kampus-Institut%20Teknologi%20Del-004B87.svg)](https://www.del.ac.id/)

---

## 1. Latar Belakang

MnemoLib merupakan sistem katalog perpustakaan cerdas berbasis Artificial Intelligence yang membantu civitas akademika **Institut Teknologi Del (IT Del)** menemukan buku atau jurnal berdasarkan potongan ingatan.

Pengguna sering kali hanya mengingat sebagian informasi seperti:
- potongan judul
- karakter cerita
- topik buku
- konteks kejadian
- kata kunci tertentu

Berbeda dengan pencarian katalog konvensional yang membutuhkan keyword lengkap, MnemoLib dirancang untuk memahami informasi parsial pengguna.

---

## 2. Anggota Kelompok

| Nama | GitHub | Peran di Tim (PjBL Role) |
|---|---|---|
| Laura Sirumapea | @LauraSirumapea | **AI Architect & Model Lead** |
| Desnita Pardosi | @DesnitaPardosi | **Data & Knowledge Engineer** |
| Mia Sibuea | @MiaSibuea | **Integration & Interface Engineer** |

---

## 3. Problem Statement

Masalah utama:
1. Pengguna sulit menemukan buku ketika hanya mengingat sebagian informasi.
2. Sistem pencarian biasa membutuhkan keyword yang spesifik dan kaku.
3. Informasi berupa cerita atau konteks sulit digunakan dalam pencarian tradisional.
4. Dibutuhkan sistem yang mampu mencari berdasarkan kemiripan makna informasi dengan waktu respon cepat.

---

## 4. Spesifikasi Formal PEAS

| Komponen PEAS | Rincian Terukur & Spesifikasi |
|---|---|
| **Performance Measure** | • **Search Accuracy ($\ge 85\%$):** Kemampuan sistem menemukan buku atau jurnal yang sesuai dengan ingatan pengguna.<br><br>• **Result Relevance:** Tingkat kecocokan hasil pencarian dengan informasi yang diberikan pengguna.<br><br>• **Response Time ($< 1,5$ detik):** Kecepatan sistem dalam menghasilkan rekomendasi koleksi.<br><br>• **Search Traversal Latency ($\le 50\text{ ms}$):** Waktu komputasi algoritma UCS dalam menentukan rute keputusan.<br><br>• **User Satisfaction:** Kemudahan pengguna menemukan koleksi tanpa harus bertanya manual ke pustakawan. |
| **Environment** | Lingkungan Perpustakaan IT Del: koleksi buku teks, laporan tugas akhir, metadata koleksi (judul, penulis, kategori, tahun terbit, sinopsis), database perpustakaan, serta informasi parsial yang diberikan pengguna. |
| **Actuators** | Menampilkan hasil pencarian buku/jurnal, memberikan rekomendasi koleksi, menampilkan nomor rak dan metadata buku, serta mengurutkan kandidat hasil pencarian berdasarkan relevansi. |
| **Sensors** | Input teks pengguna berupa potongan judul, deskripsi cerita, karakter, lokasi kejadian, topik pembahasan, kata kunci, dan informasi lain yang diingat pengguna. |

### Klasifikasi Sifat Lingkungan (6 Dimensi Russell & Norvig)

1. **Partially Observable**  
   Sistem tidak memperoleh informasi lengkap mengenai buku yang dicari karena pengguna hanya memberikan potongan ingatan yang belum utuh.

2. **Single Agent**  
   MnemoLib berperan sebagai satu intelligent agent mandiri yang melakukan proses pencarian dan rekomendasi buku.

3. **Stochastic**  
   Hasil pencarian memiliki kemungkinan berbeda karena informasi yang diberikan pengguna dapat bersifat subjektif dan tidak lengkap.

4. **Sequential**  
   Proses pencarian dilakukan melalui beberapa tahap berurutan hingga menghasilkan rekomendasi buku yang sesuai.

5. **Dynamic**  
   Data koleksi perpustakaan dapat berubah apabila terdapat penambahan, peminjaman, atau pembaruan buku/jurnal.

6. **Discrete**  
   Informasi koleksi buku, metadata, status pencarian, dan hasil pencarian direpresentasikan dalam bentuk data diskrit.

---

## 5. Diagram Arsitektur Sistem

```mermaid
flowchart TD
    subgraph SENSORS["1. Masukan (Sensors)"]
        S1["Kueri Pengguna: Potongan Ingatan / Konteks"]
        S2["Katalog Buku & Metadata Perpustakaan IT Del"]
    end

    subgraph ENGINE["2. Mesin Pencari MnemoLib"]
        E1["Validasi Kueri & Ekstraksi Makna"]
        E2["Formulasi Ruang Keadaan (X, A, T, G, C)"]
        E3["Pencarian Jalur Optimal UCS (heapq)"]
        
        S1 --> E1
        S2 --> E2
        E1 --> E2
        E2 --> E3
    end

    subgraph ACTUATORS["3. Keluaran (Actuators)"]
        A1["Rekomendasi Judul Buku / Jurnal"]
        A2["Informasi Nomor Rak di Perpustakaan IT Del"]
        A3["Sinopsis Singkat & Alasan Rekomendasi"]
        
        E3 --> A1
        E3 --> A2
        E3 --> A3
    end

---

## 6. Formulasi Ruang Keadaan Formal $(X, A, T, G, C)$

Proses pencarian keputusan pada sistem MnemoLib diformulasikan ke dalam 5 elemen formal:

- **$X$ (State Space / Kumpulan Status):**
  - `start`: Memulai sesi pencarian.
  - `query_received`: Kueri ingatan dari pengguna diterima sistem.
  - `identify_title_author`: Sistem mengecek apakah ada potongan judul atau penulis.
  - `extract_context`: Sistem membedah cerita atau topik buku yang diingat.
  - `identify_story_elements`: Sistem mengidentifikasi tokoh, latar, atau alur cerita.
  - `apply_filters`: Sistem menyaring berdasarkan kategori atau tahun terbit.
  - `catalog_lookup`: Sistem mencari kecocokan ke database katalog perpustakaan.
  - `results_presented` *(Goal)*: Buku berhasil ditemukan dan ditampilkan ke layar.

- **$A$ (Actions / Himpunan Aksi):**
  - Menerima kueri, ekstrak judul, ekstrak konteks cerita, pasang filter kategori, cari ke katalog, dan sajikan hasil.

- **$T$ (Transition Model / Perubahan Status):**
  - Model perpindahan status setelah tindakan dijalankan: $T(s, a) \to s'$.

- **$G$ (Goal Test / Syarat Berhasil):**
  - Pencarian dinyatakan selesai jika mencapai status `results_presented` dan menemukan minimal 1 buku yang relevan.

- **$C$ (Step Cost / Waktu Proses Nyata dalam Milidetik):**
  - `start` $\to$ `query_received`: `5 ms` (Terima masukan teks)
  - `query_received` $\to$ `identify_title_author`: `20 ms` (Pengecekan judul)
  - `query_received` $\to$ `apply_filters`: `15 ms` (Filter kategori/tahun)
  - `query_received` $\to$ `extract_context`: `45 ms` (Ekstraksi konteks cerita)
  - `identify_title_author` $\to$ `catalog_lookup`: `30 ms` (Cari indeks judul)
  - `extract_context` $\to$ `identify_story_elements`: `20 ms` (Identifikasi tokoh/plot)
  - `identify_story_elements` $\to$ `catalog_lookup`: `50 ms` (Pencarian semantik)
  - `apply_filters` $\to$ `catalog_lookup`: `40 ms` (Pencarian katalog terfilter)
  - `catalog_lookup` $\to$ `results_presented`: `10 ms` (Penyajian hasil)

---

## 7. Uniform Cost Search Baseline

Pada Milestone 01, MnemoLib menggunakan Uniform Cost Search (UCS) sebagai algoritma baseline untuk menentukan alur keputusan pemrosesan dengan total estimasi waktu proses (latensi milidetik) terendah.

Implementasi:
```text
src/mnemolib/search/
├── ucs.py
└── mnemolib_graph.py

---

## 8. Repository Structure

Berikut struktur repository MnemoLib:

```text
mnemolib/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── uv.lock
│
├── docs/
│   └── milestone-01/
│       ├── problem-framing.md
│       ├── peas.md
│       └── state-space.md
│
├── src/
│   └── mnemolib/
│       ├── __init__.py
│       └── search/
│           ├── __init__.py
│           ├── ucs.py
│           └── mnemolib_graph.py
│
└── tests/
    └── test_ucs.py

---

## 9. Panduan Menjalankan Program (Astral uv)
# 1. Kloning repositori
git clone https://github.com/LauraSirumapea/mnemolib.git
cd mnemolib

# 2. Pasang dependensi
uv sync

# 3. Jalankan pengujian otomatis
uv run pytest -v

# 4. Jalankan program demo
uv run mnemolib

---
10. Lisensi

Proyek ini menggunakan lisensi 
MIT License
.
Hak Cipta (c) 2026 Institut Teknologi Del - Program Studi Sarjana Sistem Informasi.
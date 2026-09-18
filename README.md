# MnemoLib
### Asisten Cerdas Perpustakaan Kampus Institut Teknologi Del Berbasis Potongan Ingatan Pengguna

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![Manajer Paket](https://img.shields.io/badge/Manajer%20Paket-Astral%20uv-purple.svg)](https://github.com/astral-sh/uv)
[![Pengujian](https://img.shields.io/badge/Pengujian-pytest-yellow.svg)](https://pytest.org)
[![Lisensi](https://img.shields.io/badge/Lisensi-MIT-green.svg)](LICENSE)
[![Kampus](https://img.shields.io/badge/Kampus-Institut%20Teknologi%20Del-004B87.svg)](https://www.del.ac.id/)

---

## 1. Latar Belakang & Profil Organisasi Mitra

**Institut Teknologi Del (IT Del)** di Sitoluama, Laguboti, adalah kampus asrama (*boarding campus*) dengan prinsip hidup **"MarTuhan, Marroha, Marbisuk"**. Mahasiswa IT Del menjalani kegiatan harian yang padat:

- **08.00 - 17.00**: Perkuliahan teori, responsi, dan praktikum laboratorium di Gedung 5 (GD5), Gedung 7 (GD7), dan Gedung 9 (GD9).
- **12.00 - 13.00**: Makan siang bersama seluruh civitas akademika.
- **19.30 - 22.00**: Belajar mandiri wajib di asrama (*study time*).

Untuk mengerjakan tugas kuliah dan Proyek Akhir (PA/TA), mahasiswa sangat membutuhkan referensi dari **Perpustakaan IT Del**. Perpustakaan ini mengelola ribuan buku fisik, laporan tugas akhir mahasiswa terdahulu, dan langganan jurnal ilmiah digital.

---

## 2. Masalah Nyata di Lapangan (*Pain Points*) & Justifikasi AI

Dalam praktiknya, mahasiswa sering kesulitan mencari buku:

1. **Lupa Judul Persis:** Mahasiswa sering kali hanya mengingat isi cerita, topik bahasan, atau ciri fisik buku (misalnya: *"buku AI warna biru yang bahas graf"* atau *"tugas akhir tentang sensor pertanian kopi"*), tetapi lupa judul dan nama penulisnya.

2. **Katalog Perpustakaan (OPAC) Masih Kaku:** Sistem pencari komputer katalog yang ada saat ini hanya mencocokkan kata yang sama persis. Kurang satu huruf atau beda susunan kata saja, hasilnya langsung **kosong (0 hasil)**.

3. **Antrean di Meja Petugas:** Karena gagal mencari di komputer, mahasiswa bertanya manual ke petugas perpustakaan, memakan waktu wawancara 10–15 menit per orang.

### Mengapa Harus Solusi AI?

Pencarian basis data biasa (SQL) tidak bisa memahami makna kata yang mirip. Solusi AI **MnemoLib** memadukan:

- **Pencarian Graf Cerdas (Uniform Cost Search):** Menentukan urutan langkah pemrosesan yang paling hemat waktu (latensi tercepat).
- **Pencarian Makna (Semantic Search):** Menghubungkan kata-kata ingatan mahasiswa dengan isi buku di perpustakaan meskipun pilihan katanya berbeda.

---

## 3. Spesifikasi Formal PEAS

| Bagian PEAS | Penjelasan & Ukuran Nyata |
|---|---|
| **Ukuran Kinerja (Performance Measure)** | • **Akurasi Pencarian ($\ge 85%$):** Buku yang disarankan benar-benar sesuai dengan yang dicari mahasiswa.<br>• **Waktu Respon Cepat ($< 1,5$ detik):** Hasil pencarian muncul tanpa membuat pengguna menunggu lama.<br>• **Waktu Hitung Rute ($\le 50\text{ ms}$):** Menemukan alur langkah pemrosesan terbaik dalam hitungan milidetik.<br>• **Penolakan Sopan:** Menolak dengan ramah jika pertanyaan tidak ada hubungannya dengan perpustakaan. |
| **Lingkungan Kerja (Environment)** | Kampus IT Del: katalog buku teks, laporan tugas akhir mahasiswa, jurnal ilmiah, dan web pencarian. |
| **Alat Bertindak (Actuators)** | Menampilkan kartu buku rekomendasi, nomor rak buku di perpustakaan, cuplikan isi buku, dan status ketersediaan. |
| **Alat Penerima Masukan (Sensors)** | Kolom ketik pengguna (potongan judul, topik cerita, kata kunci acak, atau perkiraan tahun). |

### 6 Sifat Lingkungan Sistem (Russell & Norvig)

1. **Dapat Diamati Sebagian (Partially Observable):** Sistem tidak langsung tahu buku apa yang dicari karena masukan mahasiswa hanya berupa potongan ingatan yang belum lengkap.
2. **Agen Tunggal (Single-Agent):** Sistem MnemoLib bekerja sendiri untuk mencari buku terbaik bagi pengguna.
3. **Mengandung Ketidakpastian (Stochastic):** Ingatan mahasiswa bisa saja samar atau bermakna ganda.
4. **Berurutan (Sequential):** Langkah pencarian awal menentukan langkah pencarian berikutnya.
5. **Dinamis (Dynamic):** Status buku di perpustakaan bisa berubah sewaktu-waktu saat dipinjam atau dikembalikan mahasiswa lain.
6. **Diskrit (Discrete):** Status pencarian, daftar buku, dan aksi yang dilakukan sistem terbagi dalam langkah-langkah yang jelas.

---

## 4. Diagram Arsitektur Cara Kerja Sistem

```mermaid
flowchart TD
    subgraph MASUKAN["1. Masukan Sistem (Sensors)"]
        S1["Kueri Pengguna: Potongan Ingatan / Topik / Cerita"]
        S2["Daftar Buku & Tugas Akhir Perpustakaan IT Del"]
        S3["Riwayat Pertanyaan Sebelumnya"]
    end

    subgraph MESIN["2. Mesin Pencari MnemoLib"]
        E1["Pemisahan Kata & Makna Kueri"]
        E2["Penyusunan Ruang Keadaan (X, A, T, G, C)"]
        E3["Pencarian Jalur Tercepat (Algoritma UCS)"]
        E4["Penyaringan Relevansi (Batas Kecocokan)"]

        S1 --> E1
        S2 --> E2
        S3 --> E1
        E1 --> E2
        E2 --> E3
        E3 --> E4
    end

    subgraph KELUARAN["3. Keluaran Sistem (Actuators)"]
        A1["Rekomendasi Judul Buku / Jurnal"]
        A2["Nomor Rak Buku di Perpustakaan IT Del"]
        A3["Alasan & Ringkasan Kenapa Buku Ini Cocok"]
        A4["Tahapan Berpikir Sistem"]

        E4 --> A1
        E4 --> A2
        E4 --> A3
        E4 --> A4
    end
---

## 5. Formulasi Ruang Keadaan Formal `(X,A,T,G,C)` & Baseline Search (UCS)

Sistem pencarian jalur keputusan pada MnemoLib dimodelkan ke dalam 5 elemen:

- **`X`** **(Kumpulan Status / Ruang Keadaan):**
  - `start`: Memulai pencarian.
  - `query_received`: Ingatan pengguna diterima sistem.
  - `extract_semantic_memory`: Sistem membedah cerita atau topik yang diingat.
  - `apply_faceted_filter`: Sistem menyaring kategori atau tahun buku.
  - `identify_exact_title`: Pengecekan kata yang mirip judul buku.
  - `vector_semantic_search`: Mencari ke basis data berdasarkan kesamaan makna cerita.
  - `catalog_db_lookup`: Mencari langsung ke daftar judul buku perpustakaan.
  - `relevance_scoring`: Menilai seberapa cocok buku yang ditemukan.
  - `results_presented` *(Tujuan Selesai)*: Buku yang cocok berhasil ditampilkan ke layar.

- **`A`** **(Daftar Tindakan / Aksi):**
  - Pisahkan kata ingatan, saring kategori, cari ke basis data, hitung kecocokan, dan tampilkan hasil.

- **`T`** **(Perubahan Status):**
  - Perpindahan dari satu status ke status berikutnya setelah tindakan dijalankan.

- **`G`** **(Syarat Berhasil / Tujuan):**
  - Pencarian dianggap berhasil jika buku ditemukan dengan tingkat kecocokan minimal 70% (`τ≥0,70`).

- **`C`** **(Biaya / Waktu Langkah):**
  - Menerima masukan: `5 ms`
  - Saring kategori buku: `15 ms`
  - Cek potongan judul: `20 ms`
  - Bedah makna ingatan: `45 ms`
  - Cari ke database katalog: `30 ms`
  - Cari kemiripan makna cerita: `80 ms`
  - Urutkan dan siapkan tampilan: `20 ms`

### Algoritma Pencarian Baseline (UCS)

MnemoLib menggunakan algoritma **Uniform Cost Search (UCS)** untuk memilih langkah pemrosesan yang paling cepat (total waktu milidetik paling kecil).

- Berkas kode: **`src/mnemolib/search/ucs.py`** *(menggunakan antrean prioritas `heapq`)*
- Graf alur keputusan: **`src/mnemolib/search/mnemolib_graph.py`**

============================================================
MnemoLib - Asisten Pintar Perpustakaan Kampus IT Del
Tugas 1: Pencarian Jalur Keputusan Optimal (UCS)

[+] Menyiapkan Ruang Keadaan Pencarian...
[+] Total Status: 9 simpul

[+] Menjalankan Algoritma Uniform Cost Search:
- Titik Mulai : start
- Titik Tujuan: results_presented

[V] Jalur Paling Cepat Berhasil Ditemukan!
- Total Waktu Proses: 75.00 ms
- Urutan Langkah:
1. start
2. query_received
3. identify_exact_title
4. catalog_db_lookup
5. relevance_scoring
6. results_presented

============================================================

---

## Struktur Folder

mnemolib/
├── LICENSE # Lisensi perangkat lunak terbuka (MIT)
├── README.md # Dokumen panduan utama proyek
├── pyproject.toml # Pengaturan proyek Python dan uv
├── uv.lock # Berkas pengunci versi paket
├── docs/
│ └── milestone-01/
│ ├── problem-framing.md # Cerita lengkap masalah perpustakaan IT Del
│ ├── peas.md # Rincian tabel PEAS & 6 sifat lingkungan
│ ├── state-space.md # Penjelasan rumus (X, A, T, G, C)
│ └── laporan_tugas01.md # Draf laporan untuk dikumpul ke ECourse Del
├── src/
│ └── mnemolib/
│ ├── init.py # Program utama (CLI Demo)
│ └── search/
│ ├── mnemolib_graph.py # Model graf pilihan rute keputusan
│ └── ucs.py # Logika algoritma pencarian UCS
└── tests/
└── test_ucs.py # Uji coba otomatis pytest (7 skenario uji)
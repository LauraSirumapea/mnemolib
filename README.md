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

    
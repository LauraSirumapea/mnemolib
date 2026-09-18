# MnemoLib

## Sistem Katalog Perpustakaan Cerdas Berbasis Contextual Match & Semantic Search untuk Identifikasi Buku dan Jurnal Melalui Potongan Ingatan Pengguna


## 1. Latar Belakang

MnemoLib merupakan sistem katalog perpustakaan cerdas berbasis Artificial Intelligence yang membantu pengguna menemukan buku atau jurnal berdasarkan potongan ingatan.

Pengguna sering kali hanya mengingat sebagian informasi seperti:

- potongan judul
- karakter cerita
- topik buku
- konteks kejadian
- kata kunci tertentu

Berbeda dengan pencarian katalog konvensional yang membutuhkan keyword lengkap, MnemoLib dirancang untuk memahami informasi parsial pengguna.


---

# 2. Anggota Kelompok

| Nama | GitHub |
|---|---|
| Laura Sirumapea | @LauraSirumapea |
| Desnita Pardosi | @DesnitaPardosi |
| Mia Sibuea | @MiaSibuea |


---

# 3. Problem Statement

Masalah utama:

1. Pengguna sulit menemukan buku ketika hanya mengingat sebagian informasi.
2. Sistem pencarian biasa membutuhkan keyword yang spesifik.
3. Informasi berupa cerita atau konteks sulit digunakan dalam pencarian tradisional.
4. Dibutuhkan sistem yang mampu mencari berdasarkan kemiripan informasi.


---

# 4. Spesifikasi Formal PEAS

| Komponen PEAS | Rincian Terukur & Spesifikasi |
|---|---|
| **Performance Measure** | • **Search Accuracy:** Kemampuan sistem menemukan buku atau jurnal yang sesuai dengan ingatan pengguna.<br><br>• **Result Relevance:** Tingkat kecocokan hasil pencarian dengan informasi yang diberikan pengguna.<br><br>• **Response Time:** Kecepatan sistem dalam menghasilkan rekomendasi koleksi.<br><br>• **Retrieval Success Rate:** Persentase keberhasilan sistem menemukan koleksi yang dicari pengguna.<br><br>• **User Satisfaction:** Tingkat kepuasan pengguna terhadap hasil pencarian yang diberikan sistem. |
| **Environment** | Koleksi buku dan jurnal perpustakaan, metadata koleksi (judul, penulis, kategori, tahun terbit, sinopsis), database perpustakaan, serta informasi parsial yang diberikan pengguna. |
| **Actuators** | Menampilkan hasil pencarian buku/jurnal, memberikan rekomendasi koleksi, menampilkan metadata buku, dan mengurutkan kandidat hasil pencarian berdasarkan relevansi. |
| **Sensors** | Input teks pengguna berupa potongan judul, deskripsi cerita, karakter, lokasi kejadian, topik pembahasan, kata kunci, dan informasi lain yang diingat pengguna. |


## Klasifikasi Sifat Lingkungan (6 Dimensi Russell & Norvig)

1. **Partially Observable**  
   Sistem tidak memperoleh informasi lengkap mengenai buku yang dicari karena pengguna hanya memberikan potongan ingatan.

2. **Single Agent**  
   MnemoLib berperan sebagai satu intelligent agent yang melakukan proses pencarian dan rekomendasi buku.

3. **Stochastic**  
   Hasil pencarian memiliki kemungkinan berbeda karena informasi yang diberikan pengguna dapat bersifat subjektif dan tidak lengkap.

4. **Sequential**  
   Proses pencarian dilakukan melalui beberapa tahap hingga menghasilkan rekomendasi buku yang sesuai.

5. **Dynamic**  
   Data koleksi perpustakaan dapat berubah apabila terdapat penambahan atau pembaruan buku/jurnal.

6. **Discrete**  
   Informasi koleksi buku, metadata, dan hasil pencarian direpresentasikan dalam bentuk data diskrit.
---

# 6. Uniform Cost Search Baseline

Pada Milestone 01, MnemoLib menggunakan Uniform Cost Search (UCS) sebagai algoritma baseline.

UCS melakukan eksplorasi berdasarkan cost terkecil sehingga dapat menemukan solusi dengan biaya minimum.


Implementasi:

Implementasi algoritma Uniform Cost Search tersedia pada:

```
src/mnemolib/search/

├── ucs.py
└── mnemolib_graph.py
```

File `ucs.py` berisi implementasi algoritma Uniform Cost Search (UCS) untuk melakukan eksplorasi state berdasarkan nilai cost terkecil.

File `mnemolib_graph.py` digunakan untuk merepresentasikan graph pencarian yang berisi node, state, dan hubungan antar kandidat buku.

Pengujian implementasi dilakukan menggunakan pytest.

Perintah menjalankan testing:

```
uv run pytest
```

Hasil pengujian:

```
3 passed
```

# 7. Repository Structure
 Berikut struktur repository MnemoLib:

```
mnemolib/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── uv.lock
│
├── docs/
│   └── milestone-01/
│       ├── peas.md
│       └── state-space.md
│
├── src/
│   └── mnemolib/
│       ├── __init__.py
│       └── search/
│           ├── ucs.py
│           └── mnemolib_graph.py
│
└── tests/
    └── test_ucs.py
```
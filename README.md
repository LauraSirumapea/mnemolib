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
| **Performance Measure** | • **Search Accuracy:** Kemampuan sistem menemukan buku/jurnal yang sesuai dengan informasi pengguna.<br><br>• **Relevance Score:** Tingkat kecocokan hasil pencarian berdasarkan informasi yang diberikan pengguna.<br><br>• **Response Time:** Waktu yang dibutuhkan sistem untuk menghasilkan kandidat buku.<br><br>• **Retrieval Success Rate:** Persentase keberhasilan menemukan koleksi yang sesuai.<br><br>• **Search Cost Minimization:** Meminimalkan biaya eksplorasi state pada proses pencarian. |
| **Environment** | Koleksi buku dan jurnal perpustakaan, metadata buku (judul, penulis, kategori, tahun, sinopsis), database koleksi, serta input berupa potongan ingatan pengguna. |
| **Actuators** | Output hasil pencarian buku/jurnal, ranking kandidat berdasarkan relevansi, rekomendasi koleksi, serta informasi metadata buku kepada pengguna. |
| **Sensors** | Teks masukan pengguna berupa deskripsi buku, potongan cerita, karakter, lokasi, topik pembahasan, kata kunci, dan informasi metadata tambahan. |


## Klasifikasi Sifat Lingkungan (6 Dimensi Russell & Norvig)

1. **Partially Observable**  
   Sistem tidak mendapatkan informasi lengkap mengenai buku yang dicari karena pengguna hanya memberikan potongan ingatan atau informasi parsial.

2. **Single Agent**  
   MnemoLib bekerja sebagai satu intelligent agent yang melakukan proses pencarian dan rekomendasi buku.

3. **Stochastic**  
   Hasil pencarian dapat memiliki ketidakpastian karena input pengguna bersifat subjektif dan dapat menghasilkan beberapa kandidat buku.

4. **Sequential**  
   Setiap proses eksplorasi kandidat buku memengaruhi langkah pencarian berikutnya.

5. **Dynamic**  
   Koleksi buku dan informasi perpustakaan dapat berubah ketika terdapat penambahan atau pembaruan data.

6. **Discrete**  
   State pencarian direpresentasikan dalam bentuk kandidat buku, metadata, dan hubungan antar node yang bersifat diskrit.

---

# 5. State Space Formulation (X,A,T,G,C)

## X — State Space

State merepresentasikan kandidat buku yang sedang dievaluasi.

Contoh:

`State = {book_id, metadata, relevance_score}`


## A — Actions

Action merupakan aksi perpindahan antar kandidat buku.

Contoh:

`A(s) = memilih kandidat buku berikutnya`


## T — Transition Model

Transition menjelaskan perubahan state akibat suatu aksi.

`T(s,a)=s'`


## G — Goal Test

Goal tercapai ketika kandidat buku sesuai dengan informasi pengguna.

`G(s)=True`


## C — Path Cost

Cost pencarian berdasarkan:

- jumlah node yang dieksplorasi
- perbedaan metadata
- ketidaksesuaian kandidat


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
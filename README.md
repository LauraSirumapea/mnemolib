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

# 4. PEAS Specification

## Performance Measure (P)

| Parameter | Deskripsi |
|-|-|
| Search Accuracy | Kemampuan menemukan koleksi yang sesuai |
| Result Relevance | Tingkat relevansi hasil pencarian |
| Response Time | Kecepatan memberikan hasil |
| Retrieval Success Rate | Keberhasilan menemukan buku target |
| User Satisfaction | Kepuasan pengguna |


## Environment (E)

| Komponen | Deskripsi |
|-|-|
| Library Catalog | Database buku dan jurnal |
| Book Metadata | Judul, penulis, tahun, kategori |
| User Input | Informasi berdasarkan ingatan pengguna |
| Collection Database | Koleksi perpustakaan |


## Actuators (A)

| Actuator | Fungsi |
|-|-|
| Display Results | Menampilkan kandidat buku |
| Show Metadata | Menampilkan detail buku |
| Rank Results | Mengurutkan kandidat |
| Recommendation | Memberikan rekomendasi |


## Sensors (S)

| Sensor | Contoh |
|-|-|
| Text Query | Deskripsi buku |
| Keywords | Kata kunci |
| Story Elements | Karakter, tema, lokasi |
| Metadata Filter | Tahun dan kategori |


## Environment Classification

| Property | Classification |
|-|-|
| Observability | Partially Observable |
| Deterministic | Stochastic |
| Sequential | Sequential |
| Dynamic | Dynamic |
| Discrete | Discrete |
| Agents | Single Agent |


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

# Milestone 2 - CSP Solver Algorithm

## 1. Overview

Pada Milestone 1, MnemoLib menggunakan Uniform Cost Search (UCS) sebagai baseline algorithm untuk mencari kandidat buku atau jurnal berdasarkan biaya pencarian terendah.

Pada Milestone 2, sistem dikembangkan dengan menambahkan Constraint Satisfaction Problem (CSP) Solver. CSP digunakan untuk menyaring kandidat hasil pencarian berdasarkan batasan yang diberikan pengguna.

Alur pengembangan:

User Query
↓
UCS Search (Milestone 1)
↓
Candidate Documents
↓
CSP Solver (Milestone 2)
↓
Final Result


## 2. CSP Formulation

CSP terdiri dari:

- Variables
- Domains
- Constraints


### Variables

Variabel yang digunakan:

- document_type
  - jenis dokumen (Book/Journal)

- category
  - kategori dokumen

- language
  - bahasa dokumen

- publication_year
  - tahun publikasi

- candidate_book
  - kandidat dokumen yang akan dipilih


### Domains

Domain adalah kumpulan nilai yang mungkin dimiliki setiap variable.

Contoh:

document_type:
{Book, Journal}

category:
{AI, Programming, Database}

language:
{English, Indonesia}

publication_year:
{2019, 2020, 2021, 2022, 2023}


## 3. Constraint Checking

Constraint digunakan untuk membatasi solusi yang valid.

Contoh constraint:

- Jenis dokumen harus sesuai dengan permintaan pengguna.
- Kategori dokumen harus sesuai dengan topik pencarian.
- Bahasa harus sesuai dengan preferensi pengguna.
- Tahun publikasi harus memenuhi batas tahun yang diberikan.


## 4. Backtracking Search

Backtracking digunakan untuk mencari solusi dengan mencoba kombinasi nilai dari variable.

Proses:

1. Memilih variable yang belum memiliki nilai.
2. Memberikan kemungkinan nilai dari domain.
3. Mengecek apakah nilai memenuhi constraint.
4. Jika valid, pencarian dilanjutkan.
5. Jika tidak valid, sistem kembali ke pilihan sebelumnya.


## 5. AC-3 Constraint Propagation

AC-3 digunakan untuk mengurangi domain yang tidak mungkin sebelum proses pencarian dilakukan.

Tujuannya:

- Mengurangi ruang pencarian.
- Mempercepat proses backtracking.
- Mendeteksi kondisi tidak memiliki solusi lebih awal.


## 6. MRV Heuristic

Minimum Remaining Values (MRV) digunakan untuk memilih variable dengan jumlah kemungkinan nilai paling sedikit.

Dengan memilih variable yang paling terbatas terlebih dahulu, pencarian solusi menjadi lebih efisien.


## 7. Output Solver

CSP Solver menghasilkan:

- kandidat dokumen yang memenuhi constraint
- informasi apakah solusi ditemukan
- informasi performa pencarian
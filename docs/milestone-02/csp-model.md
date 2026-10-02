# Milestone 2 - CSP Model MnemoLib

## 1. Business Problem

MnemoLib merupakan sistem pencarian buku dan jurnal berdasarkan informasi yang diingat pengguna. Pada Milestone 1, sistem menggunakan Uniform Cost Search (UCS) untuk mencari kandidat berdasarkan biaya pencarian. Pada Milestone 2, sistem dikembangkan dengan Constraint Satisfaction Problem (CSP) untuk menyaring kandidat berdasarkan batasan pengguna.

## 2. Variables

Pada Constraint Satisfaction Problem (CSP), setiap variabel merepresentasikan komponen yang harus ditentukan nilainya agar sistem dapat menemukan kandidat buku atau jurnal yang sesuai dengan kebutuhan pengguna.

Variables yang digunakan:

1. document_type
   - Menentukan jenis dokumen yang dicari pengguna.
   - Contoh nilai: Book, Journal

2. category
   - Menentukan kategori atau topik dokumen.
   - Contoh nilai: AI, Programming, Database

3. language
   - Menentukan bahasa dokumen.
   - Contoh nilai: English, Indonesia

4. publication_year
   - Menentukan tahun publikasi dokumen.

5. candidate_book
   - Menentukan kandidat buku atau jurnal yang berasal dari hasil pencarian Milestone 1.

## 3. Domains

Domain merupakan kumpulan nilai yang mungkin dimiliki oleh setiap variabel.

Contoh domain:

document_type:
{Book, Journal}

category:
{AI, Programming, Database}

language:
{English, Indonesia}

publication_year:
{2019, 2020, 2021, 2022, 2023}

candidate_book:
{kandidat dokumen hasil pencarian UCS pada Milestone 1}

## 4. Constraints

Constraint digunakan untuk membatasi nilai yang diperbolehkan sehingga solusi yang dihasilkan sesuai dengan kebutuhan pengguna.

Constraint pada MnemoLib:

1. document_type harus sesuai dengan jenis dokumen yang diminta pengguna.

2. category harus sesuai dengan kategori/topik yang dicari.

3. language harus sesuai dengan preferensi bahasa pengguna.

4. publication_year harus memenuhi batas tahun yang diberikan pengguna.

5. candidate_book harus memiliki seluruh atribut yang memenuhi constraint lainnya.

## 5. Objective

Tujuan dari CSP Solver pada MnemoLib adalah menemukan kandidat buku atau jurnal yang memenuhi seluruh constraint pengguna sehingga hasil pencarian menjadi lebih relevan dibandingkan hanya menggunakan pencarian berdasarkan cost pada Milestone 1.
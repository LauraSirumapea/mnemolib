# Milestone 2 - CSP Solver Testing

## 1. Tujuan Testing

Testing dilakukan untuk memastikan CSP Solver MnemoLib dapat menemukan kandidat buku atau jurnal yang sesuai dengan constraint pengguna.

Pengujian dilakukan terhadap:

- validasi constraint
- pencarian solusi
- kondisi tidak memiliki solusi
- kondisi constraint konflik


## 2. Test Case


| No | Test Case | Input | Expected Result |
|---|---|---|---|
| 1 | Normal Case | Buku AI, English, tahun >= 2020 | Solusi ditemukan |
| 2 | No Solution | Buku AI tahun >= 2035 | Tidak ada solusi |
| 3 | Conflict Constraint | Tahun >=2025 dan <=2020 | Tidak ada solusi |
| 4 | Multiple Solution | Kategori AI dengan beberapa kandidat | Beberapa solusi ditemukan |


## 3. Validasi Solusi

Setiap solusi yang diberikan solver harus memenuhi seluruh constraint pengguna.

Contoh:

Jika constraint:

- category = AI
- year >= 2020

Maka seluruh hasil harus memiliki:

- kategori AI
- tahun publikasi minimal 2020


## 4. Hasil Testing

| Test | Status |
|---|---|
| Normal Case | - |
| No Solution | - |
| Conflict Constraint | - |
| Multiple Solution | - |
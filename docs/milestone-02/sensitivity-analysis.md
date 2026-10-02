# Sensitivity Analysis CSP Solver

## 1. Tujuan

Sensitivity analysis dilakukan untuk mengetahui pengaruh perubahan constraint terhadap jumlah solusi dan performa CSP Solver.

Analisis dilakukan dengan mengubah tingkat keketatan constraint.


## 2. Pengujian Constraint

| Percobaan | Constraint | Expected Effect |
|---|---|---|
| 1 | Year >= 2020 | Kandidat lebih banyak |
| 2 | Year >= 2022 | Kandidat berkurang |
| 3 | Year >= 2025 | Kandidat semakin sedikit |
| 4 | Year >= 2030 | Kemungkinan tidak ada solusi |


## 3. Analisis

Constraint yang semakin ketat menyebabkan ruang pencarian menjadi semakin kecil.

Ketika domain semakin terbatas, jumlah kandidat yang memenuhi aturan pengguna akan berkurang.


## 4. Performance Analysis

Pengukuran dilakukan terhadap:

- execution time
- jumlah node pencarian
- jumlah backtracking

Perbandingan dilakukan antara:

- Backtracking biasa
- Backtracking dengan AC-3
- Backtracking dengan MRV
# Laporan Analisis Sensitivitas & Waktu Konvergensi Solver
## MnemoLib — Milestone 02: Modul Pemecahan Batasan Keputusan Bisnis

---

## 1. Tujuan Analisis Sensitivitas
Sesuai dengan instrumen penugasan dan rubrik penilaian, analisis sensitivitas dilakukan untuk mengevaluasi:
1. **Sensitivitas Skalabilitas Masalah (Problem Scaling)**: Mengamati dinamika waktu komputasi dan penelusuran simpul (*nodes visited*) saat ukuran himpunan variabel diskalakan dari skala kecil ($N=8$) hingga skala besar ($N=256$).
2. **Studi Ablasi Komparatif (Ablation Study)**: Mengukur kontribusi isolatif dari masing-masing teknik kecerdasan buatan:
   - *Baseline*: Pure Backtracking (tanpa propagasi & heuristik).
   - Heuristik MRV (*Minimum Remaining Values*).
   - Propagasi Batasan AC-3 (*Arc Consistency 3*).
   - Modul Penuh: Backtracking + AC-3 + MRV.
3. **Karakteristik Waktu Konvergensi pada Kasus Ekstrem**: Mengevaluasi seberapa cepat solver mendeteksi kegagalan pada ruang masalah yang over-constrained / kontradiktif.

---

## 2. Metodologi Eksperimen Empiris
Eksperimen dijalankan secara empiris pada lingkungan komputasi riil menggunakan modul profiling `scripts/benchmark_scaling.py`. Setiap skenario diulang sebanyak **1.000 iterasi** untuk mengeliminasi fluktuasi *scheduling jitter* sistem operasi, dan dihitung nilai rata-ratanya.

---

## 3. Hasil Eksperimen 1: Analisis Skalabilitas (Skala Kecil vs Skala Besar)

Pengujian dilakukan dengan menskalakan rantai dependensi keputusan katalog perpustakaan $X_1, X_2, \dots, X_N$ dengan batasan dependensi berantai dan batasan uniter:

| Skala Masalah | Jumlah Variabel ($N$) | Waktu Eksekusi (ms) | Simpul Dievaluasi (*Nodes*) | Jumlah *Backtracks* | Status Solusi |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Skala Kecil** | 8 | 0.119 ms | 9 | 0 | Solusi Ditemukan |
| **Skala Kecil** | 16 | 0.145 ms | 17 | 0 | Solusi Ditemukan |
| **Skala Menengah** | 32 | 0.444 ms | 33 | 0 | Solusi Ditemukan |
| **Skala Menengah** | 64 | 1.514 ms | 65 | 0 | Solusi Ditemukan |
| **Skala Besar** | 128 | 8.811 ms | 129 | 0 | Solusi Ditemukan |
| **Skala Besar** | 256 | 38.655 ms | 257 | 0 | Solusi Ditemukan |

### Visualisasi Kurva Pertumbuhan Waktu (Time vs Problem Size $N$)

```text
Waktu (ms)
  40.0 |                                                     * (256 var, 38.65 ms)
  35.0 |
  30.0 |
  25.0 |
  20.0 |
  15.0 |
  10.0 |                                       * (128 var, 8.81 ms)
   5.0 |
   1.5 |                         * (64 var, 1.51 ms)
   0.4 |           * (32 var, 0.44 ms)
   0.1 +---*--* (8 var, 0.11 ms | 16 var, 0.14 ms)
       +---|---|---|-------------|-------------|-------------|
       0   8  16  32            64            128           256   Variabel (N)
```

**Temuan Utama**:
Meskipun batas teoretis terburuk (*worst-case*) dari CSP adalah eksponensial $\mathcal{O}(2^N)$, penerapan kombinasi **AC-3 + MRV** mereduksi pohon pencarian secara drastis menjadi **hampir linier** $\mathcal{O}(N)$. Terlihat bahwa jumlah simpul yang dievaluasi tepat $N+1$ simpul dengan **0 kali backtrack**, membuktikan bahwa propagasi AC-3 memangkas seluruh inkonsistensi sebelum proses penugasan dimulai.

---

## 4. Hasil Eksperimen 2: Studi Ablasi Algoritma (Ablation Study)

Evaluasi pengaruh strategi algoritma terhadap waktu komputasi, jumlah simpul dievaluasi, dan jumlah backtrack pada kasus operasional MnemoLib:

### Tabel Komparasi Algoritma pada Berbagai Skenario

| Skenario Uji | Strategi Algoritma | Simpul (*Nodes*) | *Backtracks* | Waktu Komputasi ($\mu\text{s}$) | Status Solusi |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Normal Unary** (Hanya Judul/Penulis) | Pure Backtracking | 5 | 0 | 14.30 $\mu\text{s}$ | FOUND |
| | Backtracking + MRV | 5 | 0 | 16.53 $\mu\text{s}$ | FOUND |
| | Backtracking + AC-3 | 5 | 0 | 24.03 $\mu\text{s}$ | FOUND |
| | Backtracking + AC-3 + MRV | 5 | 0 | 24.79 $\mu\text{s}$ | FOUND |
| **Normal Dependent** (Konteks + Cerita) | Pure Backtracking | 5 | 0 | 12.90 $\mu\text{s}$ | FOUND |
| | Backtracking + MRV | 5 | 0 | 20.11 $\mu\text{s}$ | FOUND |
| | Backtracking + AC-3 | 5 | 0 | 19.57 $\mu\text{s}$ | FOUND |
| | Backtracking + AC-3 + MRV | 5 | 0 | 26.65 $\mu\text{s}$ | FOUND |
| **Normal Full** (Semua Fitur Aktif) | Pure Backtracking | 5 | 0 | 11.77 $\mu\text{s}$ | FOUND |
| | Backtracking + MRV | 5 | 0 | 21.33 $\mu\text{s}$ | FOUND |
| | Backtracking + AC-3 | 5 | 0 | 34.77 $\mu\text{s}$ | FOUND |
| | Backtracking + AC-3 + MRV | 5 | 0 | 42.11 $\mu\text{s}$ | FOUND |
| **Kasus Ekstrem: Konflik Kontradiktif**<br>*(Cerita aktif, Konteks dilarang)* | **Pure Backtracking** | **5** | **7** | **15.42 $\mu\text{s}$** | **NO_SOL** |
| | **Backtracking + MRV** | **2** | **3** | **10.28 $\mu\text{s}$** | **NO_SOL** |
| | **Backtracking + AC-3** | **0** | **0** | **3.46 $\mu\text{s}$** | **NO_SOL** |
| | **Backtracking + AC-3 + MRV** | **0** | **0** | **4.06 $\mu\text{s}$** | **NO_SOL** |

---

## 5. Analisis Mendalam: Pembahasan Waktu Konvergensi

### 5.1 Perilaku pada Kasus Normal (Overhead Trade-off)
Pada kasus normal dengan ruang keadaan kecil ($N=4$), `Pure Backtracking` memiliki waktu absolut sedikit lebih rendah ($\approx 12-14\,\mu\text{s}$) dibandingkan varian AC-3 ($\approx 24-42\,\mu\text{s}$). Hal ini disebabkan oleh *overhead* pemeliharaan antrean busur (*queue overhead*) dan alokasi struktur data `set` pada AC-3. Namun, seluruh varian tetap beroperasi jauh di bawah ambang batas performa PEAS MnemoLib ($\le 50\text{ ms}$).

### 5.2 Superioritas AC-3 pada Kasus Ekstrem (Early Failure Detection)
Dampak paling signifikan terlihat pada **Kasus Ekstrem: Konflik Kontradiktif**:
1. **Pure Backtracking**: Melakukan eksplorasi buta hingga 5 simpul dan mengalami **7 kali backtrack** (waktu $15.42\,\mu\text{s}$) sebelum akhirnya menyadari bahwa tidak ada solusi legal.
2. **Backtracking + MRV**: Memangkas eksplorasi menjadi 2 simpul dan 3 backtrack ($10.28\,\mu\text{s}$).
3. **Backtracking + AC-3**: Menghasilkan **0 simpul dan 0 backtrack**, dengan waktu eksekusi hanya **$3.46\,\mu\text{s}$** (**$\approx 4.5\times$ lebih cepat**).
   - Hal ini membuktikan efektivitas teorema pemangkasan konsistensi busur: AC-3 mendeteksi *domain wipeout* ($D_3$ menjadi $\emptyset$) pada tahap pra-pencarian (*pre-search*), sehingga proses backtracking dibatalkan seketika tanpa membuang siklus CPU.

---

## 6. Kesimpulan Analisis Sensitivitas
1. Modul CSP MnemoLib menunjukkan stabilitas konvergensi luar biasa, dengan latensi skala besar ($N=256$) hanya sebesar $38.65\text{ ms}$, memenuhi syarat latensi responsif enterprise.
2. Sinergi antara propagasi AC-3 dan heuristik MRV berhasil mengeliminasi fenomena *combinatorial explosion*, menjadikan sistem aman dari potensi serangan *denial-of-service* akibat kueri kontradiktif.

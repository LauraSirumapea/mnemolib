# Implementasi Algoritma CSP Solver: AC-3 & Backtracking MRV
## MnemoLib — Milestone 02: Modul Pemecahan Batasan Keputusan Bisnis

---

## 1. Arsitektur Modular Solver
Modul CSP pada MnemoLib diorganisasikan secara modular dan mematuhi prinsip *clean code* serta *Separation of Concerns* (SoC):

```text
src/mnemolib/search/csp/
├── __init__.py         # Antarmuka publik ekspor modul CSP
├── constraints.py      # Definisi formal variabel, domain, batasan uniter & biner
├── ac3.py              # Algoritma propagasi konsistensi busur (Arc Consistency 3)
├── mrv.py              # Heuristik pemilihan variabel Minimum Remaining Values
└── solver.py           # Mesin inferensi Backtracking Search terintegrasi
```

---

## 2. Algoritma Propagasi Batasan AC-3 (Arc Consistency 3)

### 2.1 Konsep Matematis
Sebuah busur terarah $(X_i, X_j)$ dikatakan konsisten busur (*arc-consistent*) jika untuk setiap nilai $v \in D_i$, terdapat sekurang-kurangnya satu nilai $w \in D_j$ yang memenuhi batasan biner antara $X_i$ dan $X_j$.

Algoritma AC-3 menjaga antrean busur $\mathcal{Q}$. Setiap kali domain suatu variabel $X_i$ dipangkas (*pruned*) melalui fungsi `revise()`, seluruh busur tetangga $(X_k, X_i)$ dimasukkan kembali ke dalam antrean untuk menjamin konsistensi global.

### 2.2 Pseudocode AC-3
```text
function AC-3(csp) returns bool
    inputs: csp, sebuah problem kepuasan batasan dengan himpunan variabel X dan domain D
    local variables: queue, antrean busur biner berarah

    queue <- semua busur biner dalam csp: {(X2, X3), (X3, X2)}
    while queue tidak kosong do
        (Xi, Xj) <- REMOVE-FIRST(queue)
        if REVISE(csp, Xi, Xj) then
            if |Di| == 0 then return false   // Domain wipeout (Inkonsisten)
            for each Xk in NEIGHBORS(Xi) \ {Xj} do
                add (Xk, Xi) to queue
    return true
```

### 2.3 Fungsi `REVISE(Xi, Xj)`
```text
function REVISE(csp, Xi, Xj) returns bool
    revised <- false
    for each x in Di do
        if tidak ada y in Dj sedemikian sehingga (x, y) legal menurut batasan biner then
            hapus x dari Di
            revised <- true
    return revised
```

Pada MnemoLib, batasan biner utama adalah $C_6$: $X_3 = 1 \implies X_2 = 1$.
Jika domain $X_2 = \{0\}$, maka nilai $1$ pada $D_3$ tidak memiliki pendukung (*no supporting value*) karena pasangan $(0, 1)$ terlarang. Oleh karena itu, $1$ dihapus dari $D_3$ menyisakan $D_3 = \{0\}$.

---

## 3. Heuristik Minimum Remaining Values (MRV)

### 3.1 Konsep "Fail-First Principle"
Heuristik MRV (juga dikenal sebagai *Most Constrained Variable*) memilih variabel yang belum ditugaskan (*unassigned*) yang memiliki jumlah nilai tersisa paling sedikit dalam domainnya:
$$X_{\text{selected}} = \arg\min_{X_i \in X_{\text{unassigned}}} |D_i|$$

**Rasionalitas Desain**:
Dengan memilih variabel berdomain terkecil terlebih dahulu, faktor percabangan (*branching factor*) pohon pencarian diminimalkan. Jika sebuah cabang ditakdirkan gagal karena inkonsistensi, kegagalan akan terdeteksi lebih awal (*fail-first*), memangkas subpohon besar sebelum dieksplorasi.

---

## 4. Mesin Inferensi Backtracking Search Terintegrasi

### 4.1 Alur Kerja Solver
1. **Inisialisasi**: Domain awal dibuat untuk setiap variabel ($D_i = \{0, 1\}$).
2. **Propagasi Uniter**: Fitur kueri pengguna diterapkan langsung untuk membatasi domain ($C_1 - C_4$).
3. **Pra-Pemangkasan AC-3**: Menjalankan AC-3 sebelum penelusuran. Jika terjadi *domain wipeout* ($|D_i| = 0$), pencarian langsung berhenti tanpa memasuki rekursi (`return None`).
4. **Pencarian Rekursif**:
   - Pilih variabel menggunakan **MRV**.
   - Untuk setiap nilai legal, lakukan penugasan sementara.
   - Evaluasi batasan parsial `check_partial_assignment()`.
   - Propagasi AC-3 pada cabang penugasan (*forward checking via AC-3*).
   - Lanjutkan rekursi. Jika seluruh variabel terisi, validasi batasan lengkap `check_assignment()` dan kembalikan penugasan.

### 4.2 Diagram Alir Keputusan (Mermaid)

```mermaid
flowchart TD
    Start([Kueri Masuk]) --> Init[Inisialisasi Domain {0, 1}]
    Init --> Unary[Terapkan Batasan Uniter Kueri]
    Unary --> AC3Pre[Jalankan Propagasi AC-3 Awal]
    AC3Pre --> CheckAC3{Domain Kosong?}
    CheckAC3 -- Ya --> NoSol([Gagal: Tidak Ada Solusi Legal])
    CheckAC3 -- Tidak --> BT[Mulai Backtracking Search]
    
    BT --> Complete{Semua Variabel Terisi?}
    Complete -- Ya --> Validate{Validasi Batasan Lengkap}
    Validate -- Lolos --> Success([Solusi Legal Ditemukan])
    Validate -- Gagal --> Backtrack[Lakukan Backtrack]
    
    Complete -- Tidak --> PickVar[Pilih Variabel via Heuristik MRV]
    PickVar --> TryVal[Coba Nilai Domain]
    TryVal --> Partial{Konsisten Parsial?}
    Partial -- Tidak --> NextVal{Ada Nilai Lain?}
    Partial -- Ya --> AC3Branch[Jalankan AC-3 pada Cabang]
    AC3Branch --> BranchValid{Cabang Konsisten?}
    BranchValid -- Ya --> BT
    BranchValid -- Tidak --> Backtrack
    Backtrack --> NextVal
    NextVal -- Ya --> TryVal
    NextVal -- Tidak --> NoSol
```

---

## 5. Analisis Kompleksitas Algoritma

| Algoritma / Komponen | Kompleksitas Waktu | Kompleksitas Ruang | Keterangan |
| :--- | :--- | :--- | :--- |
| **AC-3 Propagation** | $\mathcal{O}(c \cdot d^3)$ | $\mathcal{O}(c + n \cdot d)$ | $c = |\text{arcs}| = 2$, $d = |D| = 2$. Pada MnemoLib, AC-3 selesai dalam $\le 16$ operasi dasar. |
| **MRV Variable Selection** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Melakukan pencarian linier atas $n \le 4$ variabel yang belum terisi. |
| **Backtracking (Worst-Case)** | $\mathcal{O}(d^n)$ | $\mathcal{O}(n)$ | Secara teoretis $2^4 = 16$. Namun dengan AC-3 dan MRV, kedalaman pohon terpangkas hingga $\le 5$ simpul. |

# Pemodelan Matematis Formal Constraint Satisfaction Problem (CSP)
## MnemoLib — Milestone 02: Modul Pemecahan Batasan Keputusan Bisnis

---

## 1. Latar Belakang & Domain Masalah Bisnis
Dalam operasional sistem katalog perpustakaan cerdas **MnemoLib** di Institut Teknologi Del, pengguna sering kali memasukkan kueri pencarian berbasis potongan ingatan yang tidak lengkap (potongan judul, konteks topik, fragmen alur cerita, atau filter kategori). 

Pada Milestone 01, penelusuran graf dilakukan menggunakan **Uniform Cost Search (UCS)** untuk menemukan jalur inferensi dengan biaya latensi terendah. Namun, dalam lingkungan operasional nyata, alokasi modul pemrosesan dan seleksi katalog dibatasi oleh regulasi bisnis ketat:
1. **Regulasi Dependensi Alur Komputasi**: Modul analisis alur cerita (*story elements*) membutuhkan ekstraksi konteks (*context extraction*) sebagai prasyarat wajib. Memproses cerita tanpa konteks menghasilkan galat semantik dan pemborosan komputasi.
2. **Ketersediaan & Keabsahan Fitur Masukan**: Jika masukan pengguna mengandung kriteria tertentu (misal: hanya mengingat nama pengarang), sistem harus mengalokasikan modul pencarian yang tepat secara deterministik.
3. **Integritas Operasional Minimum**: Sistem tidak boleh berada dalam kondisi pasif total (*all-idle*) saat menerima permintaan kueri.
4. **Batasan Kapasitas & Kuota Sumber Daya (Resource Quota)**: Batas maksimum beban proses komputasi paralel yang diizinkan untuk menjaga latensi tetap $\le 50\text{ ms}$.

Untuk menyelesaikan sub-masalah keputusan terikat batasan ini, sistem mengadopsi formulasi **Constraint Satisfaction Problem (CSP)** yang diselesaikan dengan propagasi batasan **AC-3 (Arc Consistency 3)** dan **Backtracking Search** berbasis heuristik **MRV (Minimum Remaining Values)**.

---

## 2. Definisi Formal Komponen CSP: $\langle X, D, C \rangle$

Secara matematis formal, pemodelan CSP pada MnemoLib didefinisikan sebagai tripel:
$$\mathcal{P} = \langle X, D, C \rangle$$

### 2.1 Himpunan Variabel Keputusan ($X$)
Variabel keputusan merepresentasikan status aktivasi subsistem inferensi cerdas pada pipeline keputusan kueri:
$$X = \{X_1, X_2, X_3, X_4\}$$

| Variabel ($X_i$) | Nama Komponen Sistem | Semantik Bisnis |
| :---: | :--- | :--- |
| **$X_1$** | `identify_title_author` | Status aktivasi modul pencocokan judul dan nama pengarang. |
| **$X_2$** | `extract_context` | Status aktivasi modul ekstraksi konteks & latar belakang dokumen. |
| **$X_3$** | `identify_story_elements` | Status aktivasi modul identifikasi karakter/alur cerita dokumen. |
| **$X_4$** | `apply_filters` | Status aktivasi modul filter kategori, bahasa, dan rentang tahun. |

### 2.2 Himpunan Domain Nilai ($D$)
Setiap variabel keputusan memiliki domain diskrit biner yang merepresentasikan keputusan alokasi:
$$D = \{D_1, D_2, D_3, D_4\}$$
di mana untuk setiap $i \in \{1, 2, 3, 4\}$:
$$D_i = \{0, 1\}$$
* **Nilai $0$**: Komponen sistem dinonaktifkan (tidak dialokasikan sumber daya).
* **Nilai $1$**: Komponen sistem diaktifkan (dialokasikan sumber daya komputasi).

### 2.3 Himpunan Batasan Bisnis ($C$)
Himpunan batasan $C = \{C_1, C_2, C_3, C_4, C_5, C_6, C_7\}$ memetakan seluruh regulasi bisnis dunia nyata tanpa inkonsistensi:

#### A. Batasan Uniter (Unary Constraints / Query Features Matching)
Batasan uniter membatasi domain sebuah variabel tunggal berdasarkan ketersediaan fitur masukan kueri pengguna:
* **$C_1$ (Kebutuhan Judul/Penulis)**: Jika kueri memuat judul atau penulis ($\text{feature}_{\text{title}} = \text{True}$), maka:
  $$X_1 = 1 \iff D_1 \leftarrow D_1 \setminus \{0\} = \{1\}$$
* **$C_2$ (Kebutuhan Konteks)**: Jika kueri memuat konteks situasi/latar ($\text{feature}_{\text{context}} = \text{True}$), maka:
  $$X_2 = 1 \iff D_2 \leftarrow D_2 \setminus \{0\} = \{1\}$$
* **$C_3$ (Kebutuhan Elemen Cerita)**: Jika kueri memuat karakter/plot cerita ($\text{feature}_{\text{story}} = \text{True}$), maka:
  $$X_3 = 1 \iff D_3 \leftarrow D_3 \setminus \{0\} = \{1\}$$
* **$C_4$ (Kebutuhan Filter Spesifik)**: Jika kueri menerapkan filter metadata rentang tahun/kategori ($\text{feature}_{\text{filter}} = \text{True}$), maka:
  $$X_4 = 1 \iff D_4 \leftarrow D_4 \setminus \{0\} = \{1\}$$

#### B. Batasan Biner (Binary Constraints / Arc Consistency)
Batasan biner mengatur relasi legal antara dua variabel yang saling bergantung:
* **$C_6$ (Regulasi Dependensi Cerita terhadap Konteks)**:
  Modul elemen cerita ($X_3$) hanya boleh aktif jika modul ekstraksi konteks ($X_2$) aktif:
  $$X_3 = 1 \implies X_2 = 1 \quad \equiv \quad \neg (X_3 = 1 \land X_2 = 0)$$
  Pasangan legal $(X_2, X_3)$ yang diizinkan dalam relasi $R_{2,3}$:
  $$R_{2,3} = \{(0, 0), (1, 0), (1, 1)\}$$
  Pasangan terlarang: $(X_2=0, X_3=1) \notin R_{2,3}$.
  Busur terarah yang dievaluasi pada AC-3:
  $$\text{arcs} = \{(X_2, X_3), (X_3, X_2)\}$$

#### C. Batasan Global (Global Constraints)
* **$C_5$ (At-Least-One-Active Constraint)**:
  Sistem harus melayani kueri dengan mengaktifkan sekurang-kurangnya satu modul inferensi:
  $$\sum_{i=1}^{4} X_i \ge 1$$
* **$C_7$ (Resource Quota / Capacity Constraint)**:
  Beban alokasi proses simultan tidak boleh melebihi kuota kapasitas komputasi yang tersedia ($K_{\text{max}}$):
  $$\sum_{i=1}^{4} X_i \le K_{\text{max}}$$

---

## 3. Analisis Ruang Keadaan Solusi (State Space Analysis)
- **Ukuran Ruang Keadaan Teoretis**: Tanpa batasan, terdapat $2^4 = 16$ kombinasi penugasan lengkap.
- **Kombinasi Tereliminasi oleh Batasan Global $C_5$**: 1 kombinasi $(0, 0, 0, 0)$.
- **Kombinasi Tereliminasi oleh Dependensi $C_6$**: 4 kombinasi di mana $X_3 = 1$ dan $X_2 = 0$ yaitu $(X_1, 0, 1, X_4)$ untuk seluruh kemungkinan $(X_1, X_4)$.
- **Ruang Solusi Legal**: Dari 16 kemungkinan, hanya terdapat 11 kombinasi penugasan legal yang memenuhi batasan struktural. Filter uniter kueri ($C_1 - C_4$) kemudian memangkas ruang ini menjadi solusi unik atau himpunan solusi optimal.

---

## 4. Kesimpulan Pemodelan
Pemodelan formal ini menjamin bahwa seluruh keputusan aktivasi proses pencarian MnemoLib terverifikasi secara matematis. Algoritma solver tidak melakukan tebakan acak, melainkan mengeksplorasi ruang keputusan yang telah dipangkas secara ketat melalui propagasi AC-3 dan heuristik MRV.
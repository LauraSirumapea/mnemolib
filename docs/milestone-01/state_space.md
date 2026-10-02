# Formulasi Formal Ruang Keadaan (State Space): MnemoLib

Proses pencarian keputusan pada sistem MnemoLib diformulasikan secara formal ke dalam 5 elemen:
\[ \mathcal{S}_{search} = \langle X, A, T, G, C \rangle \]

---

## 1. State Space ($X$) - Himpunan Status
Kumpulan status yang merepresentasikan tahapan pemrosesan kueri pengguna:
* $s_0 = \text{start}$: Titik awal saat sesi pencarian dimulai.
* $s_1 = \text{query\_received}$: Kueri potongan ingatan dari pengguna berhasil diterima sistem.
* $s_2 = \text{identify\_title\_author}$: Sistem memeriksa apakah pengguna mengingat potongan judul atau nama penulis.
* $s_3 = \text{extract\_context}$: Sistem memproses konteks cerita, alur, atau topik bahasan buku.
* $s_4 = \text{identify\_story\_elements}$: Sistem mengidentifikasi tokoh cerita, latar belakang, atau elemen spesifik.
* $s_5 = \text{apply\_filters}$: Sistem menyaring berdasarkan kategori, genre, atau perkiraan tahun terbit.
* $s_6 = \text{catalog\_lookup}$: Sistem melakukan pencarian kandidat ke katalog perpustakaan.
* $s_G = \text{results\_presented}$: Buku rekomendasi berhasil ditemukan dan disajikan ke antarmuka pengguna *(Goal State)*.

---

## 2. Action Space ($A$) - Himpunan Tindakan
Aksi yang dapat diambil oleh sistem untuk berpindah antar-status:
* $a_1$: Menerima dan memvalidasi teks masukan dari pengguna.
* $a_2$: Mengecek kata kunci judul atau penulis yang eksplisit.
* $a_3$: Membedah teks narasi atau topik bahasan ingatan pengguna.
* $a_4$: Memetakan tokoh cerita atau latar narasi yang diingat.
* $a_5$: Menyaring basis data dengan atribut kategori atau tahun.
* $a_6$: Mencari kecocokan dokumen ke basis data perpustakaan.
* $a_7$: Menampilkan daftar buku rekomendasi beserta informasi rak.

---

## 3. Transition Model ($T$) - Model Perubahan Status
Fungsi transisi deterministik $T(s, a) \to s'$:
* $T(\text{start}, a_1) = \text{query\_received}$
* $T(\text{query\_received}, a_2) = \text{identify\_title\_author}$
* $T(\text{query\_received}, a_3) = \text{extract\_context}$
* $T(\text{query\_received}, a_5) = \text{apply\_filters}$
* $T(\text{identify\_title\_author}, a_6) = \text{catalog\_lookup}$
* $T(\text{extract\_context}, a_4) = \text{identify\_story\_elements}$
* $T(\text{identify\_story\_elements}, a_6) = \text{catalog\_lookup}$
* $T(\text{apply_filters}, a_6) = \text{catalog\_lookup}$
* $T(\text{catalog\_lookup}, a_7) = \text{results\_presented}$

---

## 4. Goal Test ($G$) - Pengujian Tujuan
Kondisi tujuan tercapai jika sistem berada pada status $s_G = \text{results\_presented}$ dan berhasil menemukan minimal satu kandidat buku dengan tingkat relevansi di atas ambang batas.

---

## 5. Step Cost ($C$) - Biaya Langkah (Waktu Proses Nyata)
Biaya diukur berdasarkan estimasi waktu pemrosesan nyata dalam satuan **milidetik (ms)**:
* `start` $\to$ `query_received`: $5\text{ ms}$ (Penerimaan input teks)
* `query_received` $\to$ `identify_title_author`: $20\text{ ms}$ (Pencocokan pola leksikal)
* `query_received` $\to$ `extract_context`: $45\text{ ms}$ (Analisis konteks naratif)
* `query_received` $\to$ `apply_filters`: $15\text{ ms}$ (Filter atribut tahun/kategori)
* `identify_title_author` $\to$ `catalog_lookup`: $30\text{ ms}$ (Pencarian indeks katalog)
* `extract_context` $\to$ `identify_story_elements`: $20\text{ ms}$ (Pemilahan tokoh/alur)
* `identify_story_elements` $\to$ `catalog_lookup`: $50\text{ ms}$ (Pencarian kemiripan semantik)
* `apply_filters` $\to$ `catalog_lookup`: $40\text{ ms}$ (Pencarian katalog terfilter)
* `catalog_lookup` $\to$ `results_presented`: $10\text{ ms}$ (Penyusunan tampilan hasil)
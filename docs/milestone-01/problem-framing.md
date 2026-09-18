# Dokumen Problem Framing: MnemoLib

## 1. Profil Organisasi Mitra
* **Nama Organisasi**: Perpustakaan & Pusat Informasi Institut Teknologi Del (IT Del Library & Information Center).
* **Bidang Operasional**: Layanan Informasi Akademik, Pengelolaan Koleksi Buku Teks, Skripsi/Tugas Akhir, dan Jurnal Ilmiah.
* **Volume Data**:
  - Mengelola lebih dari **15.000 judul buku cetak** dan **5.000 laporan Tugas Akhir/Tesis**.
  - Melayani lebih dari **1.500 civitas akademika aktif** (mahasiswa, dosen, dan peneliti kampus IT Del).

---

## 2. Analisis Masalah Nyata (Pain Points)
1. **Lupa Judul (Tip-of-the-Tongue):** Lebih dari 40% mahasiswa mencari buku dengan hanya mengingat cerita, topik, atau ciri fisiknya tanpa mengingat judul atau penulis persis.
2. **Katalog OPAC Terlalu Kaku:** Pencarian katalog konvensional mengharuskan kecocokan kata persis (exact match). Kueri naratif ("buku optimasi graf sampul biru") menghasilkan 0 hasil.
3. **Waktu Pustakawan Tersita:** Mahasiswa harus mengantre di meja sirkulasi untuk tanya-jawab manual dengan petugas selama 10–15 menit per orang.

---

## 3. Justifikasi Adopsi AI
* **Kelemahan Cara Konvensional:** SQL `LIKE` atau pencarian teks biasa hanya membaca huruf demi huruf, sehingga tidak mengerti sinonim atau parafrase cerita.
* **Kelebihan Pendekatan AI (MnemoLib):**
  1. **Uniform Cost Search (UCS):** Memilih jalur pemrosesan data dengan waktu proses tercepat.
  2. **Pencarian Semantik (Dense Vector):** Memahami kedekatan arti cerita mahasiswa dengan isi buku di perpustakaan.
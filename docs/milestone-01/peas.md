# Spesifikasi Formal PEAS: MnemoLib

| Komponen | Spesifikasi & Rincian Terukur |
|---|---|
| **Performance Measure**<br>*(Ukuran Kinerja)* | • **Akurasi Pencarian (≥85%):** Tingkat keberhasilan menemukan buku yang sesuai dengan ingatan pengguna.<br>• **Relevansi Hasil:** Tingkat kecocokan rekomendasi dengan informasi parsial pengguna.<br>• **Waktu Respon Cepat (<1,5 detik):** Kecepatan sistem menghasilkan rekomendasi buku.<br>• **Waktu Keputusan Rute Graf (≤50 ms):** Kecepatan algoritma UCS menentukan jalur terbaik.<br>• **Kepuasan Pengguna:** Kemudahan pengguna menemukan koleksi tanpa harus bertanya manual ke pustakawan. |
| **Environment**<br>*(Lingkungan)* | Lingkungan katalog perpustakaan digital Institut Teknologi Del (IT Del) yang berisi koleksi buku teks, laporan tugas akhir, dan jurnal beserta metadata seperti judul, penulis, kategori, tahun terbit, dan deskripsi/sinopsis. |
| **Actuators**<br>*(Alat Bertindak)* | Sistem memberikan keluaran berupa daftar kartu rekomendasi buku/jurnal, nomor rak buku di perpustakaan, informasi metadata koleksi, dan hasil pencarian berdasarkan input pengguna. |
| **Sensors**<br>*(Alat Masukan)* | Sistem menerima input berupa potongan ingatan pengguna seperti kata kunci, potongan cerita, karakter, topik, penulis terduga, atau konteks lain yang diingat pengguna. |


## Klasifikasi Lingkungan (Russell & Norvig)

1. **Partially Observable**  
   Sistem tidak memperoleh informasi lengkap mengenai buku yang dicari karena pengguna hanya memberikan potongan ingatan yang belum utuh.

2. **Single Agent**  
   MnemoLib berperan sebagai satu intelligent agent mandiri yang melakukan proses penalaran, pencarian, dan rekomendasi buku.

3. **Stochastic**  
   Hasil pencarian memiliki kemungkinan berbeda karena informasi yang diberikan pengguna dapat bersifat subjektif, ambigu, dan tidak lengkap.

4. **Sequential**  
   Proses pencarian dilakukan melalui beberapa tahap berurutan (terima kueri → ekstraksi → pencarian → perankingan) hingga menghasilkan rekomendasi buku.

5. **Dynamic**  
   Data koleksi perpustakaan dapat berubah apabila terdapat peminjaman, pengembalian, atau penambahan koleksi buku/jurnal baru.

6. **Discrete**  
   Informasi koleksi buku, metadata, status pencarian, dan hasil pencarian direpresentasikan dalam bentuk data diskrit yang terdefinisi jelas.
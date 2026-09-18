# 4. Spesifikasi Formal PEAS

| Komponen | Spesifikasi |
|---|---|
| Performance Measure | Mengukur keberhasilan sistem berdasarkan akurasi hasil pencarian, relevansi buku/jurnal yang ditemukan, waktu respon pencarian, dan kepuasan pengguna terhadap rekomendasi yang diberikan. |
| Environment | Lingkungan sistem berupa katalog perpustakaan digital yang berisi koleksi buku dan jurnal beserta metadata seperti judul, penulis, kategori, tahun terbit, dan deskripsi. |
| Actuators | Sistem memberikan keluaran berupa daftar rekomendasi buku/jurnal, informasi metadata koleksi, dan hasil pencarian berdasarkan input pengguna. |
| Sensors | Sistem menerima input berupa potongan ingatan pengguna seperti kata kunci, potongan cerita, karakter, topik, penulis, atau konteks lain yang diingat pengguna. |


## Klasifikasi Lingkungan (Russell & Norvig)

1. **Partially Observable**  
   Sistem tidak mengetahui informasi lengkap buku yang dicari karena pengguna hanya memberikan potongan ingatan.

2. **Single Agent**  
   MnemoLib berperan sebagai satu agen yang melakukan proses pencarian dan rekomendasi.

3. **Stochastic**  
   Hasil pencarian dapat berbeda karena input pengguna bersifat tidak pasti dan subjektif.

4. **Sequential**  
   Proses pencarian dilakukan melalui beberapa tahapan sebelum menghasilkan rekomendasi.

5. **Dynamic**  
   Koleksi buku dan jurnal dapat berubah karena adanya penambahan atau pembaruan data.

6. **Discrete**  
   Data koleksi dan proses pencarian direpresentasikan dalam bentuk data diskrit.
# MnemoLib PEAS Specification

## 1. Overview

PEAS (Performance Measure, Environment, Actuators, Sensors) digunakan untuk mendefinisikan karakteristik intelligent agent pada sistem MnemoLib.

MnemoLib merupakan sistem katalog perpustakaan cerdas yang membantu pengguna menemukan buku atau jurnal berdasarkan potongan ingatan pengguna, seperti informasi judul yang tidak lengkap, karakter, konteks cerita, topik, atau metadata lainnya.

---

# 2. Performance Measure (P)

Performance Measure menjelaskan indikator keberhasilan sistem dalam mencapai tujuan pencarian.

| Parameter | Deskripsi |
|---|---|
| Search Accuracy | Kemampuan sistem menemukan buku atau jurnal yang sesuai dengan kebutuhan pengguna |
| Result Relevance | Tingkat kesesuaian hasil pencarian dengan query pengguna |
| Response Time | Kecepatan sistem memberikan hasil pencarian |
| Retrieval Success Rate | Tingkat keberhasilan menemukan koleksi yang dicari |
| User Satisfaction | Tingkat kepuasan pengguna terhadap hasil pencarian |

---

# 3. Environment (E)

Environment menjelaskan lingkungan tempat intelligent agent bekerja.

| Komponen | Deskripsi |
|---|---|
| Library Catalog | Database koleksi buku dan jurnal |
| Book Metadata | Informasi buku seperti judul, penulis, tahun, kategori, dan sinopsis |
| User Input | Informasi yang diberikan pengguna berdasarkan ingatan mereka |
| Digital Library Collection | Kumpulan koleksi yang tersedia dalam sistem |
| User Interaction | Interaksi antara pengguna dan sistem pencarian |

---

# 4. Actuators (A)

Actuators merupakan tindakan yang dilakukan sistem kepada pengguna.

| Actuator | Fungsi |
|---|---|
| Display Search Results | Menampilkan kandidat buku atau jurnal |
| Show Metadata | Menampilkan detail koleksi seperti judul, penulis, dan tahun |
| Rank Results | Mengurutkan hasil berdasarkan tingkat relevansi |
| Provide Recommendation | Memberikan rekomendasi koleksi yang sesuai |
| Request Clarification | Meminta informasi tambahan ketika query belum cukup |

---

# 5. Sensors (S)

Sensors merupakan informasi yang diterima sistem dari pengguna.

| Sensor | Contoh Input |
|---|---|
| Text Query | Deskripsi buku atau jurnal yang diingat pengguna |
| Keywords | Kata kunci terkait koleksi |
| Story Elements | Karakter, lokasi, kejadian, atau tema cerita |
| Metadata Filter | Tahun publikasi, kategori, jenis koleksi |
| User Feedback | Konfirmasi atau koreksi hasil pencarian |

---

# 6. Environment Classification

Klasifikasi lingkungan sistem MnemoLib:

| Properti | Klasifikasi | Penjelasan |
|---|---|---|
| Observability | Partially Observable | Sistem tidak mengetahui seluruh informasi yang ada dalam ingatan pengguna |
| Deterministic | Stochastic | Hasil pencarian bergantung pada variasi input pengguna |
| Episodic / Sequential | Sequential | Proses pencarian dilakukan melalui beberapa tahap |
| Static / Dynamic | Dynamic | Koleksi perpustakaan dapat berubah dan bertambah |
| Discrete / Continuous | Discrete | State pencarian terdiri dari kondisi tertentu |
| Number of Agents | Single Agent | Sistem bertindak sebagai satu intelligent agent |

---

# 7. Conclusion

Berdasarkan PEAS specification, MnemoLib merupakan intelligent agent yang menerima informasi tidak lengkap dari pengguna, memproses pencarian pada katalog perpustakaan, dan menghasilkan rekomendasi buku atau jurnal yang relevan.

PEAS ini menjadi dasar perancangan sistem sebelum implementasi state space search dan pengembangan fitur semantic search pada milestone berikutnya.
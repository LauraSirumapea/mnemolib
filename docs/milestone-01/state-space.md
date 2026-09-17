# MnemoLib — State Space & Baseline Search

## 1. Overview

MnemoLib merupakan sistem katalog perpustakaan cerdas yang dirancang untuk membantu pengguna menemukan buku atau jurnal berdasarkan informasi yang masih diingat, seperti judul, nama penulis, karakter, potongan cerita, atau konteks tertentu.

Pada Milestone 1, proses pencarian dimodelkan sebagai sebuah state space dan digunakan sebagai baseline untuk algoritma Uniform Cost Search (UCS).

Baseline ini digunakan untuk memodelkan alur keputusan pencarian. Semantic search, embeddings, dan vector database merupakan pengembangan pada milestone berikutnya.

---

## 2. Formal State-Space Model

State space MnemoLib diformalkan menggunakan:

(X, A, T, G, C)

dengan:

- X = himpunan state
- A = himpunan action
- T = transition function
- G = goal state
- C = transition cost

---

## 3. X — States

Himpunan state pada baseline MnemoLib adalah:

X = {
    start,
    query_received,
    identify_title_author,
    extract_context,
    identify_story_elements,
    apply_filters,
    catalog_lookup,
    results_presented
}

### Deskripsi State

| State | Deskripsi |
|---|---|
| start | Kondisi awal proses pencarian |
| query_received | Sistem telah menerima query dari pengguna |
| identify_title_author | Sistem memproses informasi judul atau penulis yang diberikan |
| extract_context | Sistem mengekstraksi konteks dari deskripsi pengguna |
| identify_story_elements | Sistem mengidentifikasi elemen cerita seperti karakter atau kejadian |
| apply_filters | Sistem menerapkan filter pencarian yang diberikan pengguna |
| catalog_lookup | Sistem melakukan pencarian terhadap katalog |
| results_presented | Sistem menampilkan hasil pencarian kepada pengguna |

---

## 4. A — Actions

Action merupakan tindakan yang menyebabkan sistem berpindah dari satu state ke state berikutnya.

Action yang digunakan pada baseline:

- receive_query
- identify_title_author
- extract_context
- identify_story_elements
- apply_filters
- catalog_lookup
- present_results

Action tersebut merepresentasikan tahapan proses keputusan pencarian dalam MnemoLib.

---

## 5. T — Transition

Transition menunjukkan perpindahan dari state saat ini menuju state berikutnya.

Struktur transition baseline MnemoLib adalah:

start
→ query_received

query_received
→ identify_title_author
→ extract_context
→ apply_filters

identify_title_author
→ catalog_lookup

extract_context
→ identify_story_elements

identify_story_elements
→ catalog_lookup

apply_filters
→ catalog_lookup

catalog_lookup
→ results_presented

Dengan demikian, terdapat beberapa alternatif jalur pencarian dari query pengguna menuju hasil pencarian.

---

## 6. G — Goal

Goal state pada baseline MnemoLib adalah:

G = results_presented

Proses pencarian dianggap mencapai tujuan ketika sistem telah mencapai state results_presented dan hasil pencarian dapat diberikan kepada pengguna.

---

## 7. C — Transition Cost

Setiap transition memiliki weighted cost yang digunakan oleh Uniform Cost Search untuk membandingkan jalur pencarian.

Pada baseline Milestone 1, cost digunakan sebagai representasi effort operasional relatif antar-transition dan merupakan parameter baseline untuk eksperimen UCS.

Cost pada implementasi baseline:

| Transition | Cost |
|---|---:|
| start → query_received | 1 |
| query_received → identify_title_author | 2 |
| query_received → extract_context | 3 |
| query_received → apply_filters | 2 |
| identify_title_author → catalog_lookup | 2 |
| extract_context → identify_story_elements | 2 |
| identify_story_elements → catalog_lookup | 3 |
| apply_filters → catalog_lookup | 3 |
| catalog_lookup → results_presented | 2 |

Nilai cost tersebut merupakan weighted baseline yang ditetapkan untuk Milestone 1 dan bukan klaim sebagai data produksi perpustakaan.

---

## 8. Uniform Cost Search

Uniform Cost Search digunakan untuk menemukan jalur dari state awal menuju goal state dengan total transition cost paling rendah.

Implementasi menggunakan Python priority queue melalui modul `heapq`.

Source code tersedia pada:

- `src/mnemolib/search/ucs.py`
- `src/mnemolib/search/mnemolib_graph.py`

Automated tests tersedia pada:

- `tests/test_ucs.py`

---

## 9. Contoh Jalur Pencarian

Salah satu jalur yang tersedia adalah:

start
→ query_received
→ identify_title_author
→ catalog_lookup
→ results_presented

Total cost:

1 + 2 + 2 + 2 = 7

Jalur lain:

start
→ query_received
→ extract_context
→ identify_story_elements
→ catalog_lookup
→ results_presented

Total cost:

1 + 3 + 2 + 3 + 2 = 11

Jalur:

start
→ query_received
→ apply_filters
→ catalog_lookup
→ results_presented

Total cost:

1 + 2 + 3 + 2 = 8

Berdasarkan weighted cost pada baseline, UCS memilih jalur dengan total cost terendah.

---

## 10. Testing

Baseline search diuji menggunakan pytest.

Hasil pengujian:

3 passed

Pengujian mencakup:

1. UCS menemukan jalur dengan cost terendah.
2. UCS mengembalikan hasil yang sesuai ketika goal tidak dapat dicapai.
3. UCS menolak transition dengan negative cost.

Command yang digunakan:

```bash
uv run pytest


---

## ⚠️ Ada satu hal penting soal bagian Cost

Aku sengaja menulis:

> **"weighted baseline"**

dan bukan:

> "biaya nyata perpustakaan sebesar X rupiah/detik."

Karena dari materi yang kita punya, **tidak ada data operasional perpustakaan nyata yang memberikan angka cost tersebut**. Modul memang menyebut “berbobot biaya riil”, jadi kita **jangan memalsukan data**. :contentReference[oaicite:1]{index=1}

Untuk sementara ini dokumen secara jujur menyatakan bahwa angka tersebut adalah **baseline parameter**.

**Tapi nanti sebelum submission final, kita perlu evaluasi apakah dosen mengharuskan cost benar-benar berasal dari pengukuran nyata.** Kalau iya, kita akan revisi model cost dengan data/pengukuran yang bisa kalian pertanggungjawabkan.

---

# STEP 3 — Save

Tekan:

**Ctrl + S**

Setelah itu **jangan commit dulu**.

Kita akan cek apakah dokumentasi ini benar-benar konsisten dengan kode kita.

Jalankan lagi:

```powershell
uv run pytest
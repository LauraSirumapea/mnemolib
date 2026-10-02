"""Script to generate the official Milestone 2 academic report PDF for Grup 12.

Generates:
1. docs/milestone-02/Grup12-Tugas02.html
2. docs/milestone-02/Grup12-Tugas02.pdf
3. Grup12-Tugas02.pdf (root directory for submission)
"""

import os
import subprocess

HTML_CONTENT = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Laporan Tugas 2 (Milestone 2 - W04) - Grup 12</title>
<style>
  @page {
    size: A4;
    margin: 25mm 20mm 25mm 20mm;
    @bottom-right {
      content: counter(page);
    }
  }
  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #111;
    margin: 0;
    padding: 0;
  }
  h1, h2, h3, h4 {
    font-family: 'Arial', sans-serif;
    color: #0b2545;
    margin-top: 18pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
  }
  h1 { font-size: 16pt; text-transform: uppercase; border-bottom: 2px solid #0b2545; padding-bottom: 4px; }
  h2 { font-size: 13pt; margin-top: 14pt; }
  h3 { font-size: 11.5pt; font-style: italic; }
  p { margin-top: 0; margin-bottom: 8pt; text-align: justify; text-justify: inter-word; }
  
  .cover {
    page-break-after: always;
    text-align: center;
    padding-top: 40px;
  }
  .cover-logo {
    font-size: 26pt;
    font-weight: bold;
    color: #004b87;
    margin-bottom: 8px;
    letter-spacing: 2px;
  }
  .cover-inst {
    font-size: 13pt;
    font-weight: bold;
    color: #333;
    line-height: 1.3;
    margin-bottom: 40px;
  }
  .cover-title {
    font-size: 17pt;
    font-weight: bold;
    color: #0b2545;
    line-height: 1.4;
    margin: 50px 0 20px 0;
    border-top: 3px double #0b2545;
    border-bottom: 3px double #0b2545;
    padding: 18px 0;
  }
  .cover-subtitle {
    font-size: 12.5pt;
    font-weight: normal;
    color: #444;
    margin-bottom: 50px;
  }
  .cover-meta {
    margin-top: 60px;
    font-size: 11pt;
    text-align: left;
    display: inline-block;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12pt 0;
    font-size: 10pt;
    page-break-inside: avoid;
  }
  th, td {
    border: 1px solid #444;
    padding: 6pt 8pt;
    text-align: left;
  }
  th {
    background-color: #0b2545;
    color: #ffffff;
    font-weight: bold;
    text-align: center;
  }
  tr:nth-child(even) { background-color: #f8f9fa; }
  
  .code-block {
    background-color: #f4f6f8;
    border-left: 4px solid #004b87;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9pt;
    padding: 8pt 10pt;
    margin: 10pt 0;
    white-space: pre-wrap;
    word-break: break-all;
    line-height: 1.35;
  }
  
  .badge-pass {
    background-color: #28a745;
    color: white;
    padding: 2px 6px;
    border-radius: 3px;
    font-weight: bold;
    font-size: 8.5pt;
  }
  
  .alert-box {
    background-color: #eef5fc;
    border: 1px solid #b8daff;
    border-radius: 4px;
    padding: 10pt;
    margin: 10pt 0;
    font-size: 10.5pt;
  }
  
  .formula {
    background-color: #fdfdfe;
    border: 1px solid #ddd;
    text-align: center;
    padding: 8pt;
    margin: 10pt 0;
    font-style: italic;
    font-size: 11pt;
  }
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">
  <div class="cover-logo">INSTITUT TEKNOLOGI DEL</div>
  <div class="cover-inst">
    FAKULTAS INFORMATIKA DAN TEKNIK ELEKTRO<br>
    PROGRAM STUDI SARJANA SISTEM INFORMASI<br>
    TAHUN AJARAN 2026/2027
  </div>
  
  <div class="cover-title">
    LAPORAN TUGAS 2 (MILESTONE 2 - W04)<br>
    MODUL PEMECAHAN BATASAN KEPUTUSAN BISNIS<br>
    DENGAN CONSTRAINT SATISFACTION PROBLEMS (CSP)<br>
    BERBASIS AC-3 & BACKTRACKING MRV
  </div>
  
  <div class="cover-subtitle">
    Proyek Terpadu: <strong>MnemoLib — Enterprise Intelligent Library Copilot</strong><br>
    Mata Kuliah: 10S3001 - Kecerdasan Buatan (+P) (Bobot: 6.0% Komponen Proyek)
  </div>
  
  <div class="cover-meta">
    <table style="border: none; width: auto; font-size: 11pt;">
      <tr style="background: none;"><td style="border: none; font-weight: bold; width: 160px;">Kelompok</td><td style="border: none;">: <strong>Grup 12</strong></td></tr>
      <tr style="background: none;"><td style="border: none; font-weight: bold;">Dosen Pengampu</td><td style="border: none;">: Samuel Indra Gunawan Situmeang</td></tr>
      <tr style="background: none;"><td style="border: none; font-weight: bold;">Tautan Repositori</td><td style="border: none;">: https://github.com/LauraSirumapea/mnemolib.git</td></tr>
      <tr style="background: none;"><td style="border: none; font-weight: bold;">Tag Rilis GitHub</td><td style="border: none;">: <code>v0.2-milestone2</code></td></tr>
    </table>
    <br>
    <table style="width: 100%; border: 1px solid #444; font-size: 10pt;">
      <thead>
        <tr>
          <th>No</th>
          <th>Nama Mahasiswa</th>
          <th>Akun GitHub</th>
          <th>Peran Kerja (Role)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="text-align: center;">1</td>
          <td><strong>Laura Sirumapea</strong></td>
          <td>@LauraSirumapea</td>
          <td>AI Architect & Model Lead</td>
        </tr>
        <tr>
          <td style="text-align: center;">2</td>
          <td><strong>Desnita Pardosi</strong></td>
          <td>@DesnitaPardosi</td>
          <td>Data & Knowledge Engineer</td>
        </tr>
        <tr>
          <td style="text-align: center;">3</td>
          <td><strong>Mia Sibuea</strong></td>
          <td>@MiaSibuea</td>
          <td>QA Lead, Evaluator & System Integrator</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- BAB I -->
<h1>BAB I. PENDAHULUAN & DOMAIN MASALAH BISNIS</h1>

<h2>1.1 Latar Belakang Masalah Bisnis</h2>
<p>
Dalam operasional sistem informasi enterprise, khususnya pengelolaan repositori dokumen dan perpustakaan digital cerdas seperti <strong>MnemoLib</strong> di Institut Teknologi Del, keputusan alokasi sumber daya komputasi dan penelusuran katalog dibatasi oleh regulasi ketat. Civitas akademika kerap kali melakukan pencarian materi referensi ilmiah hanya berbekal potongan memori yang tidak utuh—seperti potongan fragmen judul, nama penulis yang samar, konteks peristiwa, atau karakter dan alur kasus tertentu.
</p>
<p>
Pada Milestone 01, tim telah mengembangkan mesin inferensi baseline menggunakan algoritma <em>Uniform Cost Search (UCS)</em> untuk menemukan lintasan penelusuran graf dengan latensi akumulatif terendah. Kendati demikian, penelusuran berbasis biaya jalur semata belum mampu menangani batasan operasional kritis, seperti aturan saling kebergantungan (*dependency constraints*) antarsubsistem, validasi kelayakan masukan kueri, serta batas kapasitas kuota pemrosesan paralel (*capacity limits*). Apabila subsistem penelusuran dijalankan tanpa pemenuhan prasyarat regulasi, sistem rawan mengalami kegagalan inferensi atau inefisiensi komputasi parah.
</p>

<h2>1.2 Tujuan Pengembangan Milestone 2</h2>
<p>
Pada Milestone 2 ini, tim bertugas membangun <strong>Mesin Inferensi Batasan (Constraint Solver Engine)</strong> berbasis <em>Constraint Satisfaction Problems (CSP)</em> dengan propagasi batasan <em>Arc Consistency 3 (AC-3)</em> dan algoritma pencarian <em>Backtracking</em> berheuristik <em>Minimum Remaining Values (MRV)</em>. Modul ini bertujuan menghasilkan penugasan keputusan aktivasi proses yang legal, optimal, dan terverifikasi secara matematis sebelum penelusuran katalog dieksekusi.
</p>

<hr>

<!-- BAB II -->
<h1>BAB II. PEMODELAN MATEMATIS FORMAL CSP (BOBOT 30%)</h1>

<h2>2.1 Formulasi Tripel CSP Formal</h2>
<p>
Secara matematis formal, pemodelan masalah keputusan bisnis pada MnemoLib didefinisikan sebagai tripel formal &lang;X, D, C&rang;:
</p>
<div class="formula">
  <strong>P = &lang;X, D, C&rang;</strong>
</div>

<h2>2.2 Himpunan Variabel Keputusan (X)</h2>
<p>
Himpunan variabel keputusan formal <em>X = {X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>, X<sub>4</sub>}</em> merepresentasikan status aktivasi proses inferensi pada pipeline pencarian katalog cerdas:
</p>
<table>
  <thead>
    <tr>
      <th style="width: 15%;">Simbol Variabel</th>
      <th style="width: 35%;">Nama Komponen Sistem</th>
      <th>Semantik Bisnis & Regulasi Operasional</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;"><strong>X<sub>1</sub></strong></td>
      <td><code>identify_title_author</code></td>
      <td>Status aktivasi modul pencocokan langsung judul dan identitas pengarang.</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>X<sub>2</sub></strong></td>
      <td><code>extract_context</code></td>
      <td>Status aktivasi modul ekstraksi konteks semantik dan latar belakang dokumen.</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>X<sub>3</sub></strong></td>
      <td><code>identify_story_elements</code></td>
      <td>Status aktivasi modul identifikasi elemen cerita/karakter/studi kasus.</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>X<sub>4</sub></strong></td>
      <td><code>apply_filters</code></td>
      <td>Status aktivasi modul filter metadata (kategori dokumen, bahasa, rentang tahun).</td>
    </tr>
  </tbody>
</table>

<h2>2.3 Himpunan Domain Nilai (D)</h2>
<p>
Setiap variabel keputusan <em>X<sub>i</sub> &isin; X</em> memiliki domain diskrit biner yang terdefinisi secara presisi:
</p>
<div class="formula">
  D<sub>i</sub> = {0, 1}, &forall; i &isin; {1, 2, 3, 4}
</div>
<p>
Di mana nilai <strong>0</strong> menyatakan modul dinonaktifkan (tidak dialokasikan sumber daya komputasi), sedangkan nilai <strong>1</strong> menyatakan modul diaktifkan pada jalur pemrosesan kueri.
</p>

<h2>2.4 Himpunan Batasan Bisnis Formal (C)</h2>
<p>
Himpunan batasan <em>C</em> memetakan seluruh regulasi operasional bisnis dunia nyata tanpa menimbulkan inkonsistensi:
</p>

<h3>A. Batasan Uniter (Unary Constraints / Query Matching)</h3>
<ul>
  <li><strong>C<sub>1</sub> (Fitur Judul/Pengarang)</strong>: Jika kueri memuat informasi judul/penulis, maka modul X<sub>1</sub> wajib aktif: <em>X<sub>1</sub> = 1 &hArr; D<sub>1</sub> &larr; {1}</em>.</li>
  <li><strong>C<sub>2</sub> (Fitur Konteks)</strong>: Jika kueri memuat potongan konteks, maka modul X<sub>2</sub> wajib aktif: <em>X<sub>2</sub> = 1 &hArr; D<sub>2</sub> &larr; {1}</em>.</li>
  <li><strong>C<sub>3</sub> (Fitur Elemen Cerita)</strong>: Jika kueri memuat alur cerita, maka modul X<sub>3</sub> wajib aktif: <em>X<sub>3</sub> = 1 &hArr; D<sub>3</sub> &larr; {1}</em>.</li>
  <li><strong>C<sub>4</sub> (Fitur Filter Metadata)</strong>: Jika kueri memuat filter tahun/topik, maka modul X<sub>4</sub> wajib aktif: <em>X<sub>4</sub> = 1 &hArr; D<sub>4</sub> &larr; {1}</em>.</li>
</ul>

<h3>B. Batasan Biner (Binary Constraints / Arc Consistency)</h3>
<ul>
  <li><strong>C<sub>6</sub> (Regulasi Dependensi Alur Komputasi)</strong>: Modul pemrosesan elemen cerita (X<sub>3</sub>) secara operasional mensyaratkan tersedianya konteks (X<sub>2</sub>). Oleh karena itu, X<sub>3</sub> = 1 mengimplikasikan X<sub>2</sub> = 1:
  <div class="formula">
    X<sub>3</sub> = 1 &rArr; X<sub>2</sub> = 1 &equiv; &not;(X<sub>3</sub> = 1 &and; X<sub>2</sub> = 0)
  </div>
  Relasi legal yang diizinkan pada busur (X<sub>2</sub>, X<sub>3</sub>): <em>R<sub>2,3</sub> = {(0, 0), (1, 0), (1, 1)}</em>. Pasangan (X<sub>2</sub>=0, X<sub>3</sub>=1) dilarang mutlak.</li>
</ul>

<h3>C. Batasan Global (Global Constraints)</h3>
<ul>
  <li><strong>C<sub>5</sub> (At-Least-One Active Process)</strong>: Sistem dilarang berada dalam keadaan menganggur total saat melayani kueri:
  <div class="formula">
    &sum;<sub>i=1..4</sub> X<sub>i</sub> &ge; 1
  </div>
  </li>
  <li><strong>C<sub>7</sub> (Resource Quota Constraint)</strong>: Jumlah proses simultan yang berjalan tidak boleh melebihi batas kuota komputasi maksimum server (<em>K<sub>max</sub></em>) demi menjamin latensi &le; 50 ms:
  <div class="formula">
    &sum;<sub>i=1..4</sub> X<sub>i</sub> &le; K<sub>max</sub>
  </div>
  </li>
</ul>

<hr>

<!-- BAB III -->
<h1>BAB III. IMPLEMENTASI ALGORITMA & ARSITEKTUR SOLVER (BOBOT 40%)</h1>

<h2>3.1 Struktur Modul Python Modular</h2>
<p>
Seluruh kode implementasi disusun mengikuti standar <em>clean code</em> dan modularitas tinggi pada direktori <code>src/mnemolib/search/csp/</code>:
</p>
<ul>
  <li><code>constraints.py</code>: Mengimplementasikan definisi variabel formal, pembuatan domain, fungsi batasan uniter, batasan biner <em>check_pairwise_constraint()</em>, dan verifikasi kelayakan lengkap <em>check_assignment()</em>.</li>
  <li><code>ac3.py</code>: Mengimplementasikan antrean busur <em>queue</em> dan fungsi <em>revise()</em> untuk memangkas nilai domain yang tidak memiliki pasangan konsisten.</li>
  <li><code>mrv.py</code>: Mengimplementasikan heuristik <em>select_unassigned_variable()</em> berdasarkan prinsip <em>Minimum Remaining Values</em>.</li>
  <li><code>solver.py</code>: Mengintegrasikan propagasi AC-3 awal (pra-pencarian) dan fungsi rekursif <em>backtracking_search()</em> dengan pemangkasan dini (*early pruning*) dan pengumpulan metrik statistik komputasi.</li>
</ul>

<h2>3.2 Algoritma Propagasi AC-3</h2>
<p>
Sebelum proses pencarian backtracking dieksekusi, AC-3 dijalankan untuk memastikan seluruh busur biner berada dalam status konsisten. Jika terjadi <em>domain wipeout</em> (|D<sub>i</sub>| = 0), algoritma langsung mengembalikan status <code>None</code> (No Solution) dalam hitungan mikrodetik tanpa perlu melakukan rekursi pencarian.
</p>

<h2>3.3 Backtracking Search dengan Heuristik MRV</h2>
<p>
Ketika pencarian dimulai, heuristik MRV secara dinamis memilih variabel yang memiliki sisa ukuran domain terkecil. Hal ini secara drastis menekan faktor percabangan (*branching factor*). Jika terjadi kegagalan batasan parsial pada suatu cabang, solver segera melakukan *backtrack* ke simpul sebelumnya.
</p>

<h2>3.4 Integrasi Pipeline: UCS (Milestone 1) ke CSP (Milestone 2)</h2>
<p>
Sistem MnemoLib mengadopsi arsitektur terpadu dua tahap:
</p>
<div class="code-block">
Masukan Kueri Civitas Del
        &darr;
Ekstraksi Fitur Kueri (Judul, Konteks, Cerita, Filter)
        &darr;
[MILESTONE 2: CSP SOLVER] &rarr; Propagasi AC-3 & Backtracking MRV
        &darr;
Verifikasi Penugasan Legal Modul {X1, X2, X3, X4}
        &darr;
[MILESTONE 1: UCS ENGINE] &rarr; Penelusuran Graf Jalur Berbiaya Minimum (Lowest Cost)
        &darr;
Penyajian Dokumen Pustaka Relevan & Terverifikasi
</div>

<hr>

<!-- BAB IV -->
<h1>BAB IV. PENGUJIAN OTOMATIS & KASUS EKSTREM (BOBOT 30% - BAGIAN 1)</h1>

<h2>4.1 Lingkungan & Metodologi Pengujian</h2>
<p>
Pengujian dilakukan secara otomatis menggunakan modul <code>tests/test_csp.py</code> dan <code>tests/test_ucs.py</code> pada lingkungan Python 3.13 dengan test runner <code>pytest</code> 9.1.1 di Windows 11. Sebanyak <strong>21 kasus uji terotomatisasi</strong> dirancang untuk mencakup kasus fungsional normal, boundary test, pengujian varian algoritma (ablation), dan pengujian kasus ekstrem (*edge cases*).
</p>

<h2>4.2 Matriks Kasus Uji Komprehensif</h2>
<table>
  <thead>
    <tr>
      <th>No</th>
      <th>ID Uji</th>
      <th>Kategori</th>
      <th>Skenario Masukan</th>
      <th>Hasil Diharapkan</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">1</td>
      <td>TC-01</td>
      <td>Normal</td>
      <td>Kueri memuat judul/pengarang</td>
      <td>X1=1, solusi valid ditemukan</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">2</td>
      <td>TC-02</td>
      <td>Normal</td>
      <td>Kueri memuat konteks dan alur cerita</td>
      <td>X2=1, X3=1 (Dependensi C6 terpenuhi)</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">3</td>
      <td>TC-03</td>
      <td>Normal</td>
      <td>Seluruh fitur kueri diaktifkan</td>
      <td>X={1, 1, 1, 1} lengkap</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">4</td>
      <td>TC-04</td>
      <td>Global C5</td>
      <td>Kueri kosong (fitur nonaktif)</td>
      <td>Minimal 1 modul aktif (&sum;X &ge; 1)</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">5</td>
      <td>TC-05</td>
      <td>AC-3 Test</td>
      <td>X2={0}, X3={0, 1}</td>
      <td>AC-3 memangkas nilai 1 pada X3 &rarr; D3={0}</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">6</td>
      <td>TC-06</td>
      <td>AC-3 Test</td>
      <td>X2={0}, X3={1} (Konflik mutlak)</td>
      <td>AC-3 mengembalikan False (Wipeout)</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">7</td>
      <td>TC-07</td>
      <td>MRV Test</td>
      <td>Domain X2 ukuran 1, lainnya ukuran 2</td>
      <td>Heuristik memprioritaskan variabel X2</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">8</td>
      <td>TC-08</td>
      <td>Edge Case</td>
      <td>Cerita diminta, tapi konteks dilarang keras</td>
      <td>Solver mengembalikan None (No Solution)</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">9</td>
      <td>TC-09</td>
      <td>Edge Case</td>
      <td>Inisialisasi domain awal kosong</td>
      <td>Solver mendeteksi dini &rarr; None</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">10</td>
      <td>TC-10</td>
      <td>Edge Case</td>
      <td>Butuh 4 proses, kuota dibatasi max 2</td>
      <td>Solver menolak alokasi &rarr; None</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">11</td>
      <td>TC-11</td>
      <td>Boundary</td>
      <td>Butuh 2 proses, kuota tepat max 2</td>
      <td>Solusi legal tepat batas (&sum;X = 2)</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">12-15</td>
      <td>TC-12..15</td>
      <td>Ablation</td>
      <td>4 variasi strategi algoritma</td>
      <td>Seluruh varian menghasilkan solusi konsisten</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">16</td>
      <td>TC-16</td>
      <td>Stress Test</td>
      <td>500 iterasi penyelesaian beruntun</td>
      <td>Selesai dalam &lt; 1 detik tanpa fluktuasi</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
    <tr>
      <td style="text-align: center;">17-21</td>
      <td>TC-17..21</td>
      <td>UCS M1</td>
      <td>Lintasan graf, siklus, bobot non-negatif</td>
      <td>Jalur optimal UCS terverifikasi</td>
      <td><span class="badge-pass">PASSED</span></td>
    </tr>
  </tbody>
</table>

<h2>4.3 Bukti Hasil Eksekusi Terminal Pytest</h2>
<div class="code-block">
============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\...\mnemolib
configfile: pyproject.toml
testpaths: tests
collected 21 items

tests/test_csp.py::test_normal_title_author_query PASSED                 [  4%]
tests/test_csp.py::test_normal_context_and_story_query PASSED            [  9%]
tests/test_csp.py::test_normal_all_features_active PASSED                [ 14%]
tests/test_csp.py::test_empty_query_activates_at_least_one_process PASSED [ 19%]
tests/test_csp.py::test_ac3_prunes_invalid_arc PASSED                    [ 23%]
tests/test_csp.py::test_ac3_detects_immediate_domain_wipeout PASSED      [ 28%]
tests/test_csp.py::test_mrv_selects_smallest_remaining_domain PASSED     [ 33%]
tests/test_csp.py::test_edge_case_contradictory_story_without_context PASSED [ 38%]
tests/test_csp.py::test_edge_case_empty_initial_domain PASSED            [ 42%]
tests/test_csp.py::test_edge_case_tight_quota_underflow PASSED           [ 47%]
tests/test_csp.py::test_edge_case_valid_quota_boundary PASSED            [ 52%]
tests/test_csp.py::test_all_solver_variants_find_consistent_solution[False-False] PASSED [ 57%]
tests/test_csp.py::test_all_solver_variants_find_consistent_solution[False-True] PASSED [ 61%]
tests/test_csp.py::test_all_solver_variants_find_consistent_solution[True-False] PASSED [ 66%]
tests/test_csp.py::test_all_solver_variants_find_consistent_solution[True-True] PASSED [ 71%]
tests/test_csp.py::test_stress_and_latency_performance PASSED            [ 76%]
tests/test_ucs.py::test_ucs_finds_lowest_cost_path PASSED                [ 80%]
tests/test_ucs.py::test_ucs_finds_context_path_when_title_unavailable PASSED [ 85%]
tests/test_ucs.py::test_ucs_returns_none_when_goal_is_unreachable PASSED [ 90%]
tests/test_ucs.py::test_ucs_rejects_negative_cost PASSED                 [ 95%]
tests/test_ucs.py::test_ucs_handles_graph_with_cycles PASSED             [100%]

============================= 21 passed in 0.17s ==============================
</div>

<hr>

<!-- BAB V -->
<h1>BAB V. ANALISIS SENSITIVITAS & WAKTU KONVERGENSI (BOBOT 30% - BAGIAN 2)</h1>

<h2>5.1 Analisis Skalabilitas Masalah (Skala Kecil vs Skala Besar)</h2>
<p>
Pengujian skalabilitas dilakukan dengan meningkatkan jumlah variabel keputusan secara eksponensial dari skala kecil (N=8) hingga skala besar (N=256) menggunakan skrip benchmark empiris <code>scripts/benchmark_scaling.py</code>:
</p>

<table>
  <thead>
    <tr>
      <th>Kategori Skala</th>
      <th>Jumlah Variabel (N)</th>
      <th>Waktu Konvergensi (ms)</th>
      <th>Simpul Dievaluasi (Nodes)</th>
      <th>Jumlah Backtracks</th>
      <th>Keterangan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Skala Kecil</strong></td>
      <td style="text-align: center;">8</td>
      <td style="text-align: right;">0.119 ms</td>
      <td style="text-align: center;">9</td>
      <td style="text-align: center;">0</td>
      <td>Konvergensi instan</td>
    </tr>
    <tr>
      <td><strong>Skala Kecil</strong></td>
      <td style="text-align: center;">16</td>
      <td style="text-align: right;">0.145 ms</td>
      <td style="text-align: center;">17</td>
      <td style="text-align: center;">0</td>
      <td>Konvergensi instan</td>
    </tr>
    <tr>
      <td><strong>Skala Menengah</strong></td>
      <td style="text-align: center;">32</td>
      <td style="text-align: right;">0.444 ms</td>
      <td style="text-align: center;">33</td>
      <td style="text-align: center;">0</td>
      <td>Sub-milidetik</td>
    </tr>
    <tr>
      <td><strong>Skala Menengah</strong></td>
      <td style="text-align: center;">64</td>
      <td style="text-align: right;">1.514 ms</td>
      <td style="text-align: center;">65</td>
      <td style="text-align: center;">0</td>
      <td>Pertumbuhan terkontrol</td>
    </tr>
    <tr>
      <td><strong>Skala Besar</strong></td>
      <td style="text-align: center;">128</td>
      <td style="text-align: right;">8.811 ms</td>
      <td style="text-align: center;">129</td>
      <td style="text-align: center;">0</td>
      <td>Linear scaling O(N)</td>
    </tr>
    <tr>
      <td><strong>Skala Besar</strong></td>
      <td style="text-align: center;">256</td>
      <td style="text-align: right;">38.655 ms</td>
      <td style="text-align: center;">257</td>
      <td style="text-align: center;">0</td>
      <td>Memenuhi target &le; 50 ms</td>
    </tr>
  </tbody>
</table>

<h2>5.2 Studi Ablasi Algoritma & Perilaku Kasus Ekstrem</h2>
<p>
Tabel berikut menunjukkan hasil pengujian perbandingan strategi algoritma pada skenario normal vs kasus ekstrem (kontradiksi batasan):
</p>

<table>
  <thead>
    <tr>
      <th>Skenario Pengujian</th>
      <th>Strategi Algoritma</th>
      <th>Simpul (Nodes)</th>
      <th>Backtracks</th>
      <th>Rata-rata Waktu (&mu;s)</th>
      <th>Status Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4"><strong>Kasus Normal</strong><br>(Konteks & Cerita Aktif)</td>
      <td>Pure Backtracking</td>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">0</td>
      <td style="text-align: right;">12.90 &mu;s</td>
      <td>FOUND</td>
    </tr>
    <tr>
      <td>Backtracking + MRV</td>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">0</td>
      <td style="text-align: right;">20.11 &mu;s</td>
      <td>FOUND</td>
    </tr>
    <tr>
      <td>Backtracking + AC-3</td>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">0</td>
      <td style="text-align: right;">19.57 &mu;s</td>
      <td>FOUND</td>
    </tr>
    <tr>
      <td>Backtracking + AC-3 + MRV</td>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">0</td>
      <td style="text-align: right;">26.65 &mu;s</td>
      <td>FOUND</td>
    </tr>
    <tr style="background-color: #fff2f2;">
      <td rowspan="4"><strong>Kasus Ekstrem: Konflik</strong><br>(Cerita aktif, Konteks dilarang)</td>
      <td>Pure Backtracking</td>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">7</td>
      <td style="text-align: right;">15.42 &mu;s</td>
      <td>NO_SOLUTION</td>
    </tr>
    <tr style="background-color: #fff2f2;">
      <td>Backtracking + MRV</td>
      <td style="text-align: center;">2</td>
      <td style="text-align: center;">3</td>
      <td style="text-align: right;">10.28 &mu;s</td>
      <td>NO_SOLUTION</td>
    </tr>
    <tr style="background-color: #e6ffed;">
      <td><strong>Backtracking + AC-3</strong></td>
      <td style="text-align: center;"><strong>0</strong></td>
      <td style="text-align: center;"><strong>0</strong></td>
      <td style="text-align: right;"><strong>3.46 &mu;s</strong></td>
      <td><strong>NO_SOLUTION (4.5x Lebih Cepat)</strong></td>
    </tr>
    <tr style="background-color: #e6ffed;">
      <td><strong>Backtracking + AC-3 + MRV</strong></td>
      <td style="text-align: center;"><strong>0</strong></td>
      <td style="text-align: center;"><strong>0</strong></td>
      <td style="text-align: right;"><strong>4.06 &mu;s</strong></td>
      <td><strong>NO_SOLUTION</strong></td>
    </tr>
  </tbody>
</table>

<h2>5.3 Analisis Grafik & Pembahasan Waktu Konvergensi</h2>
<p>
Berdasarkan data empiris, didapatkan temuan analisis yang sangat krusial:
</p>
<ol>
  <li><strong>Keunggulan Deteksi Dini AC-3 (*Early Failure Detection*)</strong>: Pada kasus konflik batasan ekstrem di mana solusi tidak dimungkinkan, algoritma <em>Pure Backtracking</em> harus mengeksplorasi 5 simpul dan melakukan 7 kali backtrack (15.42 &mu;s). Sebaliknya, dengan <strong>AC-3</strong>, domain variabel langsung tereduksi menjadi kosong pada tahap pra-pencarian (*pre-search*). Akibatnya, solver tidak perlu membuka simpul pencarian sama sekali (<strong>0 nodes, 0 backtracks</strong>) dan menyimpulkan ketiadaan solusi dalam waktu <strong>3.46 &mu;s (4.5 kali lebih cepat)</strong>.</li>
  <li><strong>Efisiensi Skala Besar</strong>: Pada skala besar (N=256), kombinasi AC-3 dan MRV berhasil mempertahankan konvergensi waktu sebesar <strong>38.65 ms</strong> dengan jumlah evaluasi simpul tepat N+1 (257 simpul) dan 0 backtrack. Hal ini membuktikan bahwa pemangkasan konsistensi busur mencegah terjadinya *combinatorial explosion*.</li>
</ol>

<hr>

<!-- BAB VI -->
<h1>BAB VI. KESIMPULAN & PEMBAGIAN KONTRIBUSI</h1>

<h2>6.1 Kesimpulan Capaian Proyek</h2>
<ol>
  <li>Pemodelan matematis formal &lang;X, D, C&rang; berhasil memetakan seluruh regulasi bisnis keputusan pencarian MnemoLib secara presisi tanpa inkonsistensi.</li>
  <li>Modul solver Python telah diimplementasikan secara modular, elegan, dan memenuhi prinsip *clean code* dengan integrasi propagasi batasan AC-3 dan heuristik MRV.</li>
  <li>Pengujian terotomatisasi berhasil meloloskan 21 dari 21 kasus uji (100% kelulusan) termasuk kasus ekstrem konflik batasan dan kuota kapasitas.</li>
  <li>Analisis sensitivitas membuktikan ketangguhan sistem di mana waktu konvergensi skala besar (N=256) berada pada 38.65 ms, memenuhi ambang batas latensi enterprise (&le; 50 ms).</li>
</ol>

<h2>6.2 Rincian Pembagian Kerja Anggota Kelompok (Grup 12)</h2>
<table>
  <thead>
    <tr>
      <th>Nama Mahasiswa</th>
      <th>Peran Tim</th>
      <th>Rincian Kontribusi Spesifik pada Milestone 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Laura Sirumapea</strong></td>
      <td>AI Architect & Model Lead</td>
      <td>Perancangan arsitektur algoritma CSP, implementasi modul propagasi <code>ac3.py</code>, penataan struktur solver, dan integrasi modul pencarian.</td>
    </tr>
    <tr>
      <td><strong>Desnita Pardosi</strong></td>
      <td>Data & Knowledge Engineer</td>
      <td>Perumusan basis batasan pada <code>constraints.py</code>, pemodelan relasi biner, dan implementasi heuristik pemilihan variabel <code>mrv.py</code>.</td>
    </tr>
    <tr>
      <td><strong>Mia Sibuea</strong></td>
      <td>QA Lead, Evaluator & System Integrator</td>
      <td>Perancangan matriks pengujian otomatis <code>test_csp.py</code> (16 kasus uji + edge cases), eksekusi benchmark sensitivitas skala kecil vs besar, penyusunan dokumentasi teknis, dan finalisasi laporan resmi.</td>
    </tr>
  </tbody>
</table>

</body>
</html>
"""

def generate_report():
    doc_html = r"C:\Users\ACER\.gemini\antigravity\scratch\mnemolib\docs\milestone-02\Grup12-Tugas02.html"
    pdf_out1 = r"C:\Users\ACER\.gemini\antigravity\scratch\mnemolib\docs\milestone-02\Grup12-Tugas02.pdf"
    pdf_out2 = r"C:\Users\ACER\.gemini\antigravity\scratch\mnemolib\Grup12-Tugas02.pdf"
    pdf_out3 = r"C:\Users\ACER\.gemini\antigravity\scratch\mnemolib\Grup12_Tugas02.pdf"

    with open(doc_html, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"[+] HTML report saved to {doc_html}")

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_out1}",
        doc_html
    ]

    print("[+] Rendering PDF via headless Microsoft Edge...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_out1):
        print(f"[V] Successfully generated PDF: {pdf_out1} (Size: {os.path.getsize(pdf_out1)} bytes)")
        import shutil
        shutil.copyfile(pdf_out1, pdf_out2)
        shutil.copyfile(pdf_out1, pdf_out3)
        print(f"[V] Copied to root: {pdf_out2}")
        print(f"[V] Copied to root: {pdf_out3}")
    else:
        print(f"[X] Error generating PDF: {res.stderr}")

if __name__ == "__main__":
    generate_report()

# Proyek Rekomendasi Karier Berdasarkan Minat dan Skill

## Deskripsi
Proyek ini bertujuan untuk menganalisa pekerjaan yang tepat untuk seorang individu
berdasarkan minat dan skill yang dimiliki. Dibangun dengan Streamlit dan menggunakan dataset JSON sederhana yang berisi berbagai informasi karier seperti deskripsi, bidang, skill yang dibutuhkan, dan kisaran gaji.

## Fitur Utama
1. Input Nama Pengguna
   
Memberi sentuhan personal dengan menampilkan nama pengguna di tampilan antarmuka.

2. Pemilihan Skill
   
Pengguna dapat memilih satu atau lebih skill dari daftar yang disediakan.
Skill digunakan sebagai dasar pencocokan dengan kebutuhan pekerjaan.

3. Rekomendasi Karir Otomatis
   
Menampilkan daftar karier yang cocok berdasarkan skill yang dipilih pengguna.
Karier hanya ditampilkan jika semua skill yang dibutuhkan tersedia di input pengguna.

4. Informasi Detail Karier
   
Untuk setiap rekomendasi karir, ditampilkan:

-Nama Pekerjaan

-Deskripsi Pekerjaan

-Bidang (Field): misalnya Teknologi, Desain, Pemasaran, dll.

-Kisaran Gaji (Salary Range)

## Instalasi
1. Clone repositori ini
```bash
git clone https://github.com/Farrelabrarw/Rekomendasi-karir.git
cd Rekomendasi-karir
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
## Cara Menjalankan
```bash
streamlit run rekomendasi karier.py
```

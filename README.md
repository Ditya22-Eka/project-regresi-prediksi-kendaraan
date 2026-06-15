# Prediksi Jumlah Kendaraan Bermotor di Sulawesi Tengah Menggunakan Regresi Linear dan Support Vector Classification

Repositori ini berisi implementasi proyek komputasi *Machine Learning* untuk menganalisis dan memprediksi jumlah kendaraan bermotor di kabupaten/kota Provinsi Sulawesi Tengah. Proyek ini menggunakan bahasa pemrograman Python dengan menerapkan metode Regresi Linear untuk memprediksi jumlah kendaraan, serta Support Vector Classification (SVC) untuk mengklasifikasikan kategori jumlah kendaraan.

Proyek ini disusun sebagai bagian dari pemenuhan tugas mata kuliah Statistik dan Probabilitas.

## 🔎 Latar Belakang Studi

Jumlah kendaraan bermotor di suatu wilayah dapat mengalami perubahan dari tahun ke tahun seiring dengan pertumbuhan penduduk, perkembangan ekonomi, kebutuhan transportasi, dan aktivitas masyarakat. Provinsi Sulawesi Tengah memiliki beberapa kabupaten/kota dengan jumlah kendaraan yang berbeda-beda, sehingga diperlukan analisis data untuk melihat pola perkembangan kendaraan bermotor di setiap wilayah.

Melalui proyek ini, data jumlah kendaraan bermotor tahun 2022 sampai 2025 digunakan untuk membangun model prediksi tahun 2026. Metode Regresi Linear digunakan untuk memperkirakan jumlah kendaraan berdasarkan jenis kendaraan, sedangkan Support Vector Classification digunakan untuk mengelompokkan hasil prediksi ke dalam kategori tertentu, yaitu Rendah, Sedang, dan Tinggi.

## 🗂️ Sumber Data

Dataset yang digunakan berasal dari sumber resmi Badan Pusat Statistik (BPS) Provinsi Sulawesi Tengah, dengan data jumlah kendaraan bermotor menurut kabupaten/kota dan jenis kendaraan di Provinsi Sulawesi Tengah.

Data yang digunakan mencakup tahun:

* 2022
* 2023
* 2024
* 2025

Data tahun 2025 digunakan sebagai data sementara sesuai dengan ketersediaan data dari sumber resmi.

## 🧩 Fitur Dataset

Dataset yang digunakan memiliki beberapa kolom utama, yaitu:

* `tahun`
* `kabupaten_kota`
* `mobil_penumpang`
* `bus`
* `truk`
* `sepeda_motor`
* `jumlah_kendaraan`
* `status_data`
* `kategori_jumlah_kendaraan`

Kolom `kategori_jumlah_kendaraan` merupakan hasil pengolahan dari jumlah kendaraan untuk kebutuhan metode klasifikasi menggunakan SVC. Kategori yang digunakan adalah Rendah, Sedang, dan Tinggi.

## 🔄 Alur Kerja Machine Learning

Sistem prediksi dalam repositori ini dibangun melalui beberapa tahapan sebagai berikut:

1. **Import Library**
   Menggunakan library Python seperti Pandas, NumPy, Matplotlib, dan Scikit-Learn.

2. **Membaca Dataset**
   Dataset dibaca dari file Excel menggunakan Pandas.

3. **Membersihkan Data Kosong**
   Data yang tidak tersedia tetap disimpan pada dataset asli, tetapi tidak digunakan dalam proses pelatihan model agar hasil prediksi tidak dipengaruhi oleh data kosong.

4. **Encoding Data Kategori**
   Nama kabupaten/kota diubah menjadi bentuk angka menggunakan LabelEncoder agar dapat diproses oleh model *Machine Learning*.

5. **Menentukan Fitur dan Target**
   Fitur yang digunakan adalah tahun dan kode kabupaten/kota. Target yang diprediksi adalah jumlah kendaraan berdasarkan jenis kendaraan, yaitu mobil penumpang, bus, truk, dan sepeda motor.

6. **Model Regresi Linear**
   Regresi Linear digunakan untuk memprediksi jumlah kendaraan tahun 2026 pada setiap jenis kendaraan.

7. **Prediksi Total Kendaraan**
   Hasil prediksi dari setiap jenis kendaraan dijumlahkan untuk menghasilkan total prediksi kendaraan tahun 2026.

8. **Model Support Vector Classification**
   SVC digunakan untuk memprediksi kategori jumlah kendaraan berdasarkan hasil prediksi total kendaraan.

9. **Evaluasi Model**
   Model Regresi Linear dievaluasi menggunakan MAE, MSE, RMSE, dan R2 Score. Model SVC dievaluasi menggunakan akurasi dan classification report.

10. **Visualisasi Data**
    Hasil prediksi divisualisasikan dalam bentuk grafik batang berdasarkan kabupaten/kota dan jenis kendaraan.

11. **Menyimpan Hasil Prediksi**
    Hasil prediksi dan evaluasi model disimpan ke dalam file Excel.

# 1. IMPORT LIBRARY

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    accuracy_score,
    classification_report
)

# 2. MEMBACA DATASET EXCEL

# Mengambil lokasi folder tempat file Python berada
folder_project = Path(__file__).parent

# Nama file dataset Excel
file_dataset = folder_project / "DATASET_KENDARAAN_BERMOTOR_SULTENG_2022_2025.xlsx"

# Membaca daftar sheet dalam file Excel
excel_file = pd.ExcelFile(file_dataset)

print("Daftar sheet dalam file Excel:")
print(excel_file.sheet_names)

# Membaca sheet Dataset_Model
data = pd.read_excel(file_dataset, sheet_name="Dataset_Model")

print("\n5 data pertama:")
print(data.head())

print("\nInformasi dataset:")
print(data.info())

# 3. MEMBERSIHKAN DATA KOSONG

# Menyimpan data asli, termasuk data yang kosong
data_asli = data.copy()

# Data untuk model hanya memakai baris yang jumlah kendaraannya tersedia
data_model = data.dropna(subset=["jumlah_kendaraan"])

# Menghapus baris kategori Tidak Tersedia jika ada
data_model = data_model[data_model["kategori_jumlah_kendaraan"] != "Tidak Tersedia"]

print("\nJumlah data asli:", len(data_asli))
print("Jumlah data yang digunakan untuk model:", len(data_model))

print("\nData yang siap digunakan untuk model:")
print(data_model.head())

# 4. ENCODING DATA KATEGORI

# Mengubah nama kabupaten/kota menjadi angka
encoder_kota = LabelEncoder()
data_model["kabupaten_kota_kode"] = encoder_kota.fit_transform(data_model["kabupaten_kota"])

# Mengubah kategori kendaraan menjadi angka
encoder_kategori = LabelEncoder()
data_model["kategori_kode"] = encoder_kategori.fit_transform(
    data_model["kategori_jumlah_kendaraan"]
)

print("\nDaftar kode kabupaten/kota:")
for nama, kode in zip(encoder_kota.classes_, encoder_kota.transform(encoder_kota.classes_)):
    print(kode, "=", nama)

print("\nDaftar kode kategori:")
for nama, kode in zip(encoder_kategori.classes_, encoder_kategori.transform(encoder_kategori.classes_)):
    print(kode, "=", nama)

# 5. MENENTUKAN FITUR DAN TARGET

# Fitur utama untuk memprediksi setiap jenis kendaraan
fitur = ["tahun", "kabupaten_kota_kode"]

# Target yang akan diprediksi satu per satu
target_jenis_kendaraan = [
    "mobil_penumpang",
    "bus",
    "truk",
    "sepeda_motor"
]
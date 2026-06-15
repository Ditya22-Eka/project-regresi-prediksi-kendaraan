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

# 6. MODEL REGRESI LINEAR UNTUK SETIAP JENIS KENDARAAN

print("\n==============================")
print("MODEL REGRESI LINEAR")
print("==============================")

model_regresi_jenis = {}
evaluasi_regresi = []

for target in target_jenis_kendaraan:
    print(f"\nPrediksi untuk: {target}")

    # Mengambil data yang tidak kosong pada target tersebut
    data_target = data_model.dropna(subset=[target])

    X = data_target[fitur]
    y = data_target[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("MAE  :", mae)
    print("MSE  :", mse)
    print("RMSE :", rmse)
    print("R2   :", r2)

    model_regresi_jenis[target] = model

    evaluasi_regresi.append({
        "jenis_kendaraan": target,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2
    })

    # 7. MEMBUAT DATA PREDIKSI TAHUN 2026

daftar_kota = data_model["kabupaten_kota"].unique()

data_2026 = pd.DataFrame({
    "tahun": [2026] * len(daftar_kota),
    "kabupaten_kota": daftar_kota
})

data_2026["kabupaten_kota_kode"] = encoder_kota.transform(
    data_2026["kabupaten_kota"]
)

X_2026 = data_2026[fitur]

# 8. PREDIKSI SETIAP JENIS KENDARAAN TAHUN 2026

for target in target_jenis_kendaraan:
    kolom_prediksi = "prediksi_" + target

    data_2026[kolom_prediksi] = model_regresi_jenis[target].predict(X_2026)

    data_2026[kolom_prediksi] = np.round(
        data_2026[kolom_prediksi]
    ).astype(int)

    data_2026[kolom_prediksi] = data_2026[kolom_prediksi].clip(lower=0)

    # Menghitung total prediksi kendaraan dari semua jenis kendaraan
data_2026["prediksi_jumlah_kendaraan_2026"] = (
    data_2026["prediksi_mobil_penumpang"] +
    data_2026["prediksi_bus"] +
    data_2026["prediksi_truk"] +
    data_2026["prediksi_sepeda_motor"]
)

# 9. MODEL SUPPORT VECTOR CLASSIFICATION

print("\n==============================")
print("MODEL SUPPORT VECTOR CLASSIFICATION")
print("==============================")

# Untuk SVC, fitur yang digunakan adalah tahun, kode wilayah, dan jumlah kendaraan
fitur_svc = ["tahun", "kabupaten_kota_kode", "jumlah_kendaraan"]

X_svc = data_model[fitur_svc]
y_svc = data_model["kategori_kode"]

X_train_svc, X_test_svc, y_train_svc, y_test_svc = train_test_split(
    X_svc,
    y_svc,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train_svc_scaled = scaler.fit_transform(X_train_svc)
X_test_svc_scaled = scaler.transform(X_test_svc)

model_svc = SVC(kernel="rbf", C=1.0, gamma="scale")
model_svc.fit(X_train_svc_scaled, y_train_svc)

y_pred_svc = model_svc.predict(X_test_svc_scaled)

akurasi = accuracy_score(y_test_svc, y_pred_svc)

print("Akurasi SVC:", akurasi)

print("\nClassification Report:")
print(
    classification_report(
        y_test_svc,
        y_pred_svc,
        target_names=encoder_kategori.classes_
    )
)
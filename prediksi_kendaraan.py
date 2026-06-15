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
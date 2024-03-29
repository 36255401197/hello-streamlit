import pandas as pd
import matplotlib.pyplot as plt

# Fungsi Moora
def moora(data, weights):
    # Normalisasi data
    normalized = data / data.max(axis=0)
    
    # Hitung nilai tertimbang
    weighted = normalized * weights
    
    # Hitung nilai total untuk setiap alternatif
    weighted['Total'] = weighted.sum(axis=1)
    
    return weighted

# Contoh data alternatif (dalam hal ini, kolom mewakili kriteria dan baris mewakili alternatif)
data = pd.DataFrame({
    'Kriteria_1': [3, 4, 5],
    'Kriteria_2': [2, 3, 4],
    'Kriteria_3': [5, 2, 1]
})

# Bobot untuk setiap kriteria
weights = pd.Series([0.4, 0.3, 0.3], index=['Kriteria_1', 'Kriteria_2', 'Kriteria_3'])

# Memanggil fungsi Moora untuk menghitung total
result = moora(data, weights)

# Menampilkan hasil
print("Hasil Metode Moora:")
print(result)

# Visualisasi hasil Moora
plt.figure(figsize=(8, 5))
result['Total'].plot(kind='bar', color='skyblue')
plt.title('Total Nilai Moora untuk Setiap Alternatif')
plt.xlabel('Alternatif')
plt.ylabel('Total Nilai Moora')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

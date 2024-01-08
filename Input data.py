import pandas as pd

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
print

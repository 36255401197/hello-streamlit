import streamlit as st
import numpy as np
import pandas as pd

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

criteria_labels = np.array(['Pengalaman', 'Pendidikan', 'Usia', 'Status Perkawinan', 'Alamat'])
weights = np.array([0.3, 0.5, 0.9, 0.1, 0.8])

def click_button():
    st.session_state.clicked = True

def sample_norm(values, criteria_labels):
    norm_values = []
    for val in values:
        normalized_val = []
        for i in range(len(val)):
            if criteria_labels[i] in ['Pengalaman', 'Pendidikan', 'Usia']:
                norm = val[i] / 6  # Mengubah rentang 2-6 menjadi 0-2
            elif criteria_labels[i] == 'Status Perkawinan':
                norm = val[i]  # Asumsi nilai 0 atau 2
            else:
                norm = val[i] / 10  # Mengubah rentang 1-10 menjadi 0-2
            
            normalized_val.append(norm)
        
        norm_values.append(normalized_val)
    
    return norm_values


def calculate_topsis(values, weights):
    normalized = sample_norm(values, criteria_labels)
    weighted_normalized = normalized * weights
    ideal_positive = np.max(weighted_normalized, axis=0)
    ideal_negative = np.min(weighted_normalized, axis=0)
    
    # Tambahkan nilai kecil ke ideal agar hasil TOPSIS tidak sama
    ideal_positive += 0.0001 
    ideal_negative -= 0.0001 
    
    distance_positive = np.sqrt(np.sum((weighted_normalized - ideal_positive) ** 2, axis=1))
    distance_negative = np.sqrt(np.sum((weighted_normalized - ideal_negative) ** 2, axis=1))
    closeness = distance_negative / (distance_positive + distance_negative)
    return closeness

def run():
    st.set_page_config(
        page_title="Implementasi TOPSIS",
        page_icon="📊",
    )

    st.write("# Implementasi Metode TOPSIS")
    st.write("Studi Kasus: Rekrutmen Calon Pekerja untuk Operator Mesin")

    st.markdown(
        """
        Metode Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) digunakan untuk mengambil keputusan dengan memilih alternatif yang memiliki kedekatan terbaik dengan solusi ideal positif dan kedekatan terburuk dengan solusi ideal negatif. 
        """
    )

    st.divider()

    st.write("## Input Nilai Kriteria")

    max_data = 6  # Jumlah data maksimal
    min_data = 2  # Jumlah data minimal
    input_data = []

    for i in range(len(criteria_labels)):
        label = criteria_labels[i]
        value = st.slider(f"{label}", min_value=1, max_value=10, value=5, step=1) / 10  # Mengubah rentang slider
        input_data.append(value)

    if st.button("Simpan", type='primary', on_click=click_button):
        simpanData(input_data, max_data, min_data)
    
    if st.session_state.clicked:
        data = st.session_state.nilai_kriteria
        if len(data) < min_data or len(data) > max_data:
            st.error(f"Input minimal {min_data} data dan maksimal {max_data} data untuk diproses.")
        else:
            df = pd.DataFrame(data, columns=criteria_labels)
            st.dataframe(df)

            if st.button("Proses"):
                prosesData()


def simpanData(input_data, max_data, min_data):
    if 'nilai_kriteria' not in st.session_state:
        st.session_state.nilai_kriteria = np.array([input_data])
    else:
        dataLama = st.session_state.nilai_kriteria
        if len(dataLama) < max_data:
            dataBaru = np.append(dataLama, [input_data], axis=0)
            st.session_state.nilai_kriteria = dataBaru

def prosesData():
    A = st.session_state.nilai_kriteria

    topsis_result = calculate_topsis(A, weights)
    rankings = np.argsort(topsis_result)[::-1]

    st.write("Perankingan Calon Pekerja:")
    for i, rank in enumerate(rankings, start=1):
        st.write(f"Rank {i}: Calon {rank + 1}")

if __name__ == "__main__":
    run()
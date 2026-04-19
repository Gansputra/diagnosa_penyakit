import streamlit as st
from conditional import diagnosa

# Judul Aplikasi
st.title("🩺 diagnosapenyakit")
st.write("Sistem pakar sederhana untuk diagnosa penyakit berdasarkan gejala.")

# Pilihan Gejala
gejala_list = [
    "Demam tinggi", "Batuk kering", "Sesak napas", "Sakit kepala", 
    "Nyeri otot", "Pilek", "Sakit tenggorokan", "Demam ringan", 
    "Kelelahan", "Lainnya"
]

gejala_user = st.multiselect("Pilih gejala yang Anda rasakan:", gejala_list)

# Tombol Diagnosa
if st.button("Mulai Diagnosa"):
    if not gejala_user:
        st.warning("Silakan pilih minimal satu gejala.")
    else:
        hasil = diagnosa(gejala_user)
        
        st.subheader("Hasil Analisis:")
        if hasil:
            for h in hasil:
                st.success(h)
        else:
            st.info("Gejala tidak spesifik. Silakan konsultasi ke dokter.")

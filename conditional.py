def diagnosa(gejala_user):
    hasil = []

    if all(g in gejala_user for g in ["Demam tinggi", "Batuk kering", "Sesak napas"]):
        hasil.append("COVID-19 (Segera lakukan tes PCR dan isolasi mandiri)")

    if all(g in gejala_user for g in ["Demam tinggi", "Sakit kepala", "Nyeri otot"]):
        hasil.append("Demam Berdarah (DBD) - Periksa kadar trombosit segera")

    if all(g in gejala_user for g in ["Pilek", "Sakit tenggorokan", "Batuk kering"]):
        hasil.append("Flu / Influenza (Disarankan istirahat dan minum vitamin)")

    if all(g in gejala_user for g in ["Sakit tenggorokan", "Demam ringan"]):
        hasil.append("Radang Tenggorokan (Hindari makanan berminyak)")

    if all(g in gejala_user for g in ["Nyeri otot", "Kelelahan", "Demam ringan"]):
        hasil.append("Kelelahan Fisik / Influenza Ringan")
    
    if not hasil and gejala_user:
        if "Sesak napas" in gejala_user:
            hasil.append("Gangguan Pernapasan (Segera hubungi layanan kesehatan)")
        
        if "Demam tinggi" in gejala_user:
            hasil.append("Demam Tinggi (Gunakan kompres dingin dan paracetamol)")

        if "Sakit kepala" in gejala_user:
            if "Kelelahan" in gejala_user:
                hasil.append("Sakit Kepala Akibat Kelelahan / Stress")
            else:
                hasil.append("Migrain atau Sakit Kepala Biasa")

        if "Nyeri otot" in gejala_user:
            hasil.append("Myalgia (Nyeri Otot) - Butuh relaksasi")

        if "Sakit tenggorokan" in gejala_user:
            hasil.append("Iritasi Tenggorokan / Gejala Awal Radang")

        if "Pilek" in gejala_user:
            hasil.append("Rhinitis / Pilek Biasa")

        if "Kelelahan" in gejala_user and not any("Sakit kepala" in gejala_user for g in ["Sakit kepala"]):
            hasil.append("Kelelahan Akut - Disarankan istirahat total")

        if "Demam ringan" in gejala_user:
            hasil.append("Gejala Meriang / Demam Ringan")

        if "Batuk kering" in gejala_user:
            hasil.append("Batuk Kering (Kemungkinan iritasi tenggorokan)")

    if not hasil and gejala_user:
        hasil.append("Gejala tidak spesifik. Hubungi tenaga medis untuk diagnosa lebih lanjut.")

    return hasil

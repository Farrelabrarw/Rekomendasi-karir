import streamlit as st
import json

# Load data karier dari file JSON
with open("careers.json", "r") as f:
    careers = json.load(f)

st.title("🔍 Aplikasi Rekomendasi Karir")

# 🔹 Form input nama
name = st.text_input("👤 Masukkan nama kamu:")

if name:
    st.write(f"Halo, **{name}**! Yuk cari tahu karier yang cocok buat kamu. 👇")

    # Ambil semua skill unik
    all_skills = sorted(set(skill for career in careers for skill in career["required_skills"]))

    # Tambahkan pilihan bidang
    all_fields = sorted(set(career["field"] for career in careers))
    selected_field = st.selectbox("📂 Pilih bidang yang kamu minati:", ["Semua"] + all_fields)

    # Form untuk memilih skill
    selected_skills = st.multiselect("✅ Pilih skill yang kamu miliki:", all_skills)

    # Fungsi untuk mencocokkan karir
    def recommend_careers(skills, field=None):
        recommended = []
        for career in careers:
            if field and field != "Semua" and career["field"] != field:
                continue
            matched = len(set(skills) & set(career["required_skills"]))
            if matched > 0:
                career["match_score"] = matched
                recommended.append(career)
        return sorted(recommended, key=lambda x: x["match_score"], reverse=True)

    # Tampilkan hasil rekomendasi
    if selected_skills:
        results = recommend_careers(selected_skills, selected_field)
        if results:
            st.subheader("📌 Karier yang cocok:")
            for job in results:
                st.markdown(f"### {job['title']}")
                st.write(f"**Bidang:** {job['field']}")
                st.write(f"**Deskripsi:** {job['description']}")
                st.write(f"**Skill yang dibutuhkan:** {', '.join(job['required_skills'])}")
                st.write(f"**Gaji:** Rp {job['salary_range']}")
                st.markdown("---")
        else:
            st.warning("Tidak ada karier yang cocok ditemukan.")
    else:
        st.info("Silakan pilih minimal satu skill untuk melihat rekomendasi.")
else:
    st.info("Masukkan namamu terlebih dahulu untuk memulai.")
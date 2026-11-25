# ==========================================================
# APLIKASI STREAMLIT
# ANALISIS DATA ONLINE RETAIL
# IMPLEMENTASI MODUL BAB 1 DAN BAB 2
# UNIVERSITAS PAMULANG - TEKNIK INFORMATIKA
# ==========================================================

import os
import json
import zipfile
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="Machine Learning - Online Retail | UNPAM",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# MEMBACA DATASET & LOGO
# ==========================================================

@st.cache_data
def load_data():
    if os.path.exists("Online Retail.csv"):
        try:
            return pd.read_csv("Online Retail.csv")
        except UnicodeDecodeError:
            return pd.read_csv("Online Retail.csv", encoding="ISO-8859-1")
    elif os.path.exists("Online Retail.zip"):
        with zipfile.ZipFile("Online Retail.zip", "r") as z:
            csv_files = [
                f for f in z.namelist()
                if f.lower().endswith(".csv") and not f.startswith("__MACOSX")
            ]
            if not csv_files:
                raise FileNotFoundError("Tidak ada file CSV di dalam Online Retail.zip")
            with z.open(csv_files[0]) as f:
                try:
                    return pd.read_csv(f)
                except UnicodeDecodeError:
                    f.seek(0)
                    return pd.read_csv(f, encoding="ISO-8859-1")
    else:
        raise FileNotFoundError("File Online Retail.zip maupun Online Retail.csv tidak ditemukan.")

def get_logo_unpam():
    for filename in ["logo_unpam.png", "logo_unpam.jpg", "logo_unpam.jpeg"]:
        if os.path.exists(filename):
            return filename
    return "https://placehold.co/250x250/003366/FFFFFF/png?text=LOGO+UNPAM"

try:
    df = load_data()
except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    st.info("Pastikan file Online Retail.zip berada dalam folder yang sama dengan main.py.")
    st.stop()

logo_unpam = get_logo_unpam()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:
    col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
    with col_s2:
        st.image(logo_unpam, width=110)

    st.markdown(
        "<h3 style='text-align: center; margin-bottom: 0;'>UNIVERSITAS PAMULANG</h3>"
        "<p style='text-align: center; font-size: 13px; color: gray;'>Teknik Informatika • Machine Learning</p>",
        unsafe_allow_html=True
    )
    st.divider()

    st.title("🤖 Menu Aplikasi")
    menu = st.radio(
        "Pilih Materi:",
        [
            "Beranda",
            "Data dan Statistik",
            "Visualisasi Grafik",
            "Komponen Input",
            "Media",
            "Layout Streamlit",
            "Form dan Kontrol"
        ]
    )

    st.divider()
    st.caption("Implementasi Streamlit Bab 1–2")
    st.caption("Dataset: Online Retail.csv")

# ==========================================================
# BERANDA
# ==========================================================

if menu == "Beranda":

    col_logo, col_judul = st.columns([1, 5], vertical_alignment="center")

    with col_logo:
        st.image(logo_unpam, width=130)

    with col_judul:
        st.title("🤖 MACHINE LEARNING")
        st.header("Analisis Data Online Retail")
        st.subheader("Implementasi Framework Streamlit — Universitas Pamulang")

    st.divider()

    # Identitas Kelompok
    with st.container(border=True):
        st.markdown("### 👥 Identitas Kelompok")
        col_anggota, col_info = st.columns([3, 2])

        with col_anggota:
            st.markdown("""
            **Anggota Kelompok:**
1. **Dharma Putranto** — `241011402572`
2. **Ghauri Zaki Alfatih** — `24101140062`
3. **Muhammad Nizar Citra Wijaya** — `241011402192`

                     Dosen Pengampu: Farizi Ilham, M.Kom.
            """)

        with col_info:
            st.markdown("""
            **Informasi Akademik:**
- **Institusi:** Universitas Pamulang (UNPAM)
- **Program Studi:** Teknik Informatika (S1)
- **Mata Kuliah:** Machine Learning
- **Materi:** Implementasi Streamlit Bab 1 & 2
            """)

    st.write(
        "Aplikasi ini dibuat untuk mempraktikkan "
        "materi Streamlit pada Bab 1 dan Bab 2 menggunakan dataset Online Retail."
    )

    st.markdown("""
    ### 🎯 Tujuan Aplikasi
- Menampilkan dataset Online Retail.
- Menampilkan informasi dan statistik data.
- Membuat visualisasi data.
- Menerapkan komponen interaktif Streamlit.
- Mempelajari layout dan form aplikasi.
    """)

    st.caption("Praktik Machine Learning menggunakan Python.")

    st.code("st.title('Analisis Data Online Retail')")

    st.latex(r"Total\ Penjualan = Quantity \times UnitPrice")

    st.divider()

    st.success("Aplikasi Streamlit berhasil dijalankan!")

    st.info("Silakan pilih materi melalui menu di sebelah kiri.")

    st.metric("Jumlah Data", f"{len(df):,}")

# ==========================================================
# DATA DAN STATISTIK
# ==========================================================

elif menu == "Data dan Statistik":

    st.title("📊 Data dan Statistik Online Retail")

    st.header("Preview Dataset")

    st.write("Berikut adalah beberapa baris pertama dataset.")

    jumlah_baris = st.slider(
        "Jumlah baris yang ditampilkan",
        min_value=5,
        max_value=50,
        value=10
    )

    st.dataframe(df.head(jumlah_baris), use_container_width=True)

    st.subheader("Tampilan Tabel")

    st.table(df.head(5))

    st.subheader("Informasi Statistik")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Baris", f"{len(df):,}")

    with col2:
        st.metric("Total Kolom", len(df.columns))

    with col3:
        st.metric("Jumlah Data Kosong", int(df.isnull().sum().sum()))

    st.subheader("Informasi Dataset")

    st.write(df.describe(include="all"))

    st.subheader("Struktur Data dalam JSON")

    st.json({
        "jumlah_baris": int(len(df)),
        "jumlah_kolom": int(len(df.columns)),
        "nama_kolom": list(df.columns)
    })

# ==========================================================
# VISUALISASI GRAFIK
# ==========================================================

elif menu == "Visualisasi Grafik":

    st.title("📈 Visualisasi Data")

    st.write("Visualisasi dilakukan menggunakan data Online Retail.")

    st.subheader("Grafik Jumlah Transaksi per Negara")

    if "Country" in df.columns:
        negara = df["Country"].value_counts().head(10)
        st.bar_chart(negara)

    st.subheader("Grafik Distribusi Quantity")

    if "Quantity" in df.columns:
        quantity = df["Quantity"].dropna()
        st.line_chart(quantity.head(100))
        st.area_chart(quantity.head(100))

    st.subheader("Grafik Menggunakan Matplotlib")

    if "UnitPrice" in df.columns:
        fig, ax = plt.subplots()
        df["UnitPrice"].dropna().head(50).plot(
            kind="bar",
            ax=ax
        )
        ax.set_title("Harga Produk Online Retail")
        ax.set_xlabel("Index Data")
        ax.set_ylabel("Unit Price")
        st.pyplot(fig)
        plt.close(fig)

# ==========================================================
# KOMPONEN INPUT
# ==========================================================

elif menu == "Komponen Input":

    st.title("📝 Komponen Input Streamlit")

    st.subheader("Button")

    if st.button("Klik Tombol"):
        st.success("Tombol berhasil diklik!")

    st.subheader("Checkbox")

    pilihan = st.checkbox("Saya menyukai Machine Learning")

    if pilihan:
        st.write("Pilihan checkbox aktif.")

    st.subheader("Text Input")

    nama = st.text_input("Masukkan nama:")

    if nama:
        st.write("Halo,", nama)

    st.subheader("Number Input")

    angka = st.number_input(
        "Masukkan angka:",
        min_value=1,
        max_value=100,
        value=10
    )

    st.write("Angka yang dimasukkan:", angka)

    st.subheader("Text Area")

    pesan = st.text_area("Masukkan keterangan:")

    st.write("Keterangan:", pesan)

    st.subheader("Slider")

    nilai = st.slider(
        "Pilih nilai:",
        min_value=0,
        max_value=100,
        value=50
    )

    st.write("Nilai slider:", nilai)

    st.subheader("Select Slider")

    rating = st.select_slider(
        "Pilih tingkat kepuasan:",
        options=["Rendah", "Sedang", "Tinggi"]
    )

    st.write("Tingkat kepuasan:", rating)

    st.subheader("Multiselect")

    kolom = st.multiselect(
        "Pilih kolom dataset:",
        options=list(df.columns)
    )

    if kolom:
        st.dataframe(df[kolom].head())

    st.subheader("Date Input")

    tanggal = st.date_input("Pilih tanggal:")

    st.write("Tanggal dipilih:", tanggal)

    st.subheader("File Uploader")

    file = st.file_uploader(
        "Unggah file CSV:",
        type=["csv"]
    )

    if file is not None:
        data_upload = pd.read_csv(file)
        st.dataframe(data_upload.head())

    st.subheader("Color Picker")

    warna = st.color_picker("Pilih warna:", "#00AEEF")

    st.write("Warna pilihan:", warna)

# ==========================================================
# MEDIA
# ==========================================================

elif menu == "Media":

    st.title("🖼️ Komponen Media Streamlit")

    st.subheader("Menampilkan Gambar")

    st.image(
        "https://placehold.co/600x300/png?text=Online+Retail",
        caption="Ilustrasi Aplikasi Online Retail",
        use_container_width=True
    )

    st.subheader("Audio")

    st.write("Contoh komponen audio Streamlit.")

    st.audio(
        "https://www.w3schools.com/html/horse.mp3"
    )

    st.subheader("Video")

    st.video(
        "https://www.youtube.com/watch?v=jfKfPfyJRdk"
    )

# ==========================================================
# LAYOUT STREAMLIT
# ==========================================================

elif menu == "Layout Streamlit":

    st.title("📐 Layout dan Container")

    st.subheader("Columns")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("Kolom Pertama")

    with col2:
        st.success("Kolom Kedua")

    with col3:
        st.warning("Kolom Ketiga")

    st.divider()

    st.subheader("Tabs")

    tab1, tab2, tab3 = st.tabs(
        ["Dataset", "Statistik", "Informasi"]
    )

    with tab1:
        st.dataframe(df.head())

    with tab2:
        st.write(df.describe())

    with tab3:
        st.write("Dataset yang digunakan adalah Online Retail.")

    st.subheader("Expander")

    with st.expander("Lihat penjelasan dataset"):
        st.write(
            "Dataset Online Retail berisi informasi transaksi "
            "penjualan produk secara online."
        )

    st.subheader("Container")

    with st.container(border=True):
        st.write("Ini merupakan contoh penggunaan container.")
        st.metric("Jumlah Data", f"{len(df):,}")

    st.subheader("Empty")

    tempat = st.empty()

    if st.button("Tampilkan Pesan"):
        tempat.success("Pesan ditampilkan menggunakan st.empty().")

# ==========================================================
# FORM DAN KONTROL
# ==========================================================

elif menu == "Form dan Kontrol":

    st.title("📋 Form dan Kontrol Aplikasi")

    st.subheader("Form Streamlit")

    with st.form("form_pengguna"):

        nama = st.text_input("Nama lengkap")

        email = st.text_input("Email")

        pekerjaan = st.selectbox(
            "Pilih pekerjaan:",
            ["Mahasiswa", "Pelajar", "Pekerja", "Lainnya"]
        )

        kirim = st.form_submit_button("Kirim Data")

        if kirim:

            if nama.strip() and email.strip():

                st.success("Data berhasil dikirim!")

                st.write("Nama:", nama)
                st.write("Email:", email)
                st.write("Pekerjaan:", pekerjaan)

            else:
                st.error("Nama dan email harus diisi.")

    st.divider()

    st.subheader("Stop")

    st.write(
        "Contoh penggunaan st.stop() dapat dilakukan "
        "untuk menghentikan proses berdasarkan kondisi tertentu."
    )

    if st.checkbox("Hentikan proses pada halaman ini"):

        st.warning("Proses dihentikan menggunakan st.stop().")
        st.stop()

# ==========================================================
# FOOTER
# ==========================================================

st.sidebar.divider()
st.sidebar.caption("Teknik Informatika - Universitas Pamulang")
st.sidebar.caption("Machine Learning - Online Retail")
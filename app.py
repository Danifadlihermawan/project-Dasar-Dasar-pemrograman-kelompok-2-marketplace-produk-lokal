import streamlit as st
from login import form_login
from produk import tampilkan_produk, Produk
from keranjang import keranjang_belanja
from checkout import halaman_checkout
from PIL import Image

# Judul Aplikasi
st.title("Marketplace Produk Lokal")
st.subheader("Selamat Datang! Silakan masuk untuk melihat produk lokal terbaik kami.") 
st.image('istockphoto-1264753946-1024x1024.jpg')
st.snow()


# Periksa apakah sesi sudah diset
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Form Login
if not st.session_state.logged_in:
    form_login()

# Jika sudah login
if st.session_state.logged_in:
    # Tampilkan informasi profil pengguna
    st.success(f"Selamat Datang silahkan pilih produk lokal yang berkualitas, {st.session_state.nama,}!")
    
    # Menampilkan konten sesuai halaman yang dipilih
    while True:
        halaman = st.sidebar.radio("Pilih Halaman", ["Halaman Utama", "Pencarian Produk", "Keranjang Belanja", "Checkout"])

        if halaman == "Keranjang Belanja":
            st.session_state.page = "keranjang"  # Set halaman keranjang
        elif halaman == "Checkout":
            st.session_state.page = "checkout"  # Set halaman checkout
        else:
            st.session_state.page = "produk"  # Set halaman produk

        # Menampilkan konten sesuai halaman yang dipilih
        if st.session_state.get("page") == "produk":
            kategori = st.sidebar.selectbox("Pilih Kategori Produk yang Anda Inginkan", ["Makanan", "Fashion", "Kerajinan Tangan", "Elektronik"])
            tampilkan_produk(kategori)
        
        if st.session_state.get("page") == "keranjang":
            keranjang_belanja()

        if st.session_state.get("page") == "checkout":
            halaman_checkout()

        # Berhenti looping setelah satu interaksi (rendedering selesai)
        break

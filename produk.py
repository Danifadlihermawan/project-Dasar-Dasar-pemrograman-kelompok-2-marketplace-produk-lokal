import streamlit as st
from PIL import Image

class Produk:
    def __init__(self, nama, deskripsi, harga, kategori, gambar=None):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.kategori = kategori
        self.gambar = gambar  # Menambahkan atribut gambar

    def get_details(self):
        return f"Deskripsi: {self.deskripsi}\nHarga: Rp {self.harga}\nKategori: {self.kategori}"

# Fungsi untuk menampilkan produk berdasarkan kategori
def tampilkan_produk(kategori):
    produk_makanan = [
        Produk("Nasi Goreng Spesial", "Nasi goreng dengan telur, ayam, dan sayuran", 25000, "Makanan", "images/nasigoreng.jpeg"),
        Produk("Rendang", "Makanan tradisional yang terbuat dari daging sapi dengan santan kelapa", 35000, "Makanan", "images/rendang.jpeg"),
        Produk("Sate Ayam", "Sate ayam dengan bumbu spesial", 25000, "Makanan", "images/sateayam.jpeg"),
        Produk("Nasi Padang", "Makanan Tradisional dengan cita rasa unik", 20000, "Makanan", "images/nasipadang.jpeg"),
        Produk("Ayam betutu", "Ayam utuh yang dimasak dengan bumbu khas bali rasanya pedas", 35000, "Makanan", "images/ayambetutu.jpeg")
    ]
    
    produk_fashion = [
        Produk("Kaos Lengan Panjang", "Kaos lengan panjang berbahan cotton, nyaman dipakai", 150000, "Fashion", "images/kaoslenganpanjang.jpeg"),
        Produk("Kemeja batik", "Pakaian tradisional dengan adat budaya yang murni", 50000, "Fashion", "images/kemejabatik.jpeg"),
        Produk("Sepatu kulit", "Sepatu kulit lokal yang terbuat dari bahan kulit pilihan", 150000, "Fashion", "images/sepatukulit.jpeg"),
        Produk("Tas wanita keren", "Tas unik dengan gaya yang melokal", 60000, "Fashion", "images/taswanita.jpeg")
    ]
    
    produk_kerajinan = [
        Produk("Gantungan Kunci Kayu", "Gantungan kunci berbahan kayu dengan ukiran tangan", 20000, "Kerajinan Tangan", "images/gantungankunci.jpeg"),
        Produk("wayang", "wayang kulit yang menghadiri lokal indonesia dengan gaya yang melokal", 120000, "Kerajinan Tangan", "images/wayang.jpeg"),
        Produk("Asbak Kayu", "Asbak yang terbuat dari batok kelapa", 22000, "Kerajinan Tangan", "images/asbak.jpeg"),
        Produk("Kipas kayu cendana", "Kipas kayu yang terbuat dari bahan kayu cendana yang wangi", 20000, "Kerajinan Tangan", "images/kipaskayu.jpeg"),
        Produk("Angklung", "Kerajinan yang bisa dibeli sebagai hiasan atau alat musik tradisional", 70000, "Kerajinan Tangan", "images/angklung.jpeg")
    ]
    
    produk_elektronik = [
        Produk("Polytron LED TV", "Televisi dengan teknologi LED", 2000000, "Elektronik", "images/politron.jpeg"),
        Produk("kulkas ", "kulkas dengan teknologi hemat energi dan desain kompak", 2200000, "Elektronik", "images/kulkas.jpeg"),
        Produk("Mitto 4G Smartphone", "Smartphone dengan jaringan 4G dan performa cukup baik untuk keperluan komunikasi dan media sosial", 1800000, "Elektronik", "images/mito.jpeg"),
        Produk("motor listrik", "motor listrik yang menawarkan solusi ramah lingkungan", 4000000, "Elektronik", "images/sepedalistrik.jpeg")
    ]
    
    produk_list = []
    if kategori == "Makanan":
        produk_list = produk_makanan
    elif kategori == "Fashion":
        produk_list = produk_fashion
    elif kategori == "Kerajinan Tangan":
        produk_list = produk_kerajinan
    elif kategori == "Elektronik":
        produk_list = produk_elektronik

    for produk in produk_list:
        st.subheader(produk.nama)
        st.write(produk.get_details())
        
        # Menampilkan gambar produk jika ada
        if produk.gambar:
            try:
                image = Image.open(produk.gambar)
                st.image(image, width=250)  # Mengatur lebar gambar menjadi 300px
            except Exception as e:
                st.warning(f"Gambar untuk {produk.nama} tidak ditemukan.")
        
        # Menambahkan tombol untuk menambah produk ke keranjang
        if st.button(f"Tambah ke Keranjang - {produk.nama}"):
            if "keranjang" not in st.session_state:
                st.session_state.keranjang = []
            st.session_state.keranjang.append(produk)
            st.success(f"Produk {produk.nama} telah ditambahkan ke keranjang!")


import streamlit as st
from PIL import Image

def halaman_checkout():
    st.header("Halaman Checkout")

    if len(st.session_state.keranjang) > 0:
        # Tampilkan ringkasan pesanan
        st.subheader("Ringkasan Pesanan")
        total_harga = 0
        for p in st.session_state.keranjang:
            st.write(f"- {p.nama} ({p.kategori}) - Rp {p.harga}")
            total_harga += p.harga
        st.write(f"**Total Harga: Rp {total_harga}**")
        
        # Pilih metode pembayaran
        st.subheader("Pilih Metode Pembayaran")

        metode_pembayaran = st.radio(
            "Pilih Metode Pembayaran:",
            ["Dana", "OVO", "Gopay", "Shopeepay"]
        )

        # Menampilkan ikon berdasarkan pilihan metode pembayaran
        if metode_pembayaran == "Dana":
            dana_icon = Image.open("dana.jpeg")
            st.image(dana_icon, width=50)
        elif metode_pembayaran == "OVO":
            ovo_icon = Image.open("ovo.jpeg")
            st.image(ovo_icon, width=50)
        elif metode_pembayaran == "Gopay":
            gopay_icon = Image.open("gopay.jpeg")
            st.image(gopay_icon, width=50)
        elif metode_pembayaran == "Shopeepay":
            shopeepay_icon = Image.open("shoopy.jpeg")
            st.image(shopeepay_icon, width=50)

        if st.button("Konfirmasi Pesanan"):
            st.success(f"Pesanan Anda telah dikonfirmasi dengan metode pembayaran {metode_pembayaran}. Terima kasih telah berbelanja!")
            st.session_state.keranjang = []  # Kosongkan keranjang setelah checkout
    else:
        st.write("Keranjang Anda kosong.")

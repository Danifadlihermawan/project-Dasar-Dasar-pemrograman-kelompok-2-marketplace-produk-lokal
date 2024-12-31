import streamlit as st

def keranjang_belanja():
    st.header("Keranjang Belanja Anda")
    if len(st.session_state.keranjang) > 0:
        total_harga = 0
        for p in st.session_state.keranjang:
            st.write(f"- {p.nama} ({p.kategori}) - Rp {p.harga}")
            total_harga += p.harga
        st.write(f"**Total Harga: Rp {total_harga}**")
        if st.button("Checkout"):
            st.session_state.page = "checkout"  # Pindah ke halaman checkout
    else:
        st.write("Keranjang Anda kosong.")

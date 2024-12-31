import streamlit as st

def form_login():
    with st.form("login_form"):
        st.write("Masukkan Informasi Anda untuk Melanjutkan")
        
        # Input untuk profil pengguna
        nama = st.text_input("Nama Lengkap")
        umur = st.number_input("Umur", min_value=0, max_value=100, step=1)
        jenis_kelamin = st.selectbox("Jenis kelamin", ["Laki-laki", "Perempuan"])
        status_pelanggan = st.selectbox("Status pelanggan", ["Pendidikan Menengah (SMA-SMP)", "Mahasiswa", "Wiraswasta", "Pengusaha", "Pejabat Negara"])
        alamat = st.text_input("Alamat")
        
        submitted = st.form_submit_button("Login")

    # Logika Setelah Login
    if submitted:
        if nama and umur and alamat:
            st.session_state.logged_in = True
            st.session_state.nama = nama
            st.session_state.umur = umur
            st.session_state.jenis_kelamin = jenis_kelamin
            st.session_state.status_pelanggan = status_pelanggan
            st.session_state.alamat = alamat
            
            # Menampilkan informasi yang telah diisi
            st.success(f"Selamat Datang di toko kami, {nama}! Anda telah berhasil login.")
            st.info("Informasi yang Anda masukkan:")
            st.write(f"**Nama Lengkap:** {nama}")
            st.write(f"**Umur:** {umur} tahun")
            st.write(f"**Jenis Kelamin:** {jenis_kelamin}")
            st.write(f"**Status Pelanggan:** {status_pelanggan}")
            st.write(f"**Alamat:** {alamat}")
        else:
            st.warning("Harap lengkapi semua informasi sebelum melanjutkan.")

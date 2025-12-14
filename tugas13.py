import streamlit as st

#ini halaman uutuama
st.title('Aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')
menu = st.sidebar.selectbox('menu',['Luas Jajar Genjang', 'Luas Persegi Panjang', 'Luas Trapesium'])

if menu == 'Luas Jajar Genjang':
    st.write('Ini Halaman untuk menghitung Luas Jajar Genjang')
    st.markdown(':yellow[Menghitung Luas Jajar Genjang]:balloon::balloon:')
    st.image('https://cnc-magazine.oramiland.com/parenting/images/rumus_luas_jajar_genjang-x.width-800.format-webp.webp',caption='gambar jajar genjang', )
    alas = st.number_input('Silahkan Masukkan Alas',min_value=0)
    tinggi = st.number_input('Silahkan Masukkan Tinggi',min_value=0)
    if st.button('hitung'):
        luas = alas*tinggi
        st.write(f'Luas Jajar Genjang adalah {luas}')
    
elif menu == 'Luas Persegi Panjang':
    st.write('Ini Halaman untuk menghitung Luas Persegi Panjang')
    st.markdown(':yellow[Menghitung Luas Persegi Panjang]:balloon::balloon:')
    st.image('https://blue.kumparan.com/image/upload/fl_progressive,fl_lossy,c_fill,f_auto,q_auto:best,w_640/v1639734148/alocipfjxvrwdvfp4qgh.jpg',caption='gambar jajar genjang', )
    panjang = st.number_input('Silahkan Masukkan Panjang',min_value=0)
    lebar = st.number_input('Silahkan Masukkan Lebar',min_value=0)
    if st.button('hitung'):
        luas = panjang*lebar
        st.write(f'Luas Persegi Panjang adalah {luas}')

    
elif menu == 'Luas Trapesium':
    st.write('Ini Halaman untuk menghitung Luas Trapesium')
    st.markdown(':yellow[Menghitung Luas Trapesium]:balloon::balloon:')
    st.image('https://awsimages.detik.net.id/community/media/visual/2021/06/24/trapesium_169.png?w=600&q=90',caption='gambar jajar genjang', )
    nilai1 = st.number_input('Silahkan Masukkan Nilai Pertama',min_value=0)
    nilai2 = st.number_input('Silahkan Masukkan Nilai Kedua',min_value=0)
    tinggi = st.number_input('Silahkan Masukkan Tinggi',min_value=0)
    if st.button('hitung'):
        luas = (nilai1+nilai2)*tinggi/2
        st.write(f'Luas Jajar Genjang adalah {luas}')
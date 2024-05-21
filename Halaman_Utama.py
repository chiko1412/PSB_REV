import streamlit as st
import pandas as pd
import requests
import base64

from streamlit_lottie import st_lottie


def img_to_base64(image_path):
    """Convert image to base64"""
    with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    
    # Import gambar & konversi ke base64
img_path = "imgs/icon_aka.png"  
img_base64 = img_to_base64(img_path)
st.sidebar.markdown(
    f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto;">',
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
st.sidebar.header("~~~ PROJECT PSB ~~~")

# Judul 
st.markdown("<h1 style='text-align:center;color:red;'><i class='fas fa-calculator'></i> Selamat datang di aplikasi perhitungan kerapatan dan viskositas <i class='fas fa-flask'></i></h1>", unsafe_allow_html=True)
st.markdown('----')

# File json format (File path)
lottie_url = "https://lottie.host/355e4741-b8f2-4b2a-96ea-25858290c668/bsngZSgfEx.json"

# Fungsi untuk memproses lottie url
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Memproses animasi lottie
lottie_json = load_lottie_url(lottie_url)

# Pembuatan 2 kolom
col1, col2,col3 = st.columns([1, 2, 1])

# Menampilkan animasi lottie
with col2:
    if lottie_json is not None:
        st_lottie(lottie_json)
    else:
        st.write("Failed to load Lottie animation.")

st.subheader(" Aplikasi yang dapat membantu anda untuk menghitung kerapatan curah,kerapatan absolut,kerapatan relatif dan viskositas sampel.")
st.subheader('Sebelum itu, apasih itu kerapatan dan viskositas?')

#Pengertian kerapatan dan jenis jenisnya
st.subheader('Apa itu Kerapatan?')
st.write('Kerapatan merupakan perbandingan antara massa dan volume dari suatu senyawa. Makin besar volume dan massa dari suatu senyawa, makin kecil kerapatannya. Begitu juga sebaliknya, makin kecil volume dan massa suatu senyawa, kerapatannya makin besar. Kebanyakan zat padat dan cairan mengembang sedikit bila dipanaskan dan menyusut sedikit bila dipengaruhi penambahan tekanan eksternal.Kerapatan juga memiliki berbagai jenis seperti:')

col1, col2, col3 = st.columns([1, 2, 1])
col1.markdown("<h1 style='text-align: left; color:violet;'>Kerapatan Curah</h1>", unsafe_allow_html=True)
col1.markdown(":blue[Kerapatan Curah] adalah bobot bahan padat berbentuk butiran dibagi volume curah, yaitu volume bahan dalam bentuk tercurah seperti beras pada takaran.")
col2.markdown("<h1 style='text-align: center; color:violet;'>Kerapatan Absolut</h1>", unsafe_allow_html=True)
col2.markdown(":blue[Kerapatan Absolut] adalah bobot bahan dibagi volume nyata bahan. Untuk benda yang bersifat curah, volume nyata adalah volume curah dikurangi volume udara di antara butiran-butiran bahan. Volume celah-celah butiran ini bisa diketahui dengan cara menambahkan cairan (yang akan mengisi celah-celah butiran) yang tidak bereaksi (diserap, diresapi, atau membentuk ikatan) dengan bahan.")
col3.markdown("<h1 style='text-align: center; color:violet;'>Kerapatan Relatif</h1>", unsafe_allow_html=True)
col3.markdown(":blue[Kerapatan Relatif] adalah perbandingan kerapatan bahan dengan kerapatan air pada temperatur dan tekanan yang sama.")


# Pengertian Viskositas dan metode metodenya
st.subheader('Apa itu Viskositas?')
st.write('Viskositas adalah parameter yang mengukur resistensi suatu cairan terhadap deformasi, dihasilkan oleh gaya gesek dalam fluida yang disebabkan oleh kohesi dan pertukaran momentum antar molekul-molekul fluida. Penting untuk dicatat bahwa ada perbedaan perilaku viskositas antara cairan dan gas terhadap perubahan suhu. Dalam konsep fluida ideal, viskositasnya nol. Dalam penentuan viskositas juga terdapat beberapa cara yaitu:')

# Membagi layout menjadi tiga kolom
col1, col2, col3 = st.columns([1,1,1])

# Kolom 1 - Metode Oswald
with col1:
    st.markdown("<h1 style='text-align: left; color:aqua;'><i class='fas fa-flask'></i> Metode Oswald</h1>", unsafe_allow_html=True)
    st.markdown(":blue[Penetapan kekentalan menggunakan viskosimeter Oswald] mengacu pada pengukuran kecepatan aliran fluida melalui pipa kapiler untuk menentukan kekentalan kinematik. Metode ini cocok untuk sampel cair dengan sudut kontak yang mendekati 0 derajat dengan kaca, khususnya jika kekentalannya mirip dengan air. Pengukuran dilakukan dengan membandingkan waktu aliran volume tertentu antara sampel dan standar, karena fluida mengalir karena gaya berat, sehingga diperlukan pengukuran kerapatan sampel.")
    
    
# Kolom 2 - kosong
with col2:
    st.write('')

# Kolom 3 - Metode Engler
with col3:
    st.markdown("<h1 style='text-align: aqua; color:aqua;'><i class='fas fa-flask'></i> Metode Engler</h1>", unsafe_allow_html=True)
    st.markdown(":blue[Penetapan kekentalan menggunakan viskosimeter Engler] melibatkan pengukuran kecepatan aliran fluida melalui saluran tertentu, yang mirip dengan viskosimeter Oswald tetapi menggunakan pipa dengan diameter yang lebih besar. Berbeda dengan Oswald, sudut kontak tidak harus mendekati nol. Metode ini cocok untuk sampel cair dengan kekentalan kinematik yang relatif tinggi. Selain itu, perlu mengukur kerapatan sampel dan suhu pengukuran untuk memperoleh hasil yang akurat.")







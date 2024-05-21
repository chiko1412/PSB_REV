import streamlit as st
import requests

from streamlit_lottie import st_lottie

st.markdown("<h1 style='text-align:center;color:red;'><i class='fas fa-calculator'></i> PSB (Padang Sukabumi Bogor) <i class='fas fa-flask'></i></h1>", unsafe_allow_html=True)

st.header(':violet[Anggota Kelompok]')
st.subheader(':green[1. Muhammad Fadil Nugraha (2360178)]')
st.subheader(':green[2. Mutia Azatil ismah(2360191)]')
st.subheader(':green[3. Said Muhammad Iqbal (2360253)]')
st.header(':violet[Contact Person]')
st.subheader(':green[Fadil (085624826410)]')
st.subheader(':green[Muti (083161993086)]')
st.subheader(':green[Iqbal (085771008112)]')

# file json format (File path)
lottie_url="https://lottie.host/acebf761-e872-435e-b43f-1c19cac74529/1SAS32qZRd.json"

# Fungsi untuk momproses lottie url
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
# Memproses animasi lottie
lottie_json=load_lottie_url(lottie_url)

#pembuatan 2 kolom
col1,col2= st.columns([1,2])

#Menampilkan animasi lottie
with col2 :
    if lottie_json is not None:
        st_lottie(lottie_json)
    else:
        st.write("Failed to load Lottie animation.")
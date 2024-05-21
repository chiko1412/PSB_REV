import streamlit as st
import pandas as pd
import base64

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
st.markdown("<h1 style='text-align:center;color:red;'><i class='fas fa-calculator'></i> Nilai Viskositas air berdasarkan suhu ruang <i class='fas fa-flask'></i></h1>", unsafe_allow_html=True)
    
# Fungsi untuk memuat data
def load_data():
     return pd.DataFrame({
        "Temperatur (°C)": [20, 21, 22, 23, 24, 25, 26, 27, 27.5, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        "Kerapatan air": [0.9982, 0.9980, 0.9978, 0.9976, 0.9973, 0.9971, 0.9968, 0.9965, 0.9964, 0.9963, 0.9960, 0.9957, 0.9954, 0.9951, 0.9947, 0.9944, 0.9941, 0.9937, 0.9934, 0.9930, 0.9926, 0.9922]
    })

    # Tampilkan tabel dengan format lebar (opsional)
use_container_width = st.checkbox("Tampilkan tabel dengan format lebar", value=False, key="use_container_width")
df = load_data()
st.dataframe(df.style.format({'Temperatur (°C)': '{:.1f}'}), use_container_width=use_container_width)


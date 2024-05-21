import streamlit as st
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

st.markdown("<h1 style='text-align:center;color:red;'><i class='fas fa-calculator'></i> Perhitungan Kerapatan Curah <i class='fas fa-flask'></i></h1>", unsafe_allow_html=True)
st.markdown('----')
st.subheader(':violet[Bagaimana cara mendapatkan data untuk perhitungan kerapatan curah? Simak caranya berikut ini:]')
st.write('1. Gelas ukur kosong ditimbang, catat sebagai Wgu')
st.write('2. Kacang ijo dimasukkan ke dalam gelas ukur sambil diketuk-ketuk sampai tanda tera 25,0 mL. Catat sebagai Vc. (Volume 25 mL tidak standar, bisa diubah ke volume berapa saja).')
st.write('3. Gelas ukur berisi kacang ijo ditimbang, catat sebagai Wgb. Hitung bobot kacang ijo (Wgb-Wgu) dan catat sebagai W.')

st.subheader(':blue[Rumus Kerapatan Curah]')
rumus = r"\text{Kerapatan Curah} = \frac{\text{Berat wadah isi Sampel} - \text{berat wadah kosong}}{\text{Volume Sampel}}"
st.latex(rumus)

# Perhitungan kerapatan curah
st.subheader(':green[Masukkan data data yang telah di dapat agar bisa di hitung dengan kalkulator kami]')
def calculate_bulk_density(sample_weight, berat_wadah, sample_volume):
    try:
        bulk_density = ((sample_weight - berat_wadah) / sample_volume)
        return bulk_density
    except ZeroDivisionError:
        st.error("Error: Pembagian dengan nol tidak diizinkan.")
        return None
def main():
    st.subheader('Kalkulator Kerapatan Curah')
    sample_weight_bulk = st.number_input('Bobot Gelas Ukur Isi Sampel (g):', min_value=0.0, format="%.4f", key='bulk_sample_weight')
    berat_wadah_bulk = st.number_input('Bobot Gelas Ukur (g):', min_value=0.0, format="%.4f", key='bulk_berat_wadah')
    sample_volume_bulk = st.number_input('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, format="%.2f", key='bulk_sample_volume')
    if st.button('Hitung Kerapatan Curah'):
        bulk_density = calculate_bulk_density(sample_weight_bulk, berat_wadah_bulk, sample_volume_bulk)
        if bulk_density is not None:
            st.subheader('Hasil Perhitungan Kerapatan Curah:')
            st.write('Kerapatan Curah:', bulk_density, 'g/mL')

if __name__ == '__main__':
    main()

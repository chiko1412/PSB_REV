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

st.markdown("<h1 style='text-align:center;color:red;'><i class='fas fa-calculator'></i> Perhitungan Viskositas sampel metode Engler <i class='fas fa-flask'></i></h1>", unsafe_allow_html=True)
st.markdown('----')
st.subheader(':violet[Bagaimana cara mendapatkan data untuk perhitungan Viskositas sampel metode engler? Simak caranya berikut ini:]')
st.write('a. Penetapan Kekentalan Metode Engler:')
st.write('1. Siapkan buret 50 mL dan stopwatch.')
st.write('2. Isi buret dengan air suling hingga melampaui titik nol.')
st.write('3. Buka cerat buret hingga mencapai posisi maksimum.')
st.write('4. Hidupkan stopwatch saat cairan melewati skala 5 mL.')
st.write('5. Matikan stopwatch saat skala buret mencapai 30 mL.')
st.write('6. Catat waktu yang ditunjukkan oleh stopwatch sebagai Ta.')
st.write('7. Lakukan langkah-langkah yang sama pada sampel.')
st.write('*Mengukur Densitas Air dan Sampel Sabun:*')
st.write('1. Isi gelas piala 100 mL dengan air suling.')
st.write('2. Catat suhu air suling untuk referensi.')
st.write('3. Lakukan langkah yang sama dengan sampel sabun.')
st.write('4. Timbang bobot piknometer kosong.')
st.write('5. Timbang bobot piknometer yang berisi air suling.')
st.write('6. Timbang bobot piknometer yang berisi sampel sabun.')


st.subheader(':blue[Rumus Viskositas sampel]')
rumus = r"\text{Viskositas sampel} = \frac{\text{Densitas sampel} - \text{waktu alir sampel}}{\text{Densitas air}-\text{waktu alir air}} \times \text{Viskositas air}"
st.latex(rumus)

# perhitungan viskostas sampel metode engler
st.subheader(':green[Masukkan data data yang telah di dapat agar bisa di hitung dengan kalkulator kami]')
def calculate_sample_viscosity(sample_density, water_density, sample_flow_time, water_flow_time, nilai_viskositas):
    try:
        sample_viscosity = sample_density * sample_flow_time / (water_density * water_flow_time) * nilai_viskositas
        return sample_viscosity
    except ZeroDivisionError:
        st.error("Error: Pembagian dengan nol tidak diizinkan.")
        return None
def main():
    st.subheader('Nilai Viskositas sample')
    nilai_viskositas_bulk =  st.number_input('Nilai Viskositas air (mPa.s):', min_value=0.0, format="%.4f", key='bulk_nilai_viskositas')
    sample_flow_time_sam = st.number_input('Waktu Alir Sampel (detik):', min_value=0.0, format="%.2f", key='sam_sample_flow_time')
    sample_density_sam = st.number_input('Kerapatan Sample (g/mL):', min_value=0.0, format="%.4f", key='sam_sample_density')
    water_flow_time_sam = st.number_input('Waktu Alir Air (detik):', min_value=0.0, format="%.2f", key='sam_water_flow_time')
    water_density_sam = st.number_input('Kerapatan Air (g/mL):', min_value=0.0, format="%.4f", key='sam_water_density')
    if st.button('Hitung Viskositas Sampel'):
        sample_viscosity = calculate_sample_viscosity(sample_density_sam, water_density_sam, sample_flow_time_sam, water_flow_time_sam, nilai_viskositas_bulk)
        if sample_viscosity is not None:
          st.subheader('Hasil Perhitungan Viskositas Sampel:')
          st.write('Viskositas Sampel:', sample_viscosity, 'cP')
            

if __name__ == '__main__':
    main()


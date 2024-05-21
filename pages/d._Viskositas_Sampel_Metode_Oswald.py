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

st.markdown("<h1 style='text-align:center;color:red;'><i class='fas fa-calculator'></i> Perhitungan Viskositas sampel metode oswald <i class='fas fa-flask'></i></h1>", unsafe_allow_html=True)
st.markdown('----')
st.subheader(':violet[Bagaimana cara mendapatkan data untuk perhitungan Viskositas sampel metode? Simak caranya berikut ini:]')
st.write('**a. Penentuan Densitas Aquadest/Sampel:**')
st.write('1. Persiapkan piknometer 25 mL, cuci bersih, dan timbang sebanyak 3 kali. Catat bobot kosong piknometer.')
st.write('2. Tambahkan aquadest hingga piknometer penuh, lalu tutup.')
st.write('3. Bersihkan dinding luar piknometer, kemudian timbang piknometer dengan aquadest di dalamnya sebanyak 3 kali.')
st.write('4. Lakukan langkah yang sama untuk menentukan densitas sampel (sabun).')
st.write('**b. Penentuan Waktu Alir Larutan:**')
st.write('1. Cuci viskometer Oswald dan bilas dengan aquadest, lalu isi dengan sampel melalui lubang berdiameter besar menggunakan corong sebanyak 2 kali.')
st.write('2. Masukkan zat cair ke dalam viskometer Oswald melalui lubang berdiameter besar dengan corong.')
st.write('3. Hisap zat cair menggunakan bulb dari lubang berdiameter kecil.')
st.write('4. Tutup lubang berdiameter kecil dengan jari tangan setelah zat cair melewati tanda batas.')
st.write('5. Turunkan zat cair perlahan dengan membuka jari tangan.')
st.write('6. Hidupkan stopwatch ketika zat cair mencapai tanda batas bagian atas.')
st.write('7. Matikan stopwatch ketika zat cair mencapai tanda batas bagian bawah.')
st.write('8. Ulangi percobaan sebanyak 3 kali.')


st.subheader(':blue[Rumus Viskositas sampel]')
rumus = r"\text{Viskositas sampel} = \frac{\text{Densitas sampel} - \text{waktu alir sampel}}{\text{Densitas air}-\text{waktu alir air}} \times \text{Viskositas air}"
st.latex(rumus)



# perhitungan viskositas sampel metode oswald
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

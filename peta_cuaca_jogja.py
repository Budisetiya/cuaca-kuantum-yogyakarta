import folium
import requests

# 1. Buat peta berpusat di Tugu Yogyakarta
peta = folium.Map(
    location=[-7.8011, 110.3426],  # Koordinat Tugu Jogja
    zoom_start=12,  # Tingkat perbesaran awal
    tiles="CartoDB Positron"  # Gaya peta bersih dan mudah dilihat
)

# 2. Daftar tempat penting di Kota Yogyakarta
tempat_jogja = {
    "Tugu Yogyakarta": [-7.8011, 110.3426],
    "Alun-alun Utara & Keraton": [-7.7965, 110.3665],
    "Alun-alun Selatan": [-7.8133, 110.3675],
    "Malioboro": [-7.7934, 110.3658],
    "Universitas Gadjah Mada": [-7.7702, 110.3783],
    "Candi Prambanan": [-7.7523, 110.4914],
    "Bandara Adisutjipto": [-7.7844, 110.4327]
}

# 3. Ambil data cuaca asli dari internet
print("🔄 Mengambil data cuaca Yogyakarta...")
api_url = "https://api.open-meteo.com/v1/forecast?latitude=-7.8011&longitude=110.3426&current=temperature_2m,relative_humidity_2m,precipitation,weather_code&timezone=Asia%2FJakarta"
data_cuaca = requests.get(api_url).json()["current"]

suhu = data_cuaca["temperature_2m"]
lembab = data_cuaca["relative_humidity_2m"]
hujan = data_cuaca["precipitation"]

# 4. Tambah tanda penanda di setiap lokasi
for nama_tempat, koordinat in tempat_jogja.items():
    # Teks yang muncul saat diklik tanda
    info = f"""
    <strong>{nama_tempat}</strong><br>
    🌡️ Suhu: {suhu} °C<br>
    💧 Kelembapan: {lembab} %<br>
    ☔ Curah Hujan: {hujan} mm
    """
    
    # Pasang tanda di peta
    folium.Marker(
        koordinat,
        popup=folium.Popup(info, max_width=280),
        icon=folium.Icon(color="blue", icon="cloud")
    ).add_to(peta)

# 5. Simpan peta jadi file yang bisa dibuka
peta.save("peta_cuaca_jogja.html")
print("\n✅ PETA SUDAH JADI!")
print("👉 Buka file 'peta_cuaca_jogja.html' di browser HP kamu")


import requests
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print("🌍 MENGAMBIL DATA CUACA YOGYAKARTA...")
API = "https://api.open-meteo.com/v1/forecast?latitude=-7.8011&longitude=110.3426&current=temperature_2m,relative_humidity_2m,precipitation,weather_code&timezone=Asia%2FJakarta"
data = requests.get(API).json()["current"]

suhu = data["temperature_2m"]
lembab = data["relative_humidity_2m"]
hujan = data["precipitation"]
kode = data["weather_code"]

cuaca = {
    0:"☀️ Cerah",1:"🌤️ Sebagian berawan",2:"⛅ Berawan",3:"☁️ Mendung",
    45:"🌫️ Kabut",51:"🌧️ Gerimis",61:"🌧️ Hujan ringan",63:"🌧️ Hujan sedang",65:"🌧️ Hujan lebat"
}.get(kode, "❓ Tidak diketahui")

print("\n⚛️ MEMBUAT SIRKUIT KUANTUM...")
nilai_suhu = min(1, max(0, (suhu - 20) / 15))
nilai_hujan = min(1, hujan / 10)

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.ry(nilai_suhu * 3.14, 0)
qc.cx(0, 1)
qc.ry(nilai_hujan * 3.14, 1)
qc.measure_all()

simulator = AerSimulator()
hasil = simulator.run(qc, shots=1024).result().get_counts()
peluang = round((hasil.get("11",0) + hasil.get("01",0)) / 10.24, 1)

print("\n" + "="*50)
print("📊 PEMANTAU CUACA YOGYAKARTA")
print("="*50)
print(f"📍 Lokasi      : Yogyakarta")
print(f"🌡️ Suhu        : {suhu} °C")
print(f"💧 Kelembapan  : {lembab} %")
print(f"☔ Curah Hujan : {hujan} mm")
print(f"🌤️ Kondisi     : {cuaca}")
print(f"\n⚛️ Dihitung di  : Simulator Kuantum Lokal")
print(f"📈 Peluang Hujan: {peluang} %")
print("="*50)

import requests

def ambil_ayat(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["data"]["text"]
    except requests.exceptions.RequestException as e:
        return f"Terjadi error saat mengambil data: {e}"

# Ambil teks Arab dan Inggris
arab = ambil_ayat("https://api.alquran.cloud/v1/ayah/2:255/quran-simple")
english = ambil_ayat("https://api.alquran.cloud/v1/ayah/2:255/en.asad")

# Output
print("Ayat Al-Kursi (2:255) - Arab:")
print(arab)
print("\nTerjemah (EN):")
print(english)

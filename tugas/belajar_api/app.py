import requests
url = "https://api.aladhan.com/v1/timingsByCity/28-08-2025?city=Jakarta&country=Indonesia&method=5 "
response = requests.get(url) # HTTP GET
data_json = response.json()  # konversi ke json
print(data_json['data']['timings'])
tgl_hijri = data_json['data']['date']['hijri']['date']
print(f"tgl Hijriah: (tgl_hijri")
print("jadwal sholat")

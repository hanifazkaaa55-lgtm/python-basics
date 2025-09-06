import json

# Membaca file JSON lokal
with open("peminjaman_buku.json", "r") as file:
    data = json.load(file)

total_dipinjam = 0
total_belum_kembali = 0

print("Belum kembali:")
for anggota in data["anggota"]:
    nama = anggota["nama"]
    for pinjam in anggota["pinjam"]:
        total_dipinjam += 1
        if not pinjam["kembali"]:  # boolean check
            total_belum_kembali += 1
            print(f"- {nama} : {pinjam['judul']} ({pinjam['tanggal']})")

print(f"\nTotal dipinjam: {total_dipinjam} | Belum kembali: {total_belum_kembali}")

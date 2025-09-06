# Program memasukkan 5 nama buah ke dalam list dan menampilkannya

# Inisialisasi list kosong untuk menyimpan nama buah
daftar_buah = []

# Loop sebanyak 5 kali untuk meminta input nama buah
for i in range(5):
    buah = input(f"Masukkan nama buah ke-{i+1}: ")
    daftar_buah.append(buah)

# Menampilkan daftar buah yang sudah dimasukkan
print("\nDaftar buah kamu:")
for idx, buah in enumerate(daftar_buah, start=1):
    print(f"{idx}. {buah}")

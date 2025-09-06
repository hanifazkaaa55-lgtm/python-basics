print("===================")
# open -> baca file -> ambil datanya,jadikan list
# ekstrak data dengan for loop (edit/hapus)
#buat ulang semua baris file csv dgn mode"w"

# buat list kosong untuk menampung data dari csv
data_alamat = []
with open(csv_alamat_path, "a", newline="") as file_alamat:
    edit_alamat = csv.wri
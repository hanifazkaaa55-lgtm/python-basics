print("materi 10 - file handling")
print("-------------------------")
# file extension/ekstensi yg membedakan
# jenis suatu file, lihat di akhir nama file
# .py (python), doc (document)



file_path =
#buka file target dengan mode tertentu
file_pesan = open(file_path, "r") # r read only
baca_pesan = file_pesan.read()
print(f"isi pesannya: {baca_pesan}")
# tutup file
file_pesan.close()
print("============ open csv ==============")
csv_alamat_path = r""
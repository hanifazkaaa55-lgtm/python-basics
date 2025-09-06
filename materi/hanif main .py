
print("=== MASUKKAN DATA PROFIL DIGITAL KAMU ===")

nama = input("Nama: ")
umur = int(input("Umur: "))
kelas = input("Kelas: ")
hobi = input("Hobi: ")
cita_cita = input("Cita-cita: ")
belajar_paling_enak = input("Belajar paling enak pas (pagi/siang/malam): ")
tahun_lahir = int(input("Tahun lahir: "))

print("\n=== MASUKKAN DATA TIPE DIGITAL ===")

tipe = input("Tipe digital (Contoh: Gamer, Content Creator, dll): ")
game_favorit = input("Game favorit: ")

print("\n=== FUN CHECK ===")
teman_bau_input = input("Teman sebelah bau? (ya/tidak): ").strip().lower()
teman_sebelah_bau = teman_bau_input == "ya"

# Komentar default untuk gamer
komentar = f"Wih, kamu pasti jago main {game_favorit} sambil ngoding. GG gaming! 🎮🔥"

# Tampilkan hasil
print("\n===== PROFIL DIGITAL KAMU =====")
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Kelas: {kelas}")
print(f"Hobi: {hobi}")
print(f"Cita-cita: {cita_cita}")
print(f"Belajar paling enak pas: {belajar_paling_enak}")
print(f"Tahun lahir: {tahun_lahir}")



print("\n=== TIPE DIGITAL ===")
print(f"Tipe: {tipe}")
print(f"Game favorit: {game_favorit}")
print(f"Komentar: {komentar}")

print("\n=== FUN CHECK ===")
if teman_sebelah_bau:
    print("Teman sebelah bau? ya")
    print("Aduh... kasih pewangi darurat dong, darurat nasional ini 😷")
else:
    print("Teman sebelah bau? tidak")
    print("Aman, udara segar sepanjang hari 😌")


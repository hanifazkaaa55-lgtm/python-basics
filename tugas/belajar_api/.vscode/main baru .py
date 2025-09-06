print("=== MASUKKAN DATA PROFIL DIGITAL KAMU ===")

nama = input("Nama: ")
umur = int(input("Umur: "))
kelas = input("Kelas: ")
hobi = input("Hobi: ")
cita_cita = input("Cita-cita: ")
belajar_paling_enak = input("Belajar paling enak pas (pagi/siang/malam): ")
tahun_lahir = int(input("Tahun lahir: "))

print("\n=== MASUKKAN DATA TIPE DIGITAL ===")

tipe = input("Tipe digital (Contoh: Gamer, Content Creator, Programmer, Editor, dll): ")
game_favorit = input("Game favorit: ")

print("\n=== FUN CHECK ===")
teman_bau_input = input("Teman sebelah bau? (ya/tidak): ").strip().lower()
teman_sebelah_bau = teman_bau_input == "ya"

# Komentar sesuai tipe digital


if tipe == "wibu":
    komentar = f"bau bawang"
elif tipe == "gamers":
    komentar = f"Konten kamu pasti viral! Jangan lupa ajarin cara bikin video tentang {game_favorit}! 🎥✨"
elif tipe == "k-popers":
    komentar = f"Keren! Kamu bisa bikin game {game_favorit} versi kamu sendiri nih! 👨‍💻👾"
elif tipe == "anak konten":
    komentar = f"Skill edit kamu pasti keren! Video {game_favorit} kamu pasti cinematic banget! 🎬💻"
else:
    komentar = f"Wah, tipe digital kamu unik banget! Terus semangat dan berkarya ya! 🚀"

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

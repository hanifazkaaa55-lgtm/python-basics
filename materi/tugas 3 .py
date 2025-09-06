# ranking.py

def urutkan_nilai(nilai_list):
    return sorted(nilai_list, reverse=True)

def nilai_tertinggi(nilai_list):
    return max(nilai_list)

def nilai_terendah(nilai_list):
    return min(nilai_list)
# main.py

import ranking

# Daftar nilai
nilai = [75, 90, 60, 88, 100, 55]

# Menggunakan fungsi dari modul ranking
nilai_urut = ranking.urutkan_nilai(nilai)
tertinggi = ranking.nilai_tertinggi(nilai)
terendah = ranking.nilai_terendah(nilai)

# Menampilkan hasil
print("Nilai diurutkan (descending):", nilai_urut)
print("Nilai tertinggi:", tertinggi)
print("Nilai terendah:", terendah)
# main py.


print("materi 7C - python data structure") 
print("----------------------------------")

# set -> {} -> tidak berurutan, berubah, tidak duplikat
game_ridho = {"genshin", "mlbb", "delta force"}
game_imam = {"valorant", "poin blank"}

# .add() -> menambahkan item ke set
game_imam.add("valorant")  # jika sudah ada, tidak ditambahkan lagi (skip)
game_imam.add("mlbb")

# .remove() -> menghapus item dari set
game_ridho.remove("mlbb")  # jika tidak ada, akan error

# len() -> menghitung jumlah item dalam set
print("ridho ada", len(game_ridho), "=>", game_ridho)
print("imam ada", len(game_imam), "=>", game_imam)

# dictionary -> {key: value}
daftar_anime = {
    "jujutsu_kaisen": "gojo satoru",
    "one_punch_man": "saitama",
    "jigoku_raku": "sagiri",
    "naruto": "uzumaki naruto",
    "bleach": "ichigo kurosaki",
    "attack_on_titan": "eren yeager",
    "tokyo_revengers": "mikey",
    "demon_slayer": "kamado tanjiro",
    "spy_x_family": "anya forger",
    "black_clover": "asta",
    "my_hero_academia": "midoriya izuku",
    "death_note": "light yagami",
    "dragon_ball": "goku",
    "hunter_x_hunter": "gon freecss",
    "chainsaw_man": "denji"
} # menambah item value berdasarkan key

print("\ndaftar anime favorit:")
for judul, karakter in daftar_anime.items():
    print(f"{judul} => {karakter}")

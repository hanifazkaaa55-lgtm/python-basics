import json

print("materi 12 - json")
print("-----------------")
file_json_path = r"C:\Users\User\.vscode\rukun_islam.json"
with open(file_json_path, "r") as file_json:
    data_json = json.load(file_json)
    print(f"judul file: {data_json['judul']}")
    print(f"jumlah rukun islam: {data_json['jumlah']}")
    print(f"daftar rukun islam:")
    for item_rukun in data_json['rukun']:


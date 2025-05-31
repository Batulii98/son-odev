# şifre saklayıcı
from cryptography.fernet import Fernet
import json

# Şifreleme anahtarı (ilk çalışmada üret ve sakla)
def load_key():
    return open("key.key", "rb").read()

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Şifreleri sakla
def save_password(site, password):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())

    with open("vault.json", "r+") as file:
        try:
            data = json.load(file)
        except:
            data = {}
        data[site] = encrypted.decode()
        file.seek(0)
        json.dump(data, file, indent=2)

# Şifreyi göster
def get_password(site):
    key = load_key()
    f = Fernet(key)
    with open("vault.json", "r") as file:
        data = json.load(file)
        encrypted = data.get(site)
        if encrypted:
            print(f.decrypt(encrypted.encode()).decode())
        else:
            print("Şifre bulunamadı.")

# Menü
def main():
    while True:
        print("\n1. Şifre Ekle\n2. Şifre Görüntüle\n3. Çıkış")
        choice = input("Seçim: ")

        if choice == "1":
            site = input("Site: ")
            pwd = input("Şifre: ")
            save_password(site, pwd)
        elif choice == "2":
            site = input("Site adı: ")
            get_password(site)
        elif choice == "3":
            break

if name == "main":
    try:
        open("key.key")
    except:
        write_key()

    try:
        open("vault.json", "x").write("{}")
    except:
        pass

    main()
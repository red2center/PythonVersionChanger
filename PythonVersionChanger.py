import os
import subprocess
import shutil
import requests
import glob  # glob modülünü import ettik

# Bilgisayarınızdaki Python sürümlerini bulma ve silme fonksiyonu
def remove_python_versions():
    # Python'un yüklü olduğu klasörler
    paths_to_remove = [
        r"C:\Program Files\Python*",  # Program Files içinde Python
        r"C:\Program Files (x86)\Python*",  # Program Files (x86) içinde Python
        r"C:\Users\{}\AppData\Local\Programs\Python*".format(os.getlogin())  # Kullanıcıya özel Python
    ]

    # Yüklü Python'ları silme
    for path in paths_to_remove:
        for folder in glob.glob(path):  # glob modülü ile dosya yollarını arıyoruz
            print(f"Siliniyor: {folder}")
            try:
                shutil.rmtree(folder)  # Python klasörünü sil
            except Exception as e:
                print(f"Hata: {e}")

# İstenen Python sürümünü indirip kurma
def install_python(version):
    # Python'un resmi indirilen sayfası
    download_url = f"https://www.python.org/ftp/python/{version}/python-{version}-amd64.exe"
    download_path = f"python-{version}-installer.exe"

    # Python installer'ını indir
    print(f"{version} sürümü indiriliyor...")
    response = requests.get(download_url)
    with open(download_path, "wb") as f:
        f.write(response.content)
    print(f"{version} indirildi.")

    # Python installer'ını sessizce çalıştır
    print("Kurulum başlatılıyor...")
    subprocess.run([download_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)

    # İndirdiğimiz installer'ı sil
    os.remove(download_path)
    print(f"{version} başarıyla kuruldu.")

# Ana fonksiyon
def main():
    # Yüklü Python sürümlerini sil
    print("Python sürümleri siliniyor...")
    remove_python_versions()

    # Kullanıcıdan kurulacak sürümü alma
    version = input("Hangi Python sürümünü kurmak istersiniz (örnek: 3.8.0)? ")
    
    # Python sürümünü indirip kur
    install_python(version)

if __name__ == "__main__":
    main()

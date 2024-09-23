import os
import pandas as pd
import menu
from kitap_islem import *
from uye_islem import *
from takip import *

# Excel dosyasını kontrol et ve gerekirse işlemleri başlat
def check_files():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    if not os.path.exists(file_path):
        print(f"Excel dosyası '{file_path}' bulunamadı. Lütfen gerekli dosyaları hazırlayın.")
        return False
    return True

# Veritabanını yükleme işlemi
def load_database():
    try:
        file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
        df_books = pd.read_excel(file_path, sheet_name="Books")
        df_members = pd.read_excel(file_path, sheet_name="Members")
        df_tracking = pd.read_excel(file_path, sheet_name="Tracking")
        return df_books, df_members, df_tracking
    except Exception as e:
        print("Veritabanı yüklenirken bir hata oluştu:", e)
        return None, None, None

# Ana menü ve alt menülerde kullanılacak fonksiyonlar için yöntem listeleri
member_methods = {
    1: uye_listele,
    2: uye_ekle,
    3: uye_arama,
    4: uye_guncelle,
    5: uye_sil,
    6: kitap_ver,
    7: kitap_iade,
    8: uye_kitap_takibi
}

book_methods = {
    1: kitap_listele,
    2: kitap_ekle,
    3: kitap_arama,
    4: kitap_sil,
    5: kitap_ver
}

if __name__ == "__main__":
    if not check_files():
        exit()

    df_books, df_members, df_tracking = load_database()

    while True:
        try:
            menu.anamenu()
            choice = input("Lütfen yapmak istediğiniz işlemin kodunu giriniz : ")
            if choice == "0":
                break
            elif choice == "1":
                while True:
                    menu.uyemenu()
                    uyemenu_choice = int(
                        input(
                            "Üye menüsüne hoşgeldiniz\nLütfen yapmak istediğiniz işlemin kodunu giriniz : "
                        )
                    )
                    if uyemenu_choice == 9:
                        break
                    elif not 1 <= uyemenu_choice <= 8:
                        print("Geçersiz seçim!")
                    else:
                        member_methods[uyemenu_choice]()  # Seçilen fonksiyonu çağır
            elif choice == "2":
                while True:
                    menu.kitapmenu()
                    kitapmenu_choice = int(
                        input(
                            "Kitap menüsüne hoşgeldiniz\nLütfen yapmak istediğiniz işlemin kodunu giriniz : "
                        )
                    )
                    if kitapmenu_choice == 6:
                        break
                    elif not 1 <= kitapmenu_choice <= 5:
                        print("Geçersiz seçim!")
                    else:
                        book_methods[kitapmenu_choice]()  # Seçilen fonksiyonu çağır
            elif choice == "3":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim!")
                continue
        except Exception as e:
            print("Bir hata oluştu : ", e)
            continue

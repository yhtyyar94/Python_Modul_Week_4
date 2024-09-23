import pandas as pd

# Kitap listeleme fonksiyonu
def kitap_listele():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_books = pd.read_excel(file_path, sheet_name="Books")
    print("Kütüphanedeki kitaplar:")
    print(df_books)

# Kitap ekleme fonksiyonu
def kitap_ekle():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_books = pd.read_excel(file_path, sheet_name="Books")
    
    yeni_kitap = pd.DataFrame({
        "Barkod": [input("Kitap barkodunu giriniz: ")],
        "Dil": [input("Kitabın dilini giriniz: ")],
        "Fiyat": [float(input("Kitabın fiyatını giriniz: "))],
        "Kitap_Adi": [input("Kitabın adını giriniz: ")],
        "Yayinevi": [input("Yayınevini giriniz: ")],
        "Yazar": [input("Yazarın adını giriniz: ")]
    })
    
    # append yerine pd.concat kullanıyoruz
    df_books = pd.concat([df_books, yeni_kitap], ignore_index=True)
    
    df_books.to_excel(file_path, sheet_name="Books", index=False)
    print("Kitap başarıyla eklendi.")

# Kitap arama fonksiyonu
def kitap_arama():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_books = pd.read_excel(file_path, sheet_name="Books")
    kitap_adi = input("Aradığınız kitabın adını giriniz: ")
    sonuc = df_books[df_books['Kitap_Adi'].str.contains(kitap_adi, case=False, na=False)]
    if not sonuc.empty:
        print(sonuc)
    else:
        print("Kitap bulunamadı.")

# Kitap silme fonksiyonu
def kitap_sil():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_books = pd.read_excel(file_path, sheet_name="Books")
    kitap_barkod = input("Silmek istediğiniz kitabın barkodunu giriniz: ")
    df_books = df_books[df_books['Barkod'] != int(kitap_barkod)]
    df_books.to_excel(file_path, sheet_name="Books", index=False)
    print(f"{kitap_barkod} barkodlu kitap silindi.")

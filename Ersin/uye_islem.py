import pandas as pd

# Üye listeleme fonksiyonu
def uye_listele():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_members = pd.read_excel(file_path, sheet_name="Members")
    print("Kütüphanedeki üyeler:")
    print(df_members)

# Üye ekleme fonksiyonu
def uye_ekle():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_members = pd.read_excel(file_path, sheet_name="Members")
    
    # Yeni üye bilgilerini al
    yeni_uye = pd.DataFrame({
        "id": [len(df_members) + 1],
        "Uye adi": [input("Üyenin adını giriniz: ")],
        "Telefon": [input("Üyenin telefon numarasını giriniz: ")],
        "Adres": [input("Üyenin adresini giriniz: ")]
    })
    
    # DataFrame'e yeni üye ekle (pd.concat() ile)
    df_members = pd.concat([df_members, yeni_uye], ignore_index=True)
    
    # Excel dosyasına yaz
    df_members.to_excel(file_path, sheet_name="Members", index=False)
    print("Üye başarıyla eklendi.")

# Üye arama fonksiyonu
def uye_arama():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_members = pd.read_excel(file_path, sheet_name="Members")
    uye_adi = input("Aradığınız üyenin adını giriniz: ")
    sonuc = df_members[df_members['Uye adi'].str.contains(uye_adi, case=False, na=False)]
    if not sonuc.empty:
        print(sonuc)
    else:
        print("Üye bulunamadı.")

# Üye güncelleme fonksiyonu
def uye_guncelle():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_members = pd.read_excel(file_path, sheet_name="Members")
    uye_id = input("Güncellemek istediğiniz üyenin id'sini giriniz: ")
    uye = df_members[df_members['id'] == int(uye_id)]
    if not uye.empty:
        df_members.loc[df_members['id'] == int(uye_id), 'Uye adi'] = input("Yeni ad giriniz: ")
        df_members.loc[df_members['id'] == int(uye_id), 'Telefon'] = input("Yeni telefon giriniz: ")
        df_members.loc[df_members['id'] == int(uye_id), 'Adres'] = input("Yeni adres giriniz: ")
        df_members.to_excel(file_path, sheet_name="Members", index=False)
        print("Üye bilgileri güncellendi.")
    else:
        print("Üye bulunamadı.")

# Üye silme fonksiyonu
def uye_sil():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_members = pd.read_excel(file_path, sheet_name="Members")
    uye_id = input("Silmek istediğiniz üyenin id'sini giriniz: ")
    df_members = df_members[df_members['id'] != int(uye_id)]
    df_members.to_excel(file_path, sheet_name="Members", index=False)
    print(f"{uye_id} numaralı üye silindi.")

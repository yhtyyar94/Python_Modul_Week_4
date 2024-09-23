import pandas as pd

# Kitap ödünç verme işlemi
def kitap_ver():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_books = pd.read_excel(file_path, sheet_name="Books")
    df_members = pd.read_excel(file_path, sheet_name="Members")
    df_tracking = pd.read_excel(file_path, sheet_name="Tracking")

    uye_id = input("Kitap vereceğiniz üyenin id'sini giriniz: ")
    kitap_barkod = input("Vermek istediğiniz kitabın barkodunu giriniz: ")

    uye = df_members[df_members['id'] == int(uye_id)]
    kitap = df_books[df_books['Barkod'] == int(kitap_barkod)]

    if uye.empty or kitap.empty:
        print("Geçerli üye veya kitap bulunamadı.")
        return

    yeni_kayit = pd.DataFrame({
        "id": [len(df_tracking) + 1],
        "Uye Numarasi": [uye_id],
        "Uye Adi": [uye.iloc[0]['Uye adi']],
        "Tel": [uye.iloc[0]['Telefon']],
        "Adres": [uye.iloc[0]['Adres']],
        "Barkod": [kitap_barkod],
        "Dil": [kitap.iloc[0]['Dil']],
        "Fiyat": [kitap.iloc[0]['Fiyat']],
        "Kitap_Adi": [kitap.iloc[0]['Kitap_Adi']],
        "Yayinevi": [kitap.iloc[0]['Yayinevi']],
        "Yazar": [kitap.iloc[0]['Yazar']],
        "Kayit tarihi": pd.Timestamp.now().strftime('%d-%m-%Y'),
        "Kitap iade tarihi": [input("Kitap iade tarihini giriniz (GG-AA-YYYY): ")],
        "Iade durumu": [False]
    })

    df_tracking = pd.concat([df_tracking, yeni_kayit], ignore_index=True)
    df_tracking.to_excel(file_path, sheet_name="Tracking", index=False)
    print("Kitap başarıyla ödünç verildi.")

# Kitap iade işlemi
def kitap_iade():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_tracking = pd.read_excel(file_path, sheet_name="Tracking")
    takip_id = input("İade edilecek kaydın id'sini giriniz: ")

    takip = df_tracking[df_tracking['id'] == int(takip_id)]
    if not takip.empty:
        df_tracking.loc[df_tracking['id'] == int(takip_id), 'Iade durumu'] = True
        df_tracking.to_excel(file_path, sheet_name="Tracking", index=False)
        print("Kitap başarıyla iade edildi.")
    else:
        print("Geçerli kayıt bulunamadı.")

# Kitap takibi
def uye_kitap_takibi():
    file_path = r"c:/Git/Python_Modul_Week_2/Python_Modul_Week_2/pract-2/Python_Modul_Week_4/Ersin/library_database.xlsx"
    df_tracking = pd.read_excel(file_path, sheet_name="Tracking")
    uye_id = input("Takibini görmek istediğiniz üyenin id'sini giriniz: ")
    
    takip = df_tracking[df_tracking['Uye Numarasi'] == str(uye_id)]
    if not takip.empty:
        print(takip)
    else:
        print("Bu üye için kayıtlı bir takip bulunamadı.")

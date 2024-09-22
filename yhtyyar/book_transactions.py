import json


def list_all_books():
    try:
        with open("yhtyyar/books.json", "r") as file:
            books = json.load(file)
            if len(books) == 0:
                print("\033[91mKutuphanede kayitli kitap bulunmamaktadir.")
            else:
                print("\033[92mKutuphanede kayitli kitaplar:")
                print("-" * 50)
                for book in books:
                    # some book does not have price, so we need to check it
                    for keys in book:
                        print(f"{keys} : {book[keys]}")
                    print("-" * 50)
    except Exception as e:
        print("\033[91mBir hata olustu list all books : ", e)


def add_book():
    try:
        with open("yhtyyar/books.json", "r+") as file:
            books = json.load(file)
            book_name = input("Kitap adini giriniz : ")
            author = input("Yazar adini giriniz : ")
            publisher = input("Yayinevi adini giriniz : ")
            price = float(input("Fiyatini giriniz : "))
            barcode = int(input("Barkod numarasini giriniz : "))
            language = input("Dilini giriniz : ")

            if barcode in [book["Barkod"] for book in books]:
                print("\033[91mBu barkod numarasi zaten kullanilmaktadir.")
            else:
                books.append(
                    {
                        "Dil": language,
                        "Barkod": barcode,
                        "Fiyat": price,
                        "Kitap_Adi": book_name,
                        "Yayinevi": publisher,
                        "Yazar": author,
                    }
                )
                file.seek(0)
                json.dump(obj=books, fp=file, indent=4)
                print("\033[92mKitap basariyla eklendi.")
    except Exception as e:
        print("\033[91mBir hata olustu add book : ", e)


def search_book():
    try:
        with open("yhtyyar/books.json", "r") as file:
            books = json.load(file)
            search_text = input(
                "Aramak istediginiz kitap icin anahtar kelima ya da barkod numarasi girin : "
            )
            counter = 0
            for book in books:
                if (
                    search_text.lower() in book["Kitap_Adi"].lower()
                    or search_text.lower() in book["Yazar"].lower()
                    or search_text.lower() in book["Yayinevi"].lower()
                    or search_text.lower() in str(book["Barkod"]).lower()
                ):
                    counter += 1
                    for keys in book:
                        print(f"{keys} : {book[keys]}")
                    print("-" * 50)
            if counter == 0:
                print("\033[91mAranan kitap bulunamadi.")
            else:
                print(f"{counter} adet kitap bulundu.")
    except Exception as e:
        print("\033[91mBir hata olustu search book : ", e)


def delete_book():
    try:
        with open("yhtyyar/books.json", "r") as file:
            books = json.load(file)
            barcode = input("Silmek istediginiz kitabin barkod numarasini girin : ")

            for book in books:
                if str(book["Barkod"]).lower() == barcode:
                    books.remove(book)
                    with open("yhtyyar/books.json", "w") as file:
                        json.dump(books, file)
                        print("\033[92mKitap basariyla silindi.")
                        for keys in book:
                            print(f"{keys} : {book[keys]}")
                        print("-" * 50)
                    break
            else:
                print("\033[91mKitap bulunamadi.")
    except Exception as e:
        print("\033[91mBir hata olustu delete book : ", e)


book_methods = {
    1: list_all_books,
    2: add_book,
    3: search_book,
    4: delete_book,
}

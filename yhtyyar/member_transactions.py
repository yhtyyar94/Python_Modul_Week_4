import json
from get_transaction_time import transaction_start_end_time


def list_all_members():
    try:
        with open("yhtyyar/members.json", "r") as file:
            members = json.load(file)
            if len(members["members"]) == 0:
                print("\033[91mUye bulunmamaktadir.")
            else:
                print("Uyeler:")
                print("-" * 50)
                for member in members["members"]:
                    for keys in member:
                        print(f"{keys} : {member[keys]}")
                    print("-" * 50)
    except Exception as e:
        print("\033[91mBir hata olustu list all members : ", e)


def add_member():
    try:
        with open("yhtyyar/members.json", "r") as file:
            members = json.load(file)
            new_member = {}
            if len(members["deleted_member_ids"]) != 0:
                new_member["id"] = members["deleted_member_ids"].pop()
            else:
                new_member["id"] = members["new_member_id"]
                members["new_member_id"] += 1
            new_member["Uye adi"] = input("Uye adi girin : ")
            new_member["Telefon"] = input("Uye telefon numarasi girin : ")
            new_member["Adres"] = input("Uye adresi girin : ")
            members["members"].append(new_member)
            with open("yhtyyar/members.json", "w") as file:
                json.dump(members, file)
                print("\033[92mUye basariyla eklendi.")
    except Exception as e:
        print("\033[91mBir hata olustu add member : ", e)


def search_member():
    try:
        with open("yhtyyar/members.json", "r") as file:
            members = json.load(file)
            search_text = input(
                "Aramak istediginiz uye icin anahtar kelima ya da uye numarasi girin : "
            )
            counter = 0
            for member in members["members"]:
                if (
                    search_text.lower() in member["Uye adi"].lower()
                    or search_text.lower() in member["Telefon"].lower()
                    or search_text.lower() in member["Adres"].lower()
                    or search_text.lower() in str(member["id"]).lower()
                ):
                    counter += 1
                    for keys in member:
                        print(f"{keys} : {member[keys]}")
                    print("-" * 50)
            if counter == 0:
                print("\033[91mAranan uye bulunamadi.")
            else:
                print(f"\033[92m{counter} adet uye bulundu.")
    except Exception as e:
        print("\033[91mBir hata olustu search member : ", e)


def delete_member():
    try:
        with open("yhtyyar/members.json", "r") as file:
            members = json.load(file)
            member_id = input("Silmek istediginiz uyenin numarasini girin : ")

            for member in members["members"]:
                if str(member["id"]).lower() == member_id:
                    members["members"].remove(member)
                    members["deleted_member_ids"].append(member["id"])
                    with open("yhtyyar/members.json", "w") as file:
                        json.dump(members, file)
                        print("\033[92mUye basariyla silindi.")
                        for keys in member:
                            print(f"{keys} : {member[keys]}")
                        print("-" * 50)
                    break
            else:
                print("\033[91mUye bulunamadi.")
    except Exception as e:
        print("\033[91mBir hata olustu delete member : ", e)


def book_lending():
    try:
        with open("yhtyyar/books.json", "r") as books_file:
            with open("yhtyyar/members.json", "r") as members_file:
                books = json.load(books_file)
                members = json.load(members_file)
                barcode = input(
                    "Odunc vermek istediginiz kitabin barkod numarasini girin : "
                )
                member_id = input("Kitabi alacak uyenin numarasini girin : ")

                if barcode not in [str(book["Barkod"]) for book in books]:
                    print("\033[91mKitap bulunamadi.")
                elif member_id not in [
                    str(member["id"]) for member in members["members"]
                ]:
                    print("\033[91mUye bulunamadi.")
                else:
                    with open("yhtyyar/tracking.json", "r") as tracking_file:
                        tracking = json.load(tracking_file)
                        if barcode in [
                            str(transaction["Barkod"])
                            for transaction in tracking["transactions"]
                            if transaction["Iade durumu"] == False
                        ]:

                            print(
                                "\033[91mKitap zaten odunc verilmis. Lutfen baska bir kitap secin."
                            )
                            return
                        member = [
                            member
                            for member in members["members"]
                            if str(member["id"]) == member_id
                        ][0]
                        book = [
                            book for book in books if str(book["Barkod"]) == barcode
                        ][0]
                        new_transaction = {}
                        new_transaction["id"] = tracking["new transaction id"]
                        tracking["new transaction id"] += 1
                        new_transaction["Uye Numarasi"] = member_id
                        new_transaction["Uye Adi"] = member["Uye adi"]
                        new_transaction["Tel"] = member["Telefon"]
                        new_transaction["Adres"] = member["Adres"]
                        new_transaction["Barkod"] = barcode
                        for keys in book:
                            new_transaction[keys] = book[keys]
                        new_transaction["Kayit tarihi"] = transaction_start_end_time()[
                            0
                        ]
                        new_transaction["Kitap iade tarihi"] = (
                            transaction_start_end_time()[1]
                        )
                        new_transaction["Iade durumu"] = False

                        tracking["transactions"].append(new_transaction)
                        with open("yhtyyar/tracking.json", "w") as tracking_file:
                            json.dump(tracking, tracking_file)
                            print("\033[92mKitap basariyla odunc verildi.")

    except Exception as e:
        print("\033[91mBir hata olustu book lending : ", e)


def book_return():
    try:
        with open("yhtyyar/tracking.json", "r") as file:
            tracking = json.load(file)
            barcode = input(
                "Iadesini yapmak istediginiz kitabin barkod numarasini girin : "
            )
            for transaction in tracking["transactions"]:
                if (
                    str(transaction["Barkod"]) == barcode
                    and not transaction["Iade durumu"]
                ):
                    transaction["Iade durumu"] = True
                    with open("yhtyyar/tracking.json", "w") as file:
                        json.dump(tracking, file)
                        print("\033[92mKitap basariyla iade edildi.")
                    break
            else:
                print("\033[91mKitap bulunamadi ya da zaten iade edilmis.")
    except Exception as e:
        print("\033[91mBir hata olustu book return : ", e)


def list_all_not_returned_books():
    try:
        with open("yhtyyar/tracking.json", "r") as file:
            tracking = json.load(file)
            counter = 0
            for transaction in tracking["transactions"]:
                if not transaction["Iade durumu"]:
                    counter += 1
                    for keys in transaction:
                        print(f"{keys} : {transaction[keys]}")
                    print("-" * 50)
            if counter == 0:
                print("\033[92mIadesi gecikmis kitap bulunmamaktadir.")
            else:
                print(f"\033[92m{counter} adet kitap iadesi gecikmis.")
    except Exception as e:
        print("\033[91mBir hata olustu list all not returned books : ", e)


member_methods = {
    1: list_all_members,
    2: add_member,
    3: search_member,
    4: delete_member,
    5: book_lending,
    6: book_return,
    7: list_all_not_returned_books,
}

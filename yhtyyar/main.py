import os
import json
import menu
from book_transactions import book_methods
from member_transactions import member_methods


def check_files():
    if not os.path.exists("books.json"):
        with open("books.json", "w") as file:
            json.dump([], file)
    if not os.path.exists("members.json"):
        with open("members.json", "w") as file:
            json.dump(
                {"new_member_id": 1, "deleted_member_ids": [], "members": []}, file
            )
    if not os.path.exists("tracking.json"):
        with open("tracking.json", "w") as file:
            json.dump({"new transaction id": 1, "transactions": []}, file)


if __name__ == "__main__":
    check_files()
    while True:
        try:
            menu.main_menu()
            choice = input("Lutfen yapmak istediginiz islemin kodunu giriniz : ")
            if choice == "0":
                break
            elif choice == "1":
                while True:
                    menu.member_menu()
                    member_menu_choice = int(
                        input(
                            "Uye menusune hosgeldiniz\nLutfen yapmak istediginiz islemin kodunu giriniz : "
                        )
                    )
                    if member_menu_choice == 0:
                        break
                    elif not 1 <= member_menu_choice <= 7:
                        print("Gecersiz secim!")
                        menu.member_menu()
                        choice = int(
                            input(
                                "Uye menusune hosgeldiniz\nLutfen yapmak istediginiz islemin kodunu giriniz : "
                            )
                        )
                    else:
                        member_methods[member_menu_choice]()
            elif choice == "2":
                while True:
                    menu.book_menu()
                    book_menu_choice = int(
                        input(
                            "Kitap menusune hosgeldiniz\nLutfen yapmak istediginiz islemin kodunu giriniz : "
                        )
                    )
                    if book_menu_choice == 0:
                        break
                    elif not 1 <= book_menu_choice <= 4:
                        print("Gecersiz secim!")
                        menu.book_menu()
                        choice = int(
                            input(
                                "Kitap menusune hosgeldiniz\nLutfen yapmak istediginiz islemin kodunu giriniz : "
                            )
                        )
                    else:
                        book_methods[book_menu_choice]()
            else:
                print("Gecersiz secim!")
                continue
        except Exception as e:
            print("Bir hata olustu : ", e)
            continue

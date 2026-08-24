# import math
#
# FILENAME = "students.txt"
#
#
# def add_student(name, scores):
#     scores_str = ",".join(scores)
#     line = name + "," + scores_str + "\n"
#     file = open(FILENAME, "a")
#     file.write(line)
#     file.close()
#
#
# def get_all_students():
#     students_list = []
#     try:
#         file = open(FILENAME, "r")
#         lines = file.readlines()
#         file.close()
#
#         for line in lines:
#             line = line.strip()
#             if line != "":
#                 parts = line.split(",")
#                 name = parts[0]
#                 scores = []
#                 for score in parts[1:]:
#                     scores.append(float(score))
#
#                 student = {
#                     "name": name,
#                     "scores": scores
#                 }
#                 students_list.append(student)
#     except FileNotFoundError:
#         pass
#
#     return students_list
#
#
# def show_students():
#     students = get_all_students()
#     if len(students) == 0:
#         print("სტუდენტები ვერ მოიძებნა.")
#     else:
#         for student in students:
#             scores_str = ", ".join(str(s) for s in student["scores"])
#             print("სტუდენტი: " + student["name"] + " | ქულები: " + scores_str)
#
#
# def calculate_average(scores):
#     if len(scores) == 0:
#         return 0
#     total = sum(scores)
#     average = total / len(scores)
#     return math.floor(average * 100) / 100
#
#
# def find_best_student():
#     students = get_all_students()
#     if len(students) == 0:
#         print("სტუდენტები ვერ მოიძებნა.")
#         return None
#
#     best_student = None
#     highest_average = -1
#
#     for student in students:
#         avg = calculate_average(student["scores"])
#         if avg > highest_average:
#             highest_average = avg
#             best_student = student
#
#     if best_student != None:
#         print("საუკეთესო სტუდენტი: " + best_student["name"] + " | საშუალო ქულა: " + str(highest_average))
#
#     return best_student
#
#
# def main():
#     while True:
#         print("\n===== სტუდენტების მენეჯერი =====")
#         print("1. სტუდენტის დამატება")
#         print("2. ყველა სტუდენტის ნახვა")
#         print("3. საშუალო ქულების დათვლა")
#         print("4. საუკეთესო სტუდენტის პოვნა")
#         print("5. გამოსვლა")
#
#         choice = input("აირჩიეთ მოქმედება (1-5): ").strip()
#
#         if choice == "1":
#             name = input("შეიყვანეთ სტუდენტის სახელი: ").strip()
#             scores_input = input("შეიყვანეთ ქულები მძიმით გამოყოფილი (მაგ: 90,85,100): ").strip()
#
#             scores_list = scores_input.split(",")
#             add_student(name, scores_list)
#             print("სტუდენტი წარმატებით დაემატა!")
#
#         elif choice == "2":
#             print("\n--- სტუდენტების სია ---")
#             show_students()
#
#         elif choice == "3":
#             print("\n--- საშუალო ქულები ---")
#             students = get_all_students()
#             if len(students) == 0:
#                 print("სია ცარიელია.")
#             else:
#                 for student in students:
#                     avg = calculate_average(student["scores"])
#                     print(student["name"] + ": " + str(avg))
#
#         elif choice == "4":
#             print("\n--- საუკეთესო სტუდენტი ---")
#             find_best_student()
#
#         elif choice == "5":
#             print("პროგრამის დასასრული.")
#             break
#
#         else:
#             print("არასწორი არჩევანი, სცადეთ თავიდან.")
#
#
# main()


FILENAME = "products.csv"


def get_all_products():
    products_list = []
    try:
        file = open(FILENAME, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                if len(parts) == 2:
                    name = parts[0].strip()
                    try:
                        price = float(parts[1].strip())
                        products_list.append({"name": name, "price": price})
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass

    return products_list


def add_product():
    print("\n--- პროდუქტის დამატება ---")
    name = input("შეიყვანეთ პროდუქტის დასახელება: ").strip()
    if name == "":
        print("შეცდომა: დასახელება ცარიელი ვერ იქნება!")
        return

    price_input = input("შეიყვანეთ ფასი: ").strip()
    try:
        price = float(price_input)
        if price <= 0:
            print("შეცდომა: ფასი უნდა იყოს 0-ზე მეტი!")
            return

        line = name + "," + str(price) + "\n"
        file = open(FILENAME, "a")
        file.write(line)
        file.close()
        print("პროდუქტი წარმატებით დაემატა!")

    except ValueError:
        print("შეცდომა: ფასი უნდა იყოს რიცხვი!")


def show_products():
    print("\n--- პროდუქტების სია ---")
    products = get_all_products()

    if len(products) == 0:
        print("პროდუქტები ვერ მოიძებნა ან ფაილი ცარიელია.")
    else:
        for p in products:
            print("პროდუქტი: " + p["name"] + " | ფასი: " + str(p["price"]) + " GEL")


def search_product():
    print("\n--- პროდუქტის ძებნა ---")
    search_name = input("შეიყვანეთ მოსაძებნი პროდუქტი: ").strip().lower()

    if search_name == "":
        print("შეცდომა: საძიებო სიტყვა ცარიელია!")
        return

    products = get_all_products()
    found = False

    for p in products:
        if p["name"].lower() == search_name:
            print("ნაპოვნია! " + p["name"] + " | ფასი: " + str(p["price"]) + " GEL")
            found = True
            break

    if not found:
        print("პროდუქტი ვერ მოიძებნა!")


def buy_product():
    print("\n--- პროდუქტის ყიდვა ---")
    buy_name = input("შეიყვანეთ პროდუქტი, რომლის ყიდვაც გსურთ: ").strip().lower()

    if buy_name == "":
        print("შეცდომა: დასახელება ცარიელია!")
        return

    products = get_all_products()
    found = False

    for p in products:
        if p["name"].lower() == buy_name:
            found = True
            qty_input = input("შეიყვანეთ რაოდენობა: ").strip()
            try:
                qty = int(qty_input)
                if qty <= 0:
                    print("შეცდომა: რაოდენობა უნდა იყოს 0-ზე მეტი!")
                    return

                total_cost = p["price"] * qty
                print("გადასახდელი თანხა (" + p["name"] + " x " + str(qty) + "): " + str(total_cost) + " GEL")

            except ValueError:
                print("შეცდომა: რაოდენობა უნდა იყოს მთელი რიცხვი!")
            break

    if not found:
        print("პროდუქტი ვერ მოიძებნა!")


def calculate_total():
    print("\n--- ჯამური ღირებულება ---")
    products = get_all_products()

    if len(products) == 0:
        print("ფაილში პროდუქტები არ არის.")
    else:
        total = 0
        for p in products:
            total = total + p["price"]
        print("ყველა პროდუქტის ჯამური ღირებულება: " + str(total) + " GEL")


def main():
    while True:
        print("\n===== PRODUCT SYSTEM =====")
        print("1. Add product")
        print("2. Show products")
        print("3. Search product")
        print("4. Buy product")
        print("5. Calculate total")
        print("6. Exit")

        choice = input("აირჩიეთ მოქმედება (1-6): ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            show_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            buy_product()
        elif choice == "5":
            calculate_total()
        elif choice == "6":
            print("პროგრამის დასასრული.")
            break
        else:
            print("არასწორი არჩევანი, სცადეთ თავიდან.")


main()
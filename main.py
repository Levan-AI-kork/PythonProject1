# 1, 2, 7, 8. მშობელი კლასი Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name

        # ფასის ვალიდაცია staticmethod-ით
        if Product.is_valid_price(price):
            self.price = price
        else:
            print("შეცდომა: ფასი არ შეიძლება იყოს უარყოფითი!")
            self.price = 0

        # private ატრიბუტი
        self.__quantity = 0
        self.quantity = quantity  # იყენებს setter-ს ვალიდაციისთვის

    # @property და @quantity.setter
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self.__quantity = value
        else:
            print("შეცდომა: რაოდენობა არ შეიძლება იყოს 0-ზე ნაკლები!")

    # რაოდენობის დამატება
    def add_quantity(self, amount):
        if amount > 0:
            self.__quantity += amount
        else:
            print("შეცდომა: დასამატებელი რაოდენობა უნდა იყოს დადებითი!")

    # რაოდენობის შემცირება
    def remove_quantity(self, amount):
        if amount <= 0:
            print("შეცდომა: მოსაკლები რაოდენობა უნდა იყოს დადებითი!")
        elif self.__quantity - amount < 0:
            print("შეცდომა: მარაგში არ არის საკმარისი რაოდენობა!")
        else:
            self.__quantity -= amount

    # საბოლოო ფასის გამოთვლა (საბაზო მეთოდი)
    def get_final_price(self):
        return self.price

    # @staticmethod ფასის შემოწმებისთვის
    @staticmethod
    def is_valid_price(price):
        return price >= 0

    # @classmethod ალტერნატიული კონსტრუქტორი
    @classmethod
    def from_string(cls, data):
        # მონაცემების დაშლა split-ით
        parts = data.split(",")
        name = parts[0]
        price = float(parts[1])
        quantity = int(parts[2])
        return cls(name, price, quantity)

    # __str__ მეთოდი
    def __str__(self):
        return (f"Product: {self.name}\n"
                f"Price: {self.price} GEL\n"
                f"Quantity: {self.quantity}\n"
                f"Final Price: {self.get_final_price()} GEL")


# 3 & 4. შვილობილი კლასები და პოლიმორფიზმი

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty_years):
        super().__init__(name, price, quantity)
        self.warranty_years = warranty_years

    # get_final_price მეთოდის გადაწერა (18% გადასახადი)
    def get_final_price(self):
        return round(self.price * 1.18, 2)

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nWarranty: {self.warranty_years} years"


class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    # get_final_price მეთოდის გადაწერა (10% ფასდაკლება)
    def get_final_price(self):
        return round(self.price * 0.90, 2)

    def __str__(self):
        return (f"Product: {self.name}\n"
                f"Price: {self.price} GEL\n"
                f"Size: {self.size}\n"
                f"Quantity: {self.quantity}\n"
                f"Final Price: {self.get_final_price()} GEL")


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    # get_final_price მეთოდის გადაწერა (ფასი უცვლელია)
    def get_final_price(self):
        return self.price

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nExpiration Date: {self.expiration_date}"


# 6. შეკვეთის მთლიანი თანხის დათვლა
def calculate_order(products):
    total = 0
    for product in products:
        # თითოეული პროდუქტის საბოლოო ფასი გამრავლებული რაოდენობაზე
        total += product.get_final_price() * product.quantity
    return f"Total: {round(total, 2)} GEL"


# 9. პროდუქტის მოძებნა სახელის მიხედვით
def find_product(products, name):
    for product in products:
        if product.name.lower() == name.lower():
            print("Product found!")
            return product
    print("Product not found!")
    return None


# =========================================================
# 10. საბოლოო პროგრამის ტესტირება და გაშვება
# =========================================================

# პროდუქტების შექმნა
laptop = Electronics("Laptop", 2000, 5, 2)
shirt = Clothing("T-Shirt", 100, 10, "L")
pizza = Food("Pizza", 20, 20, "2026-09-10")

# სიის შექმნა
products = [laptop, shirt, pizza]

print("--- პროდუქტების ინფორმაცია (__str__ და პოლიმორფიზმი) ---")
for product in products:
    print(product)
    print("-" * 30)

print("\n--- შეკვეთის მთლიანი თანხა ---")
print(calculate_order(products))

print("\n--- მარაგის შემცირება ---")
print(f"საწყისი რაოდენობა: {laptop.quantity}")
laptop.remove_quantity(2)
print(f"ახალი რაოდენობა remove_quantity(2)-ის შემდეგ: {laptop.quantity}")

print("\n--- classmethod-ის შემოწმება ---")
string_product = Product.from_string("Tablet,800,3")
print(string_product)

print("\n--- staticmethod-ის შემოწმება ---")
print("არის თუ არა 500 ვალიდური ფასი?:", Product.is_valid_price(500))
print("არის თუ არა -100 ვალიდური ფასი?:", Product.is_valid_price(-100))

print("\n--- პროდუქტის ძებნა ---")
find_product(products, "Laptop")
find_product(products, "Phone")
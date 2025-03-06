#product_Detials

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def product_details(self):
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")

class Electronics(Product):
    def electronic_info(self):
        print(f"{self.name} is an electronic item.")

class Clothing(Product):
    def clothing_info(self):
        print(f"{self.name} is a clothing item.")


laptop = Electronics("Laptop", 75000, "Electronics")
shirt = Clothing("Shirt", 1500, "Clothing")

laptop.product_details()
laptop.electronic_info()

shirt.product_details()
shirt.clothing_info()
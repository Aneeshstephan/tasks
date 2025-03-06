# vehicle genaralinfo

class Vehicle:
    def general_info(self, brand, model, year):
        print(f"This is a {year} {brand} {model}")

class Car(Vehicle):
    def car_info(self):
        print("This is a car")

class Bike(Vehicle):
    def bike_info(self):
        print("This is a bike")

car = Car()
bike = Bike()

car.general_info("Toyota", "Corolla", 2022)
car.car_info()

bike.general_info("Honda", "CBR", 2021)
bike.bike_info()




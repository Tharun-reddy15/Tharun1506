#1. Create a base class Vehicle with a method start()
class Vehicle:
    def start(self):
        print("Vehicle is starting...")
my_vehicle = Vehicle()
my_vehicle.start()

#2. Create a derived class Car that inherits from Vehicle
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Example usage:
my_car = Car("Toyota", "Camry")
my_car.start()
my_car.display_details()

#3. Add a class variable to track the number of vehicles created
class Vehicle:
    vehicle_count = 0  # class variable to track vehicle count

    def __init__(self):
        Vehicle.vehicle_count += 1  # increment count when a vehicle is created

    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__()  # call Vehicle's __init__ to increment count
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

#4. Demonstrate single inheritance and multilevel inheritance with appropriate classes
# Single Inheritance
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Multilevel Inheritance
# Single Inheritance
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Multilevel Inheritance
class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__()
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

    def display_battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

class ElectricCar(ElectricVehicle):
    def __init__(self, brand, model, battery_capacity, range):
        super().__init__(brand, model, battery_capacity)
        self.range = range

    def display_range(self):
        print(f"Range: {self.range} km")
my_car = Car("Toyota", "Camry")
my_car.start()
my_car.display_details()

print("\n")

my_electric_car = ElectricCar("Tesla", "Model S", 100, 500)
my_electric_car.start()
my_electric_car.display_details()
my_electric_car.display_battery_info()
my_electric_car.display_range()

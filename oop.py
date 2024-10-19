"""

The key concepts of OOP are encapsulation, inheritance, and polymorphism.
An object bundles reelated attributes or properties(variables) and can perform actions (behaviours) which are called methodss in classes.
Class is a blueprint used to design the structure or laout of the object.

"""

class Car:
    def __init__(self, brand, model, year, engine_type):
        print("I always run first")
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_type = engine_type

    # ACTIONS
    def start(self):
        print(f"{self.brand} {self.model} is starting")

    def stop_car(self):
        print(f"{self.brand} {self.model} is stopping")

    def driving(self):
        print(f"{self.brand} is {self.model} is driving with a {self.engine_type} engine")

car1 = Car("Toyota", "Camry", 2024, "V6")
car2 = Car("Toyota", "Sienna", 2023, "v4")

print(car1.brand, car1.model, car1.year, car1.engine_type)
print(car2.brand, car2.model, car2.year, car2.engine_type)

car1.stop_car()
car2.stop_car()
car1.driving()


class Phone:
    def __init__(self, brand, year, operating_system, price):
        self.brand = brand
        self.year = year
        self.operating_system = operating_system
        self.price = price

phone1 = Phone("Iphone", 2024, "IOS18", 2650500)
phone2 = Phone("Nokia", 2023, "Windows", 750000)
phone3 = Phone("Samsung", 2023, "Tinzen", 1500000)

print(f"The {phone1.brand} is the most expensive phone on the list.")
print(f"It costs {phone1.price} Naira and came out in the year {phone1.year}.")
print(f"The {phone1.brand} uses an {phone1.operating_system} OS.")


class Player:
        def __init__(self, name, hp=100):
            self.name = name
            self.hp = hp
        
        def run(self):
            return f"{self.name} is running in the game."
        
        def take_damage(self, damage):
            self.hp -= damage  # Reduce hit points by damage amount
            return f"{self.name}'s remaining HP: {self.hp}"

# Create a player
player1 = Player("John")

# Take 20 points of damage
print(player1.take_damage(20))

"""
ENCAPSULATION
This is the practice of wrapping data (attributes) and methods
(functions) into a single unit, or a class.  It allows control over how the 
data is accessed or modified by exposing only selected information
while hiding the rest (like private variables)

Basic Concept: Protects object data from outside interference by restricting access.

INHERITANCE
This allows a new class (child or deriverd class) to inherit properties and behaviours
(attributes andd methods) from an existing class (parent or base class).


"""

# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = name

    def sound(self):
        print(f"{self.name} is making a sound")

    def eat(self):
        print(f"{self.name} is eating")

class Cat(Animal):
    def __init__(self, name, species, family):
        super().__init__(name, species)
        self.family = family

    def sound(self):
        print(f"{self.name} is making the sound Meow.")

    def eat(self):
        print(f"{self.name} is licking milk.")

class Goat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def sound(self):
        print(f"{self.name} is bleating Mehhhhhhhhhh!!!!!!.")

    def eat(self):
        print(f"{self.name} is regurgitating it's food.")

cat1 = Cat("Whiskers", "Mammal", "Felidae")

cat1.sound()
cat1.eat()

goat1 = Goat("Ahmed", "Mammal", "Abaza")

goat1.sound()
goat1.eat()
goat1.breed
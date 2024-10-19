class Animal:
    def __init__(self, name, family, feeding_habit, habitat):
        self.name = name
        self.family = family
        self.feeding_habit = feeding_habit
        self.habitat = habitat

    def animal_sound(self):
        print(f"The {self.name} is making a sound")


    def sleep(self):
        return f"The {self.name} is sleeping"


    def eat(self):
        return f"The {self.name} is eating"

animal1 = Animal("Dog", "Canidae", "Ominivore", "The Home")
animal2 = Animal("Lion", "Panthera", "Canivore", "The Wild")
animal3 = Animal("Python", "Pythonidae", "Carnivore", "The Evil forest")
animal4 = Animal("Sardine", "Clupeidae", "Herbivore", "Water")

print(f"The {animal2.name} lives in {animal2.habitat}")

animal1.eat()
animal3.sleep()
animal4.animal_sound()
animal1_eat = animal1.eat()

print(f"{animal1_eat} in {animal1.habitat}")

print(animal1_eat)
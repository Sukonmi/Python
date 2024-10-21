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

print("My name is Olabimitan Daniel Ayomide "
    "I am a student of GoMyCode Abuja "
    "I am studying Data Science "
    "The name of my instructor is Samuel Okon ")

sound = "Ha"

print(sound * 3)

print(f"{12345678:,d}")
print(f"{12345678:10d}")
print(f"{12345678:010d}")
print(f"{9}:{5:02d}pm")

import math

print(f"{math.pi:f}")
print(f"{math.pi:4f}")
print(f"{math.pi:8.4f}")
print(f"{math.pi:08.4f}")

start_hour = int(input("Starting hour: "))
start_min = int(input("Starting minute: "))
stop_hour = int(input("Stopping hour: "))
stop_min = int(input("Stopping minute: "))
rate = float(input("Hourly rate: "))

start_time = f"{start_hour}:{start_min:2d}"
stop_time = f"{stop_hour}:{stop_min:02d}"

total_hours = stop_time - start_time
payment = total_hours * rate

print(f"Worked: {start_time} to {stop_time}")
print(f"Total hours: {total_hours}")
print(f"Payment: ${payment}")
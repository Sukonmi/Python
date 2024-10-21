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

class BankAccount:
    def __init__(self, owner, phone_number, email_address, account_number, balance=0):
        self.owner = owner
        self.phone_number = phone_number
        self.email_address = email_address
        self.account_nummber = account_number
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Alert!!! {deposit_amount}Naira has been credited to your account.")
        
    def check_balance(self):
        print(f"Hi {self.owner}. Your balance is: {self.balance}Naira")

    def withdraw(self, withdrawal_amount):
        self.balance -= withdrawal_amount
        print(f"Debit Alert!!! {withdrawal_amount}Naira has been debited from your account.")

    def update_acc_email(self, new_email_address):
        self.email_address = new_email_address
        print(f"Your Email has been updated to {new_email_address}")

    def account_info(self):
        print(f"Good day, Mr {self.owner}. \n"
              f"These are your available information. \n"
              f"Account number: {self.account_nummber} \n"
              f"Phone number: {self.phone_number} \n"
              f"Email address: {self.email_address} \n"
              f"Account balance: {self.balance}Naira")

account1 = BankAccount("Ayomide", "07067159089", "Ayo@gmail.com", "1513855560")

print(f"Good Afternoon, Mr {account1.owner} "
      f"Your account number is {account1.account_nummber} "
      f"And your balance is {account1.balance} Naira")

account1.deposit(100000)
account1.deposit(5000)
account1.check_balance()
account1.deposit(2000000)
account1.check_balance()
account1.withdraw(150000)
account1.check_balance()
account1.account_info()
account1.update_acc_email("Ayo_d@yahoomail.com")
account1.account_info()


class Player:
        def __init__(self, name, hp=100):
            self.name = name
            self.hp = hp
        
        def run(self):
            print(f"{self.name} is running in the game.")
        
        def take_damage(self, damage):
            self.hp -= damage  # Reduce hit points by damage amount
            print(f"{self.name}'s remaining HP: {self.hp}")
            if self.hp < 20 and self.hp != 0:
                print(f"{self.name}. Your HP: {self.hp} Get health boost to avoid death")
            elif self.hp == 0:
                print(f"{self.name} You are dead")
            else:
                pass

        def recover(self, health_boost):
            self.hp += health_boost
            print(f"{self.name}'s new HP: {self.hp}")

# Create a player
player1 = Player("John")
player2 = Player("Kester")
player3 = Player("Ayomide")

player1.take_damage(20)
player2.run()
player2.take_damage(50)
player3.take_damage(0)
player2.recover(10)
player2.take_damage(50)
player2.take_damage(10)
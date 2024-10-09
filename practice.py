print("Hello World")
print("My name is Ayomide Daniel")
print("Ayomide","Kester","Kaybee", sep="*")
print("Ayomide", end=" ")
print("Daniel")


# VARIABLES

# Snake casing
First_name = "Ayomide"

# Camel casing
lastName = "Daniel"

# Datatype
wine_id = 12

degree = 2.35

age  = "9"

print(type(wine_id), type(degree), type(age))

# String Concatination
firstName = "Ayomide"
lastName = "Daniel"
age  = "2"

all_name = firstName + " " + " is " + age  + "years old!"

print(all_name)

num1 = 3
num2 = 5

# Addition
total_score = num1 + num2

print(total_score)

# multiplication
multiplication_result = num1 * num2

print(multiplication_result)

# Division
division_result =  num2 / num1

print(division_result)

# exponent 
exponential_result = num2 ** num1

print(exponential_result)

user_name = input("What's your name: ")
print("welcome to GoMyCode" + user_name)

user_name = input("What is your name: ")
num1 = int(input("Input one number: "))
num2 = int(input("Input another number: "))

total_score = num1 + num2
dif_btw_score = num2 - num1
multip_result = num1 * num2
div_result = num2 // num1
exp_result = num2 ** num1
print(f"Welcome to Gomycalculator {user_name}. This are your results: {total_score}, {dif_btw_score}, {multip_result}, {div_result}, {exp_result}. Thank you for using Gomycalculator!")


userName = "Ayomide"
question1 = input("What city did you grow up in? \n")
question2 = input("What wouold you name your pet if you had one? \n")

bandName = question1 + question2

print(f"Namaste, {userName}. Your bandName is {bandName}. Thank you for using Bandnamtion.")


age = int(input("How old are you? \n"))
qualification = input("What is your highest qualification? \n")

if age >= 18 and age <= 20 and qualification == "BSc": 
    print("You are going to work as a junior developer")

elif age >= 25 and age <= 40 and qualification == "MSC":
    print("You are gooing to work as an intermediate developer")

elif age >= 45 and age <= 60 and qualification == "PHd":
    print("You are going to work as a senior developer")

else:
    print("Sorry you do not meet the requirements to work in our company")



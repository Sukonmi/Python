"""
A loop is a code construct that runs a set of statements while a condition is true, and stops when the condition becomes false.
There are two types of loops, which are:
- While loop
- For loop

"""

"""

n = 1

while n <=10:
    print(f"n at {n} now")
    n = n+1

n = 5

while n >=1:
    print(f"n at {n} now")
    print(f"{n} is greater than or equal to 1")
    n = n-1

n = 2

while n <=20:
    print(f"n at {n} now")
    print(f"{n} is an even number")
    n = n+2

"""

"""

For loops are used to iterate(loop over) all elements in a 
container (A container can be a list of values,
a string of characters, range of numbers)
one at a time. They are also used for counting.

"""

"""

fruits = ["apple", "banana", "mango", "pinapple"]

for f in fruits:
    print(f.capitalize())

numbers = [1,2,3,4,5,6,7,8]

for n in numbers:
    print(n*2)

numbers = [1,2,3,4,5,6,7,8,9,10]

for n in numbers:
    print(f"3x{n} = {3*n}")

for n in numbers:
    remainder = n%2
    if remainder == 1:
        print(f"{n} is an odd number")

students = {"name":"Ayomide", "age":20, "class":"ss3"}

for s in students.keys():
    print(s)

for s in students.values():
    print(s)

for s in students.items():
    print(s)

for k,v in students.items():
    print(k,v)
    
for i in range(3,51):
    print(i)

for i in range(20):
    print("Ayomide")

list = ["Kester", "AY", "Kaybee", "Samuel", "Mac"]

for i in range(len(list)):
    print(list[i])

"""

students = ["Kester", "AY", "Kaybee", "Samuel", "Mac"]
scores = [98, 92, 90, 89, 50]
statement = "I am running"
# Use a for loop to print the individual elements in each list
# Use a for loop and print the name "Samuel" 15 times
# Use a for loop and print statement 20 times

for i in range(len(students)):
    print(students[i])

for i in range(15):
    print(students[3])

for i in range(20):
    print(statement)

shopping_items = []

for i in range(6):
    shopping_items.append(input("Input your shopping item: \n"))

for i in range(len(shopping_items)):
    print(shopping_items[i])

student_info = {}
responses = []

questions = ["What's your name? \n", 
             "How old are you? \n", 
             "What class are you? \n",
             "Where are you from? \n", 
             "Enter your email address: \n"]

keys = ["name", "age", "class", "state", "email"]

size = len(questions)

for i in range(size):
    print(f"indexing questions at index {i}")
    current_question = questions[i]
    user_reponse = input(current_question)
    student_info[keys[i]] = user_reponse

print(student_info)
   
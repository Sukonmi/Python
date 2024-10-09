"""
A loop is a code construct that runs a set of statements while a condition is true, and stops when the condition becomes false.
There are two types of loops, which are:
- While loop
- For loop

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

guessed_password = "Ayomide"

while guessed_password != "hacker":
    guessed_password = input("Enter correct password: ")
    print("Wrong password! {guessed_password} Try again")

print("Password correct.")

"""

# Use a while loop that askes a user to guess an answer to a quiz queestion and the program should only run 5 times.
#  What is the capital of lagos state. 
answer = "Ikeja"

while answer != "Ikeja":
    answer = input("Enter your answer: ")
    print() 


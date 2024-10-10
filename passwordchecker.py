"""

guessed_password = "Ayomide"

while guessed_password != "hacker":
    guessed_password = input("Enter correct password: ")
    print("Wrong password! {guessed_password} Try again")

print("Password correct.")

"""

"""

# Use a while loop that askes a user to guess an answer to a quiz queestion and the program should only run 5 times.
#  What is the capital of lagos state. 
answer = "Lagos"

while answer != "Ikeja":
    answer = input("Enter your answer: ")
    print("Wrong Password! Try  again")
    n 

print("Password correct") 


# The break keyword is for breaking out of a loop.

while True:
    answer = input("Enter the correct answer: \n")
    if answer == "stop":
        print("You have stopped the program")
        break

print("What is the name of my instructor: \n")
while True:
    answer = input("Enter the correct answer: \n ")
    if answer == "Samuel Okon":
        print("You are correct!")
        break
    else:
        print("You are wrong!")

"""        

# n += 1 is the same thing as n = n + 1
trails = 1
while True:
    trails += 1
    password = input("Enter the correct answer: \n")
    if password == "Ayomide" and trails!=5:
        print("You are correct!")
        break
    elif password != "Ayomide" and trails!=5:
        print("Wrong password! try again")
    else:
        print("Max trails reached. You criminal!")
        break


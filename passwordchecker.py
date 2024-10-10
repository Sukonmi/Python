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
        

# n += 1 is the same thing as n = n + 1
trails = 0
while True:
    trails += 1
    print(trails)
    password = input("Enter the correct answer: \n")
    if password == "Ayomide" and trails<=5:
        print("You are correct!")
        break
    elif password != "Ayomide" and trails<=5:
        print("Wrong password! try again")
    else:
        print("Max trails reached. You criminal!")
        break

"""

# Write a program that allows the user to guess the magic number with only 3 attempts.
# - The magic number is 7
# if the user guesses the correct number and doesn't exceed the number of trials print "Congratulations, you guessed it!" and stop the program.
# if the user guesses wrong and stil doesn't exceed the number of trails, allow the user to try again. print "Wrong guess. Try again."
# if they failed print "You used all your attempts,the magic number was 7"
# after each failed trial give a clue based on their magic number
print("Welcome to AY's guessing challenge")


trails = 0
magicNumber = 7
while True:
    trails += 1
    print(trails)
    userGuess = int(input("What is the magic number: \n"))
    if userGuess  == magicNumber and trails<=3:
        print("Congratulations, you guessed it!")
        break
    elif userGuess != magicNumber and trails < 3:
        if userGuess > magicNumber:
            print("wrong password! Your guess wass too high. Try again")
        else:
            print("Wrong password! Your guess was too low. Try again.")

    else:
        print(f"Sorry, You've used all your attempts. \n The magic number is {magicNumber}")
        break
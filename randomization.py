import random

Random_integer = random.randint(1,6), random.randint(1,6)

print(Random_integer)

print(input("Heads or Tails? \n").capitalize)
Random_integer2 = random.randint(0,1)
if Random_integer2 == 0:
    print("Heads")
else:
    print("Tails")

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score

print("The highest score in the class is:", highest_score)

# Calculate sum of even numbers from 1 to 100
even_sum = sum(i for i in range(2, 101, 2))

# Print the result
print("The sum of even numbers from 1 to 100 is:", even_sum)


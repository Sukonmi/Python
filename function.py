# Functions helps you avoid repeating yourself.

def correct_password():
    print("Your password is correct")

def wrong_password():
    print("Your password is wrong")

def check_password():
    user_input = input("Enter your password: \n")

    if user_input == "GoMyCode":
        correct_password()
    else:
        wrong_password()

check_password()

def sum_two_numbers(a,b):
    print(a+b)

sum_two_numbers(1,2)


def area(b,h):
    triangle_area = (b*h)/2
    return triangle_area

print(f"Traingle area is {area(3,4)}")

def minimum_number(a,b):
    if a>b:
        return b
    else:
        return a

print(minimum_number(2,5))


def print_scores(scores,bonus):
    for score in scores:
        print(f"{score} would be updated to {score+bonus}")

print_scores([67,68,72,71,69],10)

def multiplication_table(numbers,multiplier):
    for n in numbers:
        print(f"{multiplier}x{n} = {n*multiplier}")

multiplication_table([1,2,3,4,5,6,7,8,9,10,11,12],1000)
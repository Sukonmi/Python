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
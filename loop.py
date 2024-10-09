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
operations = ["+", "-", "*"]

while True:
    operation = input("Enter operation: \n")

    if operation not in operations:
        print("Invalid")
        continue

    print("Not skipping")
    num2 = input("Enter second number")
# You would have 4 functions
def add(a,b):
    pass

def subtract(a,b):
    pass

operations = {"+":add(), "-":subtract()}

def calculate():
    print()
    for symbol in operations.keys():
        print(symbol)
    user = input("What are your")
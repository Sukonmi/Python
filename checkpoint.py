shopping_list = []
unique_items = set()
items_info = {}

while True:
    print("""Shopping List Menu:\n
          1. Add items.
          2. Remove items.
          3. View items.
          4. Exit""")
    
    user_choice = int(input("Select from the available options(1-4): \n"))

    if user_choice == 1:
        print("Add Item selected")
        for i in range(5):
            item = input("Enter item: ")
            if item in unique_items:
                print(f"{item} is already in shopping list")
            else:
                item_quantity = int(input(f"How many quantity of {item}?"))
                shopping_list.append(item)
                unique_items.add(item)
                items_info[item] = item_quantity
                print(f"{item} has been added to your shopping cart")
    elif user_choice == 3:
        print("Displaying items in your cart")
        if len(shopping_list) > 0:
            for item in shopping_list:
                print(f"{item} with {items_info[item]} quantity")
        else:
            print("Your cart is empty")
    elif user_choice == 4:
        print("Thank you for patronizing us")
        break
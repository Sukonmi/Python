shopping_list = []
unique_items = set()
items_info = {}
our_store_items = {"Mango":5, "Apple":10, "Pear":4}

while True:
    print("""Shopping List Menu
          1. Add Item
          2. Remove Item
          3. View Items
          4. Exit
          """)
    
    user_choice = int(input("Select from the available options(1/2/3/4): \n"))

    if user_choice == 1:
        print("Add Item Selected.")
        print("These are the items we have in our store currently")
        for item in our_store_items.keys():
            print(item)
        for i in range(5):
            item = input("Enter item: ").capitalize()
            if item in our_store_items:
                if item in unique_items:
                    print(f"{item} is already in shopping list")
                else:
                    item_quantity = int(input(f"How many quantity of {item}?: "))
                    shopping_list.append(item)
                unique_items.add(item)
                items_info[item] = item_quantity
                items_info[f"{item}_price"] = our_store_items[item]
                print(f"{item} has been added to your shopping cart")
            else:
                print("Sorry! We do not have this currently.")

    elif user_choice == 3:
        print("Displaying items in your cart")
        if len(shopping_list) > 0:
            for item in shopping_list:
                print(f"{item} with {items_info[item]} quanity(s) with price of {items_info[f"{item}_price"]}")
        else:
            print("Your cart is empty")
    
    elif user_choice == 4:
        print("Thank you for patronizing us")
        break


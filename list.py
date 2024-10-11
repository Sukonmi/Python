# DATA STRUCTURES.
items = ["Ayomide", "Kester", "Kaybee", "Mac", "Samuel", 1, 2, 5.5, [1,3,5, [4,8]]]

print(items[8][3][1])

myList = ["Chicken Republic", "Kilimanjaro", "KFC", "Tastia", 4, 65, 80, ["Victor", 30, [20, 30, [100, 200, 300]]]]

print(myList[3], myList[7][2][2][2])



# List Slicing
l = [100,11,21,41,51,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# [start_index:stop_index] NB: The stop_index is not inclusive, it is exclusive.
print(l[14:8:-2])

l.append(16)

l.pop()
l.remove(2)
# pop removes from behind, while reemove allows you to speciify
# count counts the number of reocurence of a value
# len is an inbuilt ppython to check the length of anything.

print(l.count(1))
print(len(l))

l.sort()

print(l)

myList = [1, 4, 3, 20, 6 ,7, 9, 10, 14, 2, 1, 2]

# Count the occourence of 2
print(myList.count(2))

# What is the size of the list
size = len(myList)
print(size)

# What's the index of the value of 14
print(myList.index(14))

# pop the last item
myList.pop()

# remove the value 9
myList.remove(9)

# sort the list
myList.sort()

print(myList)

# LIST PRACTICE EXERCISE
# 1. Create a list of 5 favorite fruits and print the list.

favorite_fruits = ["Apple", "Pineapple", "Banana", "Orange", "Watermelon"]

print(favorite_fruits)
# 2. Accessing Elements:

myList = [2, 4, 6, 8, 10]

print(myList[0], myList[4])

# 3. Modifying a List:

colors = ["red", "green", "blue"]  

# 3a. Add a new color to the list.

colors.append("black")

# 3b. Change the second color to "yellow".

colors[1] = "Yellow"

# 3c. insert a new color  in the index 1

colors.insert(1,"Grey")

# 3d. Print the updated list.

print(colors)

# 4. List Length:
# Create a list of 7 different animals. Print how many animals are in the list.
animal_names = ["Dog", "Lion", "Tiger", "Snake", "Dragon", "Eagle", "Cheetah"]

numberofanimals = len(animal_names)
print(numberofanimals)

# 5. Slicing a List:

numbers = [10, 20, 30, 40, 50]

# 5b. slice the list to print only the first three numbers.
print(numbers[0:3])

# We use the del keyword to removes a specified index.

my_list =  ['Scala', 'SQL', 'R', 'SAS', 'C++', 'php', 'html', 'Matlab']

del my_list[0]      #remove the item with 0 index (python)    

print(my_list)      ['Scala', 'SQL', 'R', 'SAS', 'C++', 'php', 'html', 'Matlab']
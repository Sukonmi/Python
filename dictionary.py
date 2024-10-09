student_one = {"Student_name": "David Amadi", "Age":20, "Class": "SS1", "Club": ["Maths", "Science"]}
student_two = {"Student_name": "Daniel Ayomide", "Age":30, "Class": "Graduate", "Club": ["PSG", "Arsenal"]}

print(student_two["Student_name"], "Age", "Class", "Club")

pizza_sizes = {"Small":15, "Medium":20, "Large":25}

# to check all the keys in a dictionary
print(pizza_sizes.keys())

# return all the values stored in the dictionary
print(pizza_sizes.values())

# Return both the keys and values
print(pizza_sizes.items())


# DICTIONARY PRACTICE EXERCISE
# Create a Dictionary:

personalInfo = {"name": "Ayomide", "age":20, "city": "Abuja"}

print(personalInfo)

#  Accessing Dictionary Values:

student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])

#  Adding and Modifying Values:

person = {"name": "Alice", "age": 30}

person["city"]="New York"

person["age"]=31

print(person)

#  Dictionary Length:

# Create a dictionary representing three different cars with their prices. Print how many key-value pairs are in the dictionary.
carPrices = {"BMW": 30000000, "Lamborghini": 45000000, "Tesla": 65000000}

print(carPrices.items())

#  Using a Dictionary with Lists:

# Create a dictionary where the key is the name of a country and the value is a list of 3 cities in that country. Print the dictionary.
location = {"Nigeria": ["Lagos", "Abuja", "Ogun"]}

print(location)

my_dictionary = {"knowledge": "Data Science", "tool": "python", "year": 2020}
second_dict = {"Database": "POSTGRESQL", "tool": "Java"}

my_dictionary.pop("tool")
my_dictionary.update(second_dict)

print(my_dictionary)

# update is used to add, update or merge an existing dictionary from another dictionary




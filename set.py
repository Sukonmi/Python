my_set = {"python", "java", "R"}

print(my_set.difference({"JS", "R"}))
# difference check for things that aren't common.

my_set.add("scala")
# add includes new values

print(my_set)

unique_numbers = {1, 2, 3, 4, 5}

unique_numbers.add(6)

lengthofnumbers = len(unique_numbers)

print(lengthofnumbers)

unique_numbers.add(2)

print(unique_numbers)
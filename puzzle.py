import math

max_age = 90

user_age = int(input("How old are you? "))
years_left_for_user = max_age - user_age

days_left = years_left_for_user * 365
weeks_left = years_left_for_user * 52
months_left = years_left_for_user * 12

print(f"You have {days_left} days left, {weeks_left} weeks left, and {months_left} months left.")
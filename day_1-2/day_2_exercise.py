# So today's exercise: #
# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: 
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). yearLet the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
import datetime

username = input ("What is your username? ")
age = int(input (f"{username}, how old are you? "))
mark_age = 100
age_difference = mark_age - age
print(f" Well today you are {age} years old. You will reach {mark_age} years old in {age_difference} years")

currentYear = datetime.datetime.now().year # why "datetime" is twice?
year = currentYear + age_difference
print(f"You will be {mark_age} in year: {year}")

# # 1. What's the frequency?

# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter counts.

# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} 

# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included

#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile
#


entered_text=input("Enter your text: ")

#version 1

# def get_char_count(entered_text):
#     char_count={}
#     for c in entered_text:
#         if c in char_count:
#             char_count[c] += 1
#         else:
#             char_count[c] = 1
#     return char_count

# print(get_char_count(entered_text))

#version 2
from collections import Counter # generally we import all modules at the top of the file
my_counter = Counter(entered_text)
print(my_counter)
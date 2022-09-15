# 2. Almost Hangman

# Write a program to recognize a text symbol

# The user (first player) enters the text.

# Only asterisks instead of letters are output.

# Assume that there are no numbers, but there may be spaces.

# The user (i.e. the other player) enters the symbol.

# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.


text = input("Enter your set word: ")
set_word = ""
guess_word = ""

for c in text:
    if c == ' ':
        set_word += " "
    else:   
        set_word += "_"
print(set_word)

guess = input("Enter your guess: ")

for c in text:
    if c == guess:
        guess_word += c
    elif c == ' ':
        guess_word += " "
    else:
        guess_word += "_"
print(guess_word) 
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
#If game is on
#know how many guesses
#set word/guess word
#if wrong guess_chances -=1
#if correct: another guess


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
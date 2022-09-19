# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
#If game is on
#know how many guesses
#set word/guess word
#if wrong guess_chances -=1
#if correct: another guess


text = input("Enter your set word: ")
chances = input("Enter how many guesses available:")
set_word = ""
guess_word = ""

for c in text:
    if c == ' ':
        set_word += " "
    else:   
        set_word += "_"
print(set_word)

game_status = False

while not game_status:
    guess = int(input("Enter your guess: "))
    while guess > 1:
        for c in text:
            guess -= 1
            if c == guess:
                guess_word += c  
            elif c == ' ':
                guess_word += " "
            else:
                guess_word += "_" 
            print(guess_word) 

    if guess == 0:
        game_status = True
        print(guess_word)
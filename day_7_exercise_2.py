# 2. Palindrome
# Write the function is_palindrome (text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False

entered_text=input("Enter a word or sentence to check if it is read equally from both sides: ")

def is_palindrome (entered_text):
    entered_text = entered_text.replace(" ", "").lower()
    reversed_text = entered_text[::-1]
    return entered_text == reversed_text
        
print(is_palindrome(entered_text))
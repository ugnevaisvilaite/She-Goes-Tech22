# 3. Text conversion

# Write a program for text conversion

# Save user input

# Print the entered text without changes

# Exception: if the words in the input are not .... bad, 
# then the output is not ...  bad section must be changed to is good

text=input("Enter your text: ")

first_word = text.rfind("not")    #any difference between find and rfind
second_word = text.rfind("bad")
new_word = "good"

if first_word > 0 and second_word > 0:
    
    changed=text.replace(first_word, new_word)
    
print(changed)
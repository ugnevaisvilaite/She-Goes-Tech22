# 3. Reversed words

# The user enters a sentence.

# We output all the words of the sentence in a reverse form. 
# - not the whole text reversed!!

# Example

# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately

# PS Split and join operations could be useful here.

text= input("Enter your text: ")
separated=text.split(" ")
whole_text=[]
for n in separated:
    words = n[::-1]
    whole_text.append(words)
    full_text= " ".join(whole_text)
print(full_text)


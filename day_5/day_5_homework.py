
# write a program that asks for two text inputs s1 and s2 
# you can use better names than s1 and s2

# then checks if all the characters in first string are in second string
# if they are, print All character counts in the second string
# if not, print Not all characters are in the second string
# example
# s1 = "abc"
# s2 = "abracadabra"
# output: a 5, b 2, c 1, d 1, r 2  # so do not print the empty ones

# example two
# s1 = "abc"
# s2 = "def"
# output: Not all characters are in the second string
# so preferably use alphabetic ordering  :)


str1=input("Enter first word: ").lower()
str2=input("Enter second word: ").lower()

same = []

a_len = len(str1)
b_len = len(str2)

if a_len <= b_len: #check if second word is same/longer than first word
    for a in str1:
        for b in str2: #compare each letter
            if a == b:
                same.append(b)     #if same add letter to list
    count=dict((i, same.count(i)) for i in same)   #count how many of each letters (that match)
else:
    print("Not all characters are in the second string")
    
    
if len(count) == a_len:  
    print("All character counts in the second string")
    print(count)
else:
    print("Not all characters are in the second string")


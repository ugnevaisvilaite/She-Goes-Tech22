
str1=input("enter word: ").lower()
str2=input("enter word: ").lower()

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


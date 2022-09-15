# 1. Confusion

# The user enters a name.

# You print user name in reverse (should begin with capital letter)
#  then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"

# Example:

# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?

name=input("Enter your name: ")
extra = ",a thorough mess is it not "

reversed=name[::-1] 
print(reversed)
print(f"{reversed.capitalize()} {extra} {name[0]} ?")
# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings 
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af" 
# because "a" is in both "abc" and "fab" but not in "boo"
# same goes for "f" it is present in both "good strings" but not in "badstring"
# notice "b" is not in the result because it is in the badstring.

# slightly harder way would be to use loops and if statements to check each character
# the easy way is to use sets and set operations 😊

# either approach is acceptable


def check_unique_characters(arg_1, arg_2, arg_3):
    a=(set(arg_1) & set(arg_2)) - set(arg_3)
    return "".join(sorted(a))

print(check_unique_characters("abcf", "fab", "boo"))
print(check_unique_characters("abcf123", "fab123", "b2oo"))

print("----------------------------------------------------------------")

#VERSION 2 - LIMITLESS ARGUMENTS

def check_unique_characters_limitless(*args):
    a=(set(args[0]) & set(args[1])) - set(args[-1])
    return "".join(sorted(a))

print(check_unique_characters_limitless("abcf", "fab", "boo"))
print(check_unique_characters_limitless("laba123", "a3","kala1", "abc"))
print(check_unique_characters_limitless("abcf123", "fab123","fab123", "b2o3o"))
print(check_unique_characters_limitless("abc123", "123","fab123", "b2o3o"))


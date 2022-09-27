# 2. Common Elements

# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.

# get_common_elements(seq1, seq2, seq3)

# Example:

# get_common_elements("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element 

# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)

# 2. b For those with some experience 

# BONUS:  make a function that can handle an arbitrary number of input sequences
# so function which takes any number of sequences and returns a tuple with common elements
# get_common_elements(seq1, seq2, seq3, seq4, seq5, seq6, seq7) etc :), so just like print takes any number of values

#2.a

def get_common_elements(seq1, seq2, seq3):
    return tuple(set(seq1) & set(seq2) & set(seq3))

print(get_common_elements("abc", ['a', 'b'], ('b', 'c')))


#2.b
def get_common_elements_second(*seq):
    if len(seq) == 0:
        return print("end")   #dont know how to make it print "end" or "not working"
    return tuple((set(seq[0]).intersection(*seq[1:])))

print(get_common_elements_second("abc", ['a', 'b', 'c'], ('b', 'c')))
print(get_common_elements_second("572hsbd9i2", ['7', 'z', 'c', 'i'], ('b', 'c','i', '7')))
print(get_common_elements_second("572hsbd9i2", [], ('b', 'c','i', '7')))

# 1f -> write the function get_word_usage(srcpath, destpath)

# The function opens the file and finds the most frequently used words

# recommendation to use Counter module!

# assume that the words are separated by either whitespace or newline (the good old split will come in handy)

# the saved list of words and frequency should be saved in destpath in the following form:

# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary

from collections import Counter


def get_word_usage(read_file,new_file, encoding="utf-8"):
    with open(read_file, encoding=encoding) as fin, open(new_file, mode="w", encoding=encoding) as fout:
        text =  fin.read()
        full_list = text.split()
        
        most_frequent_word_list = Counter(full_list)
        max_frequency=most_frequent_word_list.most_common(10)
        
        for x in max_frequency:
            fout.write(str(x))


read_file='day_12/sherlock_holmes_adventures.txt'
new_file='day_12/count_list.txt'
get_word_usage(read_file,new_file)
            
            
            
    
                
            
        
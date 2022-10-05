# 1e -> write the function clean_punkts(srcpath, destpath)

# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")
import string



def clean_punkts(srcpath, destpath, encoding='utf-8'):
    with open(srcpath, encoding=encoding) as fin, open(destpath, "w", encoding=encoding) as fout:
        for line in fin:
            for c in line:
                if c in string.punctuation:
                    line = line.replace(c, '')
            fout.write(line)
        
srcpath='day_12/pure_sherlock.txt'
destpath='day_12/clean_sherlock.txt'
clean_punkts(srcpath, destpath)


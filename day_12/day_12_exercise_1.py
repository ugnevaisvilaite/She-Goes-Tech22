# Exercise
# read text from  sherlock_holmes_adventures.txt

# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file

# check file_line_len("sherlock_holmes_adventures.txt") -> 12305
import os
import string
from collections import Counter



print(os.getcwd())

def file_line_len(fpath):
    line_length = 0
    with open(fpath) as f:
        for _ in f:
            line_length += 1
    return line_length

print(file_line_len("day_12/sherlock_holmes_adventures.txt"))

# 1b -> write the function get_text_lines(fpath), which returns a list with only those lines that contain text.

# So we want to avoid/filter out those lines that contain whitespace
#----------------------------------------------------------------
def get_text_lines(fpath, new_file, sep='\n', encoding="utf-8"):
    with open(fpath, encoding=encoding) as fin, open(new_file, mode="w", encoding=encoding) as fout:
        lines = [line.strip() for line in fin]
        for line in lines:
            fout.write(line + sep)

new_file="day_12/new_sherlock.txt"                  
get_text_lines("day_12/sherlock_holmes_adventures.txt",new_file)

#another approach
def get_text_line(fpath):
    with open(fpath, encoding="utf-8") as fin:
        lines = [lines.strip() for lines in fin]
    return lines

text_lines = get_text_line("day_12/sherlock_holmes_adventures.txt")
print(text_lines[:10])
print(len(text_lines))
#----------------------------------------------------------------

# 1c -> write the function save_lines(destpath, lines)

# This function will store all lines into destpath file 
#----------------------------------------------------------------
def save_lines(destpath, lines, sep="\n",encoding="utf-8"):
    with open(destpath, mode="w", encoding=encoding) as fout:
        for line in lines:
            fout.write(line + sep)
        
save_lines("day_12/new.txt", text_lines)
#----------------------------------------------------------------
# 1d -> call save_lines with destpath being "pure_sherlock.txt" and lines being the text lines we cleaned from 1b
#----------------------------------------------------------------
save_lines("day_12/pure_sherlock.txt", text_lines)

#----------------------------------------------------------------

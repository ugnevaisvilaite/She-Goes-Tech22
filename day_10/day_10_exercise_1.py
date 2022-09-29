# 1. Song class
# define a class Song

# The class constructor needs to have three additional 3 parameters (self and 3 more!)

# title defaults to empty string

# author defaults to empty string

# lyrics by default empty tuple

# inside constructor method:

# set/store these three parameters inside objects variables of the same name (remember to use self!)

#  print on the screen "New Song made" - (try also printing here author and title!)

# Minimum:

# Write a method sing that prints the song line by line on the screen, first printing the author and title, if any.

# Write a method yell that prints the song in capital letters line by line on the screen, first printing the author and title, if any.

# Bonus: make the above sing and chain methods chainable, so we can call them several times (chained)

# Bonus: create an additional parameter max_lines to yell and sing methods that prints only a certain number of lines for both sing and yell. Better do with some default value e.g. -1, at which all rows are then printed.

# Create multiple songs with lyrics

# Example:


# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])

# ziemelmeita.sing(1).yell()

# Outputs:

# Ziemeļmeita - Jumprava

# Gāju meklēt ziemeļmeitu

# Ziemeļmeita - Jumprava

# GĀJU MEKLĒT ZIEMEĻMEITU

# GARU, TĀLU CEĻU VEICU

class Song:
    
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f" New Song made: {self.title} - {self.author} ")
        
    def sing(self):
        for i in self.lyrics:
            print(i)
        return self

        
    def yell(self):
        for i in self.lyrics:
            print(i.upper())
        return self
 
        
        
ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])

print(ziemelmeita.sing().yell())


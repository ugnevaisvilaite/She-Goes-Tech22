# 2. Deck - probably for homework, see how far you get

# write a class Deck with the following attributes(variables) 

# available - contains list of card tuples that can be used (list)

# spent - contains list of card tuples that have been used (list)

# there should be following methods:

# constructor (__init__) method

# initializes available with full 52 card list of tuples

# initializes spent with empty list

# shuffle(self):

# # shuffles available cards - works just like 1st function but works on available

# get_cards(self, count=1):
# # gets some number(default 1) of cards from available 
# adds these cards to spent
# returns these cards

# # you can add other methods and/or attributes if you wish to Deck class

# example usage:
# my_deck = Deck()
# print(my_deck.available) # 52
# print(my_deck.spent) # 0
# my_deck.shuffle() # shuffles available
# print(my_deck.available) # 52
# print(my_deck.spent) # 0
# my_cards = my_deck.get_cards(5) # gets 5 cards from available
# print(my_cards) # 5 cards like (3, 'hearts ♥'), (6, 'diamonds ♦'), (3, 'spades ♠'), (5, 'clubs ♣'), (7, 'hearts ♥'
# single_card = my_deck.get_cards() # gets 1 card from available
# print(single_card) # 1 card like (4, 'diamonds ♦')
# print(my_deck.available) # 46 because we got 6 cards
# print(my_deck.spent) # 6 because we got 6 cards

import random
import itertools


def get_shuffled_cards():
    symbol = [2,3,4,5,6,7,8,9,10,"J","Q","K", "A"]
    colors = ["clubs (♣)", "diamonds (♦)", "hearts (♥)", "spades (♠)"]
    cards = [(s, c) for s in symbol for c in colors]
    
    random.shuffle(cards)
    return cards

class Deck:
    symbol = [2,3,4,5,6,7,8,9,10,"J","Q","K", "A"]
    colors = ["clubs (♣)", "diamonds (♦)", "hearts (♥)", "spades (♠)"]
    
    def __init__(self):
        self.available = list(itertools.product(self.symbol, self.colors)) 
        self.spent = []
        self.shuffle()
        
    def shuffle(self):
        self.available = random.sample(self.available, len(self.available)) #pool: available, pick until reached len(available)
        card_count=len(self.available)  
        print(f'Available cards: {self.available} cards.\nAvailable card count: {card_count}.')
        return self
    
    def get_cards(self, count=1):  #default as for one card
        cards=self.available[:count] #get required number of cards
        self.available=self.available[count:] #check how much is left of available after minus shuffled cards
        self.spent.extend(cards)
        a=len(cards)
        b=len(self.available)
        print(f'Available cards: {b} cards.!\nAvailable card count: {a}.')
        return cards
    

        
if __name__ == "__main__":
    print(get_shuffled_cards())
    print("----------------------------------------------------------------")
    my_deck = Deck()
    print("----------------------------------------------------------------1")
    print(my_deck.available) # 52
    print(my_deck.spent) # 0
    print("----------------------------------------------------------------6")
    my_deck.shuffle() 
    print(my_deck.spent)  #0
    print("----------------------------------------------------------------2")
    my_cards = my_deck.get_cards(7) # gets 7 cards from available
    print(my_cards) 
    print(my_deck.spent) #7 cards
    print("----------------------------------------------------------------3")
    single_card = my_deck.get_cards() # gets 1 card from available, left 44
    print("----------------------------------------------------------------4")
    print(single_card) # 1 card 
    print("----------------------------------------------------------------5")
    print(my_deck.available)
    print("----------------------------------------------------------------5")
    my_cards = my_deck.get_cards() # gets 1 cards from available, left 43
    print("----------------------------------------------------------------7")
    print(my_cards)
    print("----------------------------------------------------------------8")
    my_cards = my_deck.get_cards(15) #get 15, left 28


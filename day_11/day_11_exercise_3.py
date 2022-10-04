


class Deck:
    symbols=[2,3,4,5,6,7,8,9,10,"J","Q", "K", "A"]
    colors= ["clubs (♣)", "diamonds (♦)", "hearts (♥)", "spades (♠)"]
    
    
    def __init__(self):
        self.available = list()
        self.spent= []
        
    def __str__(self):
        return f'Available cards {self.available} cards, Available cards {self.spent} cards'
        
    # def shuffle(self): #shuffle the list of available cards
        
    #     return self

    # def get_the_cards(self):  #get the list of available cards(specific number of cards)
        
    #     return self
    
    
if __name__ == "__main__":
    # print(get_shuffled_cards())
    my_deck = Deck()
    print("----------------------------------------------------------------")
    print(my_deck.available)
    print("----------------------------------------------------------------")
    print(my_deck.spent)
    # my_deck.shuffle()
    
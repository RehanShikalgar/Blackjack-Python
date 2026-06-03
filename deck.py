from card import Card

class Deck:
    def __init__(self):   #   creates 52 cards and shuffle them. constructor calls those functions to get the job done.
        self.cards = self.cards_in_deck()
        self.shuffle()

    def __str__(self):
        return f"Cards remaining: {len(self.cards)} | Cards used: {52 - len(self.cards)}"

    def cards_in_deck(self):
        cards =[]   #   empty list. we are going to store 52 cards in it.

        suits=["Diamonds","Spades","Hearts","Clubs"]
        values=["A",2,3,4,5,6,7,8,9,10,"Q","K","J"]

        for suit in suits:
            for val in values:
                cards.append(Card(suit, val))  #  class Card which is above.. 

        return cards   #   returns all (52) cards.
    

    def shuffle(self):
        import random
        random.shuffle(self.cards)   #   this will shuffle those 52 cards.

    def deal(self):
        one_card = self.cards.pop()   #   pop() will take the last card from the shuffled list
        return one_card    #   after shuffling, we return one card, because that's all a player or a dealer is going to need at once.
        
from player import Player
from card import Card

class Dealer(Player) :
    def __init__(self):
        super().__init__(0)

    def show_visible_hand(self):
        if self.hand[0]:
            print("Hidden")
        print(self.hand[1])

    def should_hit(self):
        if self.calculate_score() < 17:
            return True
        else:
            return False
    

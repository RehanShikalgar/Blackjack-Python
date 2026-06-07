from dealer import Dealer
from player import Player
from deck import Deck


class Game:
    def __init__(self, balance):
        self.deck = Deck()
        self.player = Player(balance)
        self.dealer = Dealer()


    def initial_deal(self):
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

        print("\n Player's Hand: ")
        self.player.show_hand()

        print("\n Dealer's Hand: ")
        self.dealer.show_visible_hand()

        print("Player's Score: ", self.player.calculate_score())

from deck import Deck
from player import Player

d = Deck()

player = Player(3000)

player.add_card(d.deal())
player.add_card(d.deal())

player.show_hand()

print(player.calculate_score())
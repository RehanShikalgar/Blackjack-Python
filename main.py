from deck import Deck
from player import Player
from dealer import Dealer

d = Deck()
dealer = Dealer()

dealer.add_card(d.deal())
dealer.add_card(d.deal())

dealer.show_visible_hand()

dealer.show_visible_hand()

print("---- Reveal ----")

dealer.show_hand()
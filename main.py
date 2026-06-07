from deck import Deck
from player import Player
from dealer import Dealer
from game import Game


balance = int(input("Enter your starting balance: "))
game = Game(balance)
game.initial_deal()


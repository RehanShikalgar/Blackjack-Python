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


    def player_plays(self):
        player_turn = True
        while player_turn == True:
            user_input = input('TYPE "hit" TO HIT TO KEEP TAKING CARDS OR TYPE "stand" TO STOP TAKING CARDS: ').lower()
            if user_input == 'hit':
                player_turn = self.player_hit()
            elif user_input == 'stand':
                player_turn = self.player_stand()
            else:
                print("Wrong Input.")

    def player_hit(self):
        self.player.add_card(self.deck.deal())
        print("___________________________________________")
        print("Your Cards: ")
        self.player.show_hand()
        print("_____________________________________")
        score = self.player.calculate_score()
        if(score > 21): # Bust Logic..
            print("You Busted. The Score surpassed 21.")
            print("Your Score: ", score)
            return False

        print("Your Score: ", score)
        return True

    def player_stand(self):
        print("You Chose to Stand. Your Score is: ", self.player.calculate_score())
        return False

    def dealer_plays(self):
        dealer_turn = True
        
        while dealer_turn:
            score = self.dealer.calculate_score()
            if(score < 17):
                dealer_turn = self.dealer_hit()
            else:
                dealer_turn = self.dealer_stand()
            
            

    def dealer_hit(self):
        self.dealer.add_card(self.deck.deal())
        return True

    def dealer_stand(self):
        print("Dealer turn ends as Dealer score is equal to OR greater than 17.")
        self.dealer.show_hand()
        return False

    def compare_score(self):
        dealer_score = self.dealer.calculate_score()
        player_score = self.player.calculate_score()
        if dealer_score > 21:
            return "player"

        elif player_score > 21:   # it's reduntant. still keeping it coz I might call compare_score() before interpreter gives me player bust result.
            return "dealer"

        elif dealer_score > player_score:
            return "dealer"

        elif player_score > dealer_score:
            return "player"

        else:
            return "tie"


    def declare_winner(self, winner):
        dealer_score = self.dealer.calculate_score()
        player_score = self.player.calculate_score()
        if winner == "player":
            print("You Win..!\n")
            print("Dealer Score: ")
            print(dealer_score,"\n")
            print("Your Score:")
            print(player_score,"\n")
        
        elif winner == "dealer":
            print("Dealer Wins.\n")
            print("Dealer Score: ")
            print(dealer_score, "\n")
            print("Your Score:")
            print(player_score,"\n")

        elif winner == "tie":
            print("It's a tie.")

    def game_play(self):
        self.player.show_balance()
        self.initial_deal()

        self.player_plays()

        if self.player.calculate_score() > 21:
            self.declare_winner("dealer")
            return

        self.dealer_plays()

        winner = self.compare_score()

        self.declare_winner(winner)

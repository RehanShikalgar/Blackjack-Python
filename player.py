MIN_BET = 100
MAX_BET = 10000

class Player:
    def __init__(self, balance):
        self.hand = []
        self.balance = balance
        self.current_bet = 0
        print("Available Balance: ", self.balance)
        

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        for hands in self.hand:
            print(hands)

    def calculate_score(self):
        score = 0
        for card in self.hand:
            # print(card.value)
            
            if card.value in ["J", "Q", "K"]:
                score = score + 10
            elif card.value == "A":
                if score+ 11 <= 21: 
                    score = score + 11
                else:
                    score = score + 1
            else:
                 score += card.value
                
        return score



    def place_bet(self, amount):
       
        
        if amount <MIN_BET:
            raise ValueError ("Bet amount should be greater than 100.")

        elif amount >MAX_BET:
            raise ValueError ("Bet amount cannot exceed $10,000")

        elif amount > self.balance:
            print("Current Balance: ", self.balance)
            raise ValueError ("Amount shouldn't exceed your Current Balance.")

        self.current_bet=amount
            
        
        self.balance = self.balance - self.current_bet 
        print("Your bet amount: ", self.current_bet)
        print("Current Balance: ", self.balance)
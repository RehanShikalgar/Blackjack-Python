MIN_BET = 100
MAX_BET = 10000

class Player:
    def __init__(self, balance):
        self.hand = []
        self.balance = balance
        self.current_bet = 0
      
    def show_balance(self):
        print("Available Balance:", self.balance)
        

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



    def place_bet(self):

        while True:

            amount = int(input("Enter Bet Amount: "))

            if amount < MIN_BET:
                print(f"Bet amount must be at least {MIN_BET}.")
                

            elif amount > MAX_BET:
                print(f"Bet amount cannot exceed {MAX_BET}.")
               

            elif amount > self.balance:
                print(f"Your current balance is {self.balance}.")
               
            else:
                self.current_bet = amount
                print("Your bet amount:", self.current_bet)
                print("Bet Accepted..!")
                return

    
    def clear_hand(self):
        self.hand.clear()
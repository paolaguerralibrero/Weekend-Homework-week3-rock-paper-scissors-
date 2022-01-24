class Game():
    def __init__(self, choice_1, choice_2):
        self.choice_1 = choice_1
        self.choice_2 = choice_2


    def check_win(self):
        if self.choice_1 == "paper" and self.choice_2 == "rock":
            return "Player 1 wins"
        if self.choice_1 == "rock" and self.choice_2 == "paper":
            return "Player 2 wins"

        if self.choice_1 == "scissors" and self.choice_2 == "paper":
            return "Player 1 wins"
        if self.choice_1 == "paper" and self.choice_2 == "scissors":
            return "Player 2 wins"

        if self.choice_1 == "rock" and self.choice_2 == "scissors":
            return "Player 1 wins"
        if self.choice_1 == "scissors" and self.choice_2 == "rock":
            return "Player 2 wins"

        if self.choice_1 == "paper" and self.choice_2 == "paper":
            return "None"
        if self.choice_1 == "scissors" and self.choice_2 == "scissors":
            return "None"
        if self.choice_1 == "rock" and self.choice_2 == "rock":
            return "None"    
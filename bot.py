import random

class Bot:

    def __init__(self, player):
        self.player = player

    def chooseMove(self, board):
        # Removes taken positions
        positions = [pos for pos in board if type(pos) != str]
        return random.choice(positions)

import random

winningPos = [
    [0, 1, 2], [3, 4, 5],
    [6, 7, 8], [0, 3, 6],
    [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

class Bot:

    def __init__(self, player):
        self.player = player

    def chooseMove(self, board):
        # Removes taken positions
        positions = [pos for pos in board if type(pos) != str]

        for pos in winningPos:
            winningMovesLeft = [p for p in pos if type(p) != str]
            if len(winningMovesLeft) == 1:
                return winningMovesLeft[0]

        return random.choice(positions)

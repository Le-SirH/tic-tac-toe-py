import random
import time

winningPos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
]

class Bot:

    def __init__(self, player):
        self.player = player
        self.board = []
        self.winPosGoal = random.choice(winningPos)

    def chooseMove(self, board):
        # determines whether there is a spot to be blocked
        # pMoves finds available moves for each winning position
        # winningMoves determines the positions of the available winning moves
        for pos in winningPos:
            pMoves = [pMove for pMove in pos if type(self.board[pMove]) == str]
            winningMoves = [p for p in pos if type(self.board[p]) != str]
            if (len(pMoves) == 2) & (len(winningMoves) == 1):
                if self.board[pMoves[0]] == self.board[pMoves[1]]:
                    return winningMoves[0]

        # If there are no blocks to be made, make a move based on a winning position.
        # winPosGoal is a randomly chosen winning position that the bot goes for.
        # availablePos filters the board positions to tell which are available
        winMove = random.choice(self.winPosGoal)
        if not self.isTaken(winMove): return winMove
        else:
            availablePos = [pos for pos in self.board if type(pos) != str]
            self.winPosGoal = random.choice(winningPos)
            return random.choice(availablePos)

    def isTaken(self, movePos):
        openPos = [pos for pos in self.board if type(pos) != str]
        if movePos in openPos: return False
        return True

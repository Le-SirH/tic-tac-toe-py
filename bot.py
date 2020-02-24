import random

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
        # filters the board positions to tell which are available
        positions = [pos for pos in self.board if type(pos) != str]
        for pos in winningPos:
            # filters the moves available for each winning position
            pMoves = [pMove for pMove in pos if type(self.board[pMove]) == str]
            # determines the positions of the available winning moves
            winningMovesLeft = [p for p in pos if type(self.board[p]) != str]
            # determines whether there is a spot to be blocked
            if (len(pMoves) == 2) & (len(winningMovesLeft) == 1):
                if self.board[pMoves[0]] == self.board[pMoves[1]]:
                    return winningMovesLeft[0]
        
        # If there are no blocks to be made, make a move based on a winning position.
        # winPosGoal is a randomly chosen winning position that the bot goes for.
        winMove = random.choice(self.winPosGoal)
        if self.isTaken(winMove) == False:
            return winMove
        else: 
            # resets winPosGoal & chooses a random position on the board.
            self.winPosGoal = random.choice(winningPos)
            return random.choice(positions)

    def isTaken(self, movePos):
        openPos = [pos for pos in self.board if type(pos) != str]
        if movePos in openPos:
            return False
        return True

import bot
import random

winningPos = bot.winningPos

class Game:

    def __init__(self, player, bot, firstMove):
        self.board = [n for n in range(9)]
        self.player = player
        self.firstMove = firstMove
        self.bot = bot
        self.bot.board = self.board
        self.winner = ''

    def move(self, player, pos):
        self.board[int(pos)] = player
        if self.movesLeft() == 0:
            self.winner = 'Tie!'
            print('Its a Tie!')
        else: self.checkWinner()

    def movesLeft(self):
        return len([pos for pos in self.board if type(pos) != str])

    def checkWinner(self):
        for pos in winningPos:
            if (self.board[pos[0]] == self.board[pos[1]]) & (self.board[pos[1]] == self.board[pos[2]]):
                self.winner = self.board[pos[0]]
                print('Winner Decided: {}'.format(self.winner))
                return

    def isTaken(self, movePos):
        openPos = [pos for pos in self.board if type(pos) != str]
        if movePos in openPos: return False
        return True

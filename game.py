import bot 
import random

winningPos = bot.winningPos

class Game:

    def __init__(self, player, bot, firstMove):
        # Numbers from 0 to 8, tracking the positions of the board.
        # Each number will be replaced with an 'X' or 'O' eventually.
        self.board = [n for n in range(9)]
        self.player = player
        self.firstMove = firstMove
        self.bot = bot
        self.bot.board = self.board


    def start(self):

        if self.player == self.firstMove:
            usrMove = input("Choose your first move: ")
            self.move(self.player, usrMove)

        while self.movesLeft() > 0:

            self.move(self.bot.player, self.bot.chooseMove(self.board))
            self.bot.board = self.board
            self.checkWinner()
            self.printBoard()

            usrMove = input("Choose a move: ")
            while self.isTaken(usrMove) == False:
                print("That move is taken!")
                usrMove = input("Choose a move: ")

            self.move(self.player, usrMove)
            self.checkWinner()

    def stop(self):
        print("GG")
        exit()

    def move(self, player, pos):
        self.board[int(pos)] = player
        return

    def movesLeft(self):
        return len([pos for pos in self.board if type(pos) != str])

    def checkWinner(self):
        if self.movesLeft() == 0:
            print("It's a draw!")
            self.stop()
        for pos in winningPos:
            if (self.board[pos[0]] == self.board[pos[1]]) & (self.board[pos[1]] == self.board[pos[2]]):
                self.printBoard()
                print("Winner Decided: {}".format(self.board[pos[0]]))
                self.stop()
                break

    def isTaken(self, movePos):
        openPos = [pos for pos in self.board if type(pos) != str]
        if movePos in openPos:
            return False
        return True

    def printBoard(self):
        print(self.board[0], "|", self.board[1], "|", self.board[2] )
        print("---------")
        print(self.board[3], "|", self.board[4], "|", self.board[5] )
        print("---------")
        print(self.board[6], "|", self.board[7], "|", self.board[8] )
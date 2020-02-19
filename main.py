import bot
import random

winningPos = [
    [0, 1, 2], [3, 4, 5], 
    [6, 7, 8], [0, 3, 6], 
    [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]
]

class Game:

    def __init__(self, player, bot, firstMove):
        # Numbers from 0 to 8, tracking the positions of the board.
        # Each number will be replaced with an 'X' or 'O' eventually.
        self.board = [n for n in range(9)]
        self.player = player
        self.firstMove = firstMove
        self.bot = bot

    def start(self):

        if self.player == self.firstMove:
            usrMove = input("Choose your first move: ")
            self.move(self.player, usrMove)

        while self.movesLeft() > 0:
            
            self.move(self.bot.player, self.bot.chooseMove(self.board))
            self.checkWinner()
            self.printBoard()
            
            usrMove = input("Choose a move: ")
            while self.isTaken(usrMove):
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
        for pos in winningPos:
            if board[pos[0]] == board[pos[1]] & board[pos[1]] == board[pos[2]]:
                print("Winner Decided: {}".format(board[pos[0]]))
                self.stop()
                break
    
    def isTaken(self, movePos):
        openPos = [pos for pos in self.board if type(pos) != str]
        if movePos in openPos:
            return false
        return true

    def printBoard(self):
        print(self.board)
        pass

# Randomly picks heads or tails to see who takes the first move
choice = random.choice(["heads", "tails"])

print("Welcome to TicTacToe. To see who goes first we will flip a coin.")
userChoice = input("Heads or Tails: ")
print("It was {}.".format(choice))

if userChoice.lower() == choice:
    bot = bot.Bot('O')
    game = Game('X', bot, 'X')
    print("You will go first, make your first move.")

else:
    bot = bot.Bot('X')
    game = Game('O', bot, bot.player)
    print("I will go first. Good luck beating me >:D")

game.start()

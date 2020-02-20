import bot
import game
import random

# Randomly picks heads or tails to see who takes the first move
choice = random.choice(["heads", "tails"])

print("Welcome to TicTacToe. To see who goes first we will flip a coin.")
userChoice = input("Heads or Tails: ")
print("It was {}.".format(choice))

if userChoice.lower() == choice:
    game = game.Game('X', bot.Bot('O', []), 'X')
    game.printBoard()
    print("You will go first, make your first move.")

else:
    game = game.Game('O', bot.Bot('X', []), 'X')
    print("I will go first. Good luck beating me >:D")

game.start()

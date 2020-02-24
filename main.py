import bot
import game
import random
import sys
import pygame
# Ryan Waite
print('\nWelcome to TicTacToe. To see who goes first we will flip a coin.\n')

userChoice = input("Heads or Tails: ")
choice = random.choice(['heads', 'tails'])
print('\nThe coin shows {}.'.format(choice))

game = game.Game('X', bot.Bot('O'), 'X')

if userChoice.lower() != choice:
    game.player = 'O'
    game.bot.player = 'X'
    print('\nI will go first. Good luck beating me >:D\n')

game.start()

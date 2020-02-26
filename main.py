import bot
import game
import random
import pygame

# pygame setup

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

GRID_WIDTH = 90
GRID_HEIGHT = 90

MARGIN = 5

WINDOW_SIZE = [300, 300]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TicTacToe")

gameOver = False

# Ryan Waite
"""
print('\nWelcome to TicTacToe. To see who goes first we will flip a coin.\n')

userChoice = input("Heads or Tails: ")
choice = random.choice(['heads', 'tails'])
print('\nThe coin shows {}.'.format(choice))

game = game.Game('X', bot.Bot('O'), 'X')

if userChoice.lower() != choice:
    game.player = 'O'
    game.bot.player = 'X'
    print('\nI will go first. Good luck beating me >:D\n')
"""

game = game.Game('X', bot.Bot('O'), 'X')
game.player = 'O'
game.bot.player = 'X'


# PyGame main loop
while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (GRID_WIDTH + MARGIN)
            row = pos[1] // (GRID_HEIGHT + MARGIN)
            grid[row][column] = game.player

    screen.fill(BLACK)

    for row in range(3):
        for column in range(3):
            color = WHITE
            if game.board[row][column] == 'X':
                color = BLUE
            if game.board[row][column] == 'O':
                color = GREEN
            pygame.draw.rect(screen, color, [
                (MARGIN + GRID_WIDTH) * column + MARGIN,
                (MARGIN + GRID_HEIGHT) * row + MARGIN,
                GRID_WIDTH, GRID_HEIGHT
            ])

    clock.tick(60)
    pygame.display.flip()

game.start()
pygame.quit()


"""

0 1 2 3 4 5 6 7 8

0,0 1,0 2,0
0,1 1,1 2,1
0,2 1,2 2,2

0 1 2
3 4 5
6 7 8

f(x,y) = (x+1) * (y+1) + (x - y)
f(0,0) = 0
f(1,1) = 4

"""

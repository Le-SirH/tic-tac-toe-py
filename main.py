import bot
import game
import random
import sys
import pygame

# pygame setup

pygame.init()
clock = pygame.time.Clock()

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
game = game.Game('X', bot.Bot('O'), 'X')
game.player = 'O'
game.bot.player = 'X'

# Ryan Harrington
def coordToNum(x, y):
    result = (y ** 2) + (y * 2) + x
    if y == 2: result -= 2
    return result

def checkWinner():
    winners = ['X', 'O', 'Tie!']
    if game.winner in winners:
        return True
    else: return False

grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

# PyGame main loop
while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if checkWinner() == True:
                break
            pos = pygame.mouse.get_pos()
            column = pos[0] // (GRID_WIDTH + MARGIN)
            row = pos[1] // (GRID_HEIGHT + MARGIN)
            game.move(game.player, coordToNum(column, row))
            if checkWinner() == False:
                game.move(game.bot.player, game.bot.chooseMove(game.board))
            else: break

    screen.fill(BLACK)

    for row in range(3):
        for column in range(3):
            color = WHITE
            if game.board[coordToNum(column, row)] == 'X':
                color = BLUE
            if game.board[coordToNum(column, row)] == 'O':
                color = GREEN
            pygame.draw.rect(screen, color, [
                (MARGIN + GRID_WIDTH) * column + MARGIN,
                (MARGIN + GRID_HEIGHT) * row + MARGIN,
                GRID_WIDTH, GRID_HEIGHT
            ])

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

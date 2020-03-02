import bot
import game
import random
import pygame

# pygame setup
# Ryan Waite
pygame.init()
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

GRID_WIDTH = 293.5
GRID_HEIGHT = 293.5

MARGIN = 5

WINDOW_SIZE = [900, 900]

xImg = pygame.image.load('x.png')
oImg = pygame.image.load('o.png')

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TicTacToe")

gameOver = False

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

def numToCoord(n):
    x = GRID_WIDTH * (n % 3) + (n - 1 * MARGIN)
    y = GRID_HEIGHT * (n // 3) + (n - 1 * MARGIN)
    return (x, y)

def coordinate():
    coord = ((MARGIN + GRID_WIDTH) * column + MARGIN,
            (MARGIN + GRID_HEIGHT) * row + MARGIN)
    return coord

# Ryan Waite
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

# PyGame main loop
while not gameOver:

    # Ryan Harrington
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (GRID_WIDTH + MARGIN)
            row = pos[1] // (GRID_HEIGHT + MARGIN)
            playerMove = coordToNum(column, row)
            if game.isTaken(playerMove):
                break
            elif checkWinner() == True:
                break
            else:
                game.move(game.player, playerMove)
                if checkWinner() == False:
                    game.move(game.bot.player, game.bot.chooseMove(game.board))
                else: break

    screen.fill(BLACK)

    # Ryan Waite
    for row in range(3):
        for column in range(3):
            color = WHITE
            if game.board[coordToNum(column, row)] == 'X':
                n = coordToNum(column, row)
                coord = numToCoord(n)
                screen.blit(xImg, coord)
            elif game.board[coordToNum(column, row)] == 'O':
                coord = coordinate()
                screen.blit(oImg, coord)
            else: pygame.draw.rect(screen, color, [
                (MARGIN + GRID_WIDTH) * column + MARGIN,
                (MARGIN + GRID_HEIGHT) * row + MARGIN,
                GRID_WIDTH, GRID_HEIGHT
            ])

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

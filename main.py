import bot

# Numbers from 0 to 8, tracking the positions of the board.
# Each number will be replaced with an 'X' or 'O' eventually.
board = [n for n in range(9)]

# Tracks the past moves of each player, preventing them from making the same move
xMoves = []
oMoves = []
choice=""
# Whenever a move is made, this modifies the board data & tracks past moves.
def move(player, pos):
    if player == 'X':
        xMoves.append(pos)
    else:
        oMoves.append(pos)
    board[pos] = player
    return print(board)

# Initializes the AI
bot = bot.Bot('X')
# Randomly picks heads or tails to see who takes the first move
def coinFlip(choice):
    choice=random.choice(["heads","tails"])
x0=random.choice(["x","o"])
print("Welcome to TicTacToe, you are",x0, + "'s. To see who goes first we will flip a coin.")
coinFlip()
userChoice=input("Heads or Tails")
if userChoice==choice:
    print("It was",choice, "You will go first, make your first move.")
    
else:
    print("It was",choice,"I will go first. Good luck beating me >:| ")    
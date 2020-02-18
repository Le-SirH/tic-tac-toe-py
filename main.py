# Numbers from 0 to 8, tracking the positions of the board.
# Each number will be replaced with an 'X' or 'O' eventually.
board = [n for n in range(9)]

# Tracks the past moves of each player, preventing them from making the same move
xMoves = []
oMoves = []

# Whenever a move is made, this modifies the board data & tracks past moves.
def move(player, pos):
    if player == 'X':
        xMoves.append(pos)
    board[pos] = player
    return print(board)

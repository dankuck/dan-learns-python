from copy import deepcopy

def plant(board, move):
    x, y = move
    if (x < 0 or y < 0 or x > 4 or y > 4):
        raise IndexError('Bad move, x or y outside of bounds 0:4')
    if (board[x][y] == '*'):
        raise RuntimeError('Cannot plant in occupied spot')
    board = deepcopy(board)
    board[x][y] = '*'
    return board

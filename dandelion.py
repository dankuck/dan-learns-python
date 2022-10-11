from copy import deepcopy

def plant(board, move):
    error = moveError(board, move)
    if (error):
        raise error
    x, y = move
    board = deepcopy(board)
    board[x][y] = '*'
    return board

def isValidMove(board, move):
    return moveError(board, move) == None

def moveError(board, move):
    x, y = move
    if (x < 0 or y < 0 or x > 4 or y > 4):
        return IndexError('Bad move, x or y outside of bounds 0:4')
    if (board[x][y] == '*'):
        return RuntimeError('Cannot plant in occupied spot')
    return None

class FixedStrategy:
    """
    This dummy strategy yields some arbitrarily chosen points
    where dandelions may be placed.
    """
    def __init__(self):
        self.i = 0
        self.moves = [
            (2, 2),
            (1, 3),
            (4, 2),
            (0, 1),
            (4, 4),
            (3, 3),
            (2, 0),
        ]

    def generateMove(self, board, compass):
        self.i += 1
        return self.moves[self.i - 1]

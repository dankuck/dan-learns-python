from copy import deepcopy

def blow(board, direction):
    board = deepcopy(board)
    for ri, row in enumerate(board):
        for ci, cell in enumerate(row):
            if (cell == '*'):
                blow_cell(board, ri, ci, direction)
    return board

def blow_cell(board, ri, ci, direction):
    if (direction == 'no' or direction == 'ne' or direction == 'nw'):
        if (ri == 0):
            return
        ri = ri - 1
    elif (direction == 'so' or direction == 'se' or direction == 'sw'):
        if (ri == 4):
            return
        ri = ri + 1
    if (direction == 'ea' or direction == 'ne' or direction == 'se'):
        if (ci == 4):
            return
        ci = ci + 1
    elif (direction == 'we' or direction == 'sw' or direction == 'nw'):
        if (ci == 0):
            return
        ci = ci - 1
    if (board[ri][ci] == ' '):
        board[ri][ci] = '.'
    blow_cell(board, ri, ci, direction)

class FixedStrategy:
    """
    This dummy strategy yields some arbitrarily chosen directions
    in which the wind can be blown.
    """
    def __init__(self):
        self.i = 0
        self.directions = [
            'no',
            'se',
            'nw',
            'ea',
            'ne',
            'sw',
            'so',
        ]

    def generateMove(self, board, compass):
        self.i += 1
        return self.directions[self.i - 1]

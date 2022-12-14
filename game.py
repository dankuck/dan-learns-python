from dandelion import plant
from wind import blow
from to_string import compass_to_string, board_to_string

def boardIsFull(board):
    for row in board:
        for cell in row:
            if (cell == ' '):
                return False
    return True

class Game:
    def __init__(self, dandelion, wind):
        self.dandelion = dandelion
        self.wind = wind
        self.board = [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
        self.compass = {
            'no': False,
            'ne': False,
            'ea': False,
            'se': False,
            'so': False,
            'sw': False,
            'we': False,
            'nw': False,
        }
        self.stepI = 0

    def play(self):
        while (not self.done()):
            self.step()
        return self.winner()

    def step(self):
        if (self.done()):
            raise RuntimeError('Game is already done')
        if (self.stepI % 2 == 0):
            self.board = plant(
                self.board,
                self.dandelion.generateMove(self.board, self.compass)
            )
        else:
            self.board, self.compass = blow(
                self.board,
                self.compass,
                self.wind.generateMove(self.board, self.compass)
            )
        self.stepI += 1

    def done(self):
        return self.winner() != None

    def winner(self):
        if (boardIsFull(self.board)):
            return self.dandelion
        if (self.stepI == 14):
            return self.wind
        return None

    def toString(self):
        return board_to_string(self.board) + "\n" + compass_to_string(self.compass)

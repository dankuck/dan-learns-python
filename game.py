from dandelion import plant
from wind import blow

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

    def play(self):
        for step in range(1, 7):
            self.board = plant(
                self.board,
                self.dandelion.generateMove(self.board, self.compass)
            )
            self.board, self.compass = blow(
                self.board,
                self.compass,
                self.wind.generateMove(self.board, self.compass)
            )
            if (boardIsFull(self.board)):
                return self.dandelion
        return self.wind

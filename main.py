from to_string import board_to_string, compass_to_string

print("DANDELIONS")

board = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

compass = {
    'no': False,
    'ne': False,
    'ea': False,
    'se': False,
    'so': False,
    'sw': False,
    'we': False,
    'nw': False,
}

print(board_to_string(board))
print(compass_to_string(compass))

board = [
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*']
]

compass = {
    'no': True,
    'ne': True,
    'ea': True,
    'se': True,
    'so': True,
    'sw': True,
    'we': True,
    'nw': True,
}

print(board_to_string(board))
print(compass_to_string(compass))

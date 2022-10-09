from to_string import board_to_string, compass_to_string

print('TESTS')

def it_prints_a_blank_board():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    string = board_to_string(board)
    expected = " - - - - - \n" \
               "|         |\n" \
               " - - - - - \n" \
               "|         |\n" \
               " - - - - - \n" \
               "|         |\n" \
               " - - - - - \n" \
               "|         |\n" \
               " - - - - - \n" \
               "|         |\n" \
               " - - - - - "
    assert(string == expected)

def it_prints_a_full_board():
    board = [
        ['*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*']
    ]
    string = board_to_string(board)
    expected = " - - - - - \n" \
               "|* * * * *|\n" \
               " - - - - - \n" \
               "|* * * * *|\n" \
               " - - - - - \n" \
               "|* * * * *|\n" \
               " - - - - - \n" \
               "|* * * * *|\n" \
               " - - - - - \n" \
               "|* * * * *|\n" \
               " - - - - - "
    assert(string == expected)

def it_prints_an_empty_compass():
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
    string = compass_to_string(compass)
    expected = "   \n" \
               " + \n" \
               "   "
    assert(string == expected)

def it_prints_a_full_compass():
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
    string = compass_to_string(compass)
    expected = "\\|/\n" \
                "-+-\n" \
                "/|\\"
    assert(string == expected)

tested = [
    it_prints_a_blank_board(),
    it_prints_a_full_board(),
    it_prints_an_empty_compass(),
    it_prints_a_full_compass(),
]

print('Tested:', len(tested))


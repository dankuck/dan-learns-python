from to_string import board_to_string, compass_to_string
from wind import blow

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

def it_blows_seeds_north():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'no');
    expected = [
        [' ', '.', ' ', ' ', ' '],
        [' ', '.', ' ', ' ', ' '],
        [' ', '.', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected);

def it_blows_seeds_south():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'so');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', '.', ' ', ' ', ' ']
    ]
    assert(after == expected);

def it_blows_seeds_east():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'ea');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', '.', '.', '.'],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected);

def it_blows_seeds_west():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'we');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['.', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected);

def it_blows_seeds_northeast():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'ne');
    expected = [
        [' ', ' ', ' ', ' ', '.'],
        [' ', ' ', ' ', '.', ' '],
        [' ', ' ', '.', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected);

def it_blows_seeds_southeast():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'se');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', '.', ' ', ' ']
    ]
    assert(after == expected);

def it_blows_seeds_southwest():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'sw');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        ['.', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected);

def it_blows_seeds_northwest():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'nw');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['.', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected);

def it_works_correctly_at_the_borders():
    '''
    The first way this was written, it would check if we were at a border and stop without
    considering that maybe we were not headed in the direction of that border. This now passes
    because we only check the borders that are in the direction we're headed in.
    '''
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'no');
    expected = [
        ['.', ' ', ' ', ' ', ' '],
        ['.', ' ', ' ', ' ', ' '],
        ['*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected)

    board = [
        [' ', ' ', '*', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'ea');
    expected = [
        [' ', ' ', '*', '.', '.'],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected)

    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '*'],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'so');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '*'],
        [' ', ' ', ' ', ' ', '.'],
        [' ', ' ', ' ', ' ', '.']
    ]
    assert(after == expected)

    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' ']
    ]
    after = blow(board, 'we');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['.', '.', '*', ' ', ' ']
    ]
    assert(after == expected)

def it_works_with_multiple_dandelions():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'se');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
        [' ', '*', ' ', '.', ' '],
        [' ', ' ', '.', ' ', '.']
    ]
    assert(after == expected)

def it_doesnt_destroy_other_dandelions_with_new_seeds():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'sw');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        ['.', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected)

def blow_returns_a_new_board():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    after = blow(board, 'no')
    after[0][0] = '*' # mess with the new board but not the old one
    assert(board != after)

tested = [
    it_prints_a_blank_board(),
    it_prints_a_full_board(),
    it_prints_an_empty_compass(),
    it_prints_a_full_compass(),
    it_blows_seeds_north(),
    it_blows_seeds_south(),
    it_blows_seeds_east(),
    it_blows_seeds_west(),
    it_blows_seeds_northeast(),
    it_blows_seeds_southeast(),
    it_blows_seeds_southwest(),
    it_blows_seeds_northwest(),
    it_works_correctly_at_the_borders(),
    it_works_with_multiple_dandelions(),
    it_doesnt_destroy_other_dandelions_with_new_seeds(),
    blow_returns_a_new_board(),
]

print('Tested:', len(tested))


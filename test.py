from to_string import board_to_string, compass_to_string
from wind import blow, FixedStrategy as WindFixedStrategy
from dandelion import plant, FixedStrategy as DandelionFixedStrategy
from game import Game

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
    after_board, after_compass = blow(board, compass, 'no');
    expected = [
        [' ', '.', ' ', ' ', ' '],
        [' ', '.', ' ', ' ', ' '],
        [' ', '.', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after_board == expected);

def it_blows_seeds_south():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'so');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', '.', ' ', ' ', ' ']
    ]
    assert(after_board == expected);

def it_blows_seeds_east():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'ea');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', '.', '.', '.'],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after_board == expected);

def it_blows_seeds_west():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'we');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['.', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after_board == expected);

def it_blows_seeds_northeast():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'ne');
    expected = [
        [' ', ' ', ' ', ' ', '.'],
        [' ', ' ', ' ', '.', ' '],
        [' ', ' ', '.', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after_board == expected);

def it_blows_seeds_southeast():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'se');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', '.', ' ', ' ']
    ]
    assert(after_board == expected);

def it_blows_seeds_southwest():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'sw');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        ['.', ' ', ' ', ' ', ' ']
    ]
    assert(after_board == expected);

def it_blows_seeds_northwest():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'nw');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['.', ' ', ' ', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after_board == expected);

def blow_works_correctly_at_the_borders():
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
    after_board, after_compass = blow(board, compass, 'no');
    expected = [
        ['.', ' ', ' ', ' ', ' '],
        ['.', ' ', ' ', ' ', ' '],
        ['*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after_board == expected)

    board = [
        [' ', ' ', '*', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'ea');
    expected = [
        [' ', ' ', '*', '.', '.'],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after_board == expected)

    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '*'],
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
    after_board, after_compass = blow(board, compass, 'so');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '*'],
        [' ', ' ', ' ', ' ', '.'],
        [' ', ' ', ' ', ' ', '.']
    ]
    assert(after_board == expected)

    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' ']
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
    after_board, after_compass = blow(board, compass, 'we');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['.', '.', '*', ' ', ' ']
    ]
    assert(after_board == expected)

def blow_works_with_multiple_dandelions():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'se');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
        [' ', '*', ' ', '.', ' '],
        [' ', ' ', '.', ' ', '.']
    ]
    assert(after_board == expected)

def blow_doesnt_destroy_other_dandelions_with_new_seeds():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'sw');
    expected = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
        [' ', '*', ' ', ' ', ' '],
        ['.', ' ', ' ', ' ', ' ']
    ]
    assert(after_board == expected)

def blow_returns_a_new_board_and_compass():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' '],
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
    after_board, after_compass = blow(board, compass, 'no')
    after_board[0][0] = '*' # mess with the new board but not the old one
    assert(board != after_board)
    assert(compass != after_compass)

def plant_plants_a_dandelion():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    move = 0, 0
    after = plant(board, move)
    expected = [
        ['*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert(after == expected)

def plant_cannot_plant_where_a_dandelion_already_exists():
    board = [
        ['*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    move = 0, 0
    try:
        plant(board, move)
    except (BaseException):
        return; # good job, you noticed that there's already a dandelion there
    assert(False); # bad job

def plant_cannot_plant_outside_the_boundary():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    bad_moves = [
        (-1, 2),
        (2, -1),
        (5, 2),
        (2, 5),
    ]
    errors = []
    for move in bad_moves:
        try:
            plant(board, move)
        except BaseException as e:
            errors.append(move)
    assert(len(errors) == len(bad_moves))

def plant_returns_a_new_board():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    move = 0, 0
    after = plant(board, move)
    assert(board != after)

def fixed_dandelion_strategy_gives_seven_different_moves():
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
    strategy = DandelionFixedStrategy()
    # 1
    move = strategy.generateMove(board, compass)
    board = plant(board, move)
    # 2
    move = strategy.generateMove(board, compass)
    board = plant(board, move)
    # 3
    move = strategy.generateMove(board, compass)
    board = plant(board, move)
    # 4
    move = strategy.generateMove(board, compass)
    board = plant(board, move)
    # 5
    move = strategy.generateMove(board, compass)
    board = plant(board, move)
    # 6
    move = strategy.generateMove(board, compass)
    board = plant(board, move)
    # 7
    move = strategy.generateMove(board, compass)
    board = plant(board, move)

def fixed_wind_strategy_gives_seven_different_moves():
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
    strategy = WindFixedStrategy()
    # 1
    move = strategy.generateMove(board, compass)
    assert(not compass[move])
    compass[move] = True
    # 2
    move = strategy.generateMove(board, compass)
    assert(not compass[move])
    compass[move] = True
    # 3
    move = strategy.generateMove(board, compass)
    assert(not compass[move])
    compass[move] = True
    # 4
    move = strategy.generateMove(board, compass)
    assert(not compass[move])
    compass[move] = True
    # 5
    move = strategy.generateMove(board, compass)
    assert(not compass[move])
    compass[move] = True
    # 6
    move = strategy.generateMove(board, compass)
    assert(not compass[move])
    compass[move] = True
    # 7
    move = strategy.generateMove(board, compass)
    assert(not compass[move])
    compass[move] = True

def blow_rejects_bad_directions():
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
    try:
        blow(board, compass, 'north-by-south')
    except BaseException:
        return # good, we expected an exception
    assert(False)

def blow_rejects_used_directions():
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    compass = {
        'no': True,
        'ne': False,
        'ea': False,
        'se': False,
        'so': False,
        'sw': False,
        'we': False,
        'nw': False,
    }
    try:
        blow(board, compass, 'no')
    except BaseException:
        return # good, we expected an exception
    assert(False)

def it_plays_a_game():
    dandelion = DandelionFixedStrategy()
    wind = WindFixedStrategy()
    game = Game(dandelion, wind)
    winner = game.play()
    assert(winner in {dandelion, wind})


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
    blow_works_correctly_at_the_borders(),
    blow_works_with_multiple_dandelions(),
    blow_doesnt_destroy_other_dandelions_with_new_seeds(),
    blow_returns_a_new_board_and_compass(),
    plant_plants_a_dandelion(),
    plant_cannot_plant_where_a_dandelion_already_exists(),
    plant_returns_a_new_board(),
    plant_cannot_plant_outside_the_boundary(),
    fixed_dandelion_strategy_gives_seven_different_moves(),
    fixed_wind_strategy_gives_seven_different_moves(),
    blow_rejects_bad_directions(),
    blow_rejects_used_directions(),
    it_plays_a_game(),
]

print('Tested:', len(tested))

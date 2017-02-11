# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random
import sys


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """

    field = list(range(1, 17))
    # field.append(EMPTY_MARK) #add EMPTY_MARK to the list as a 16-th element
    field[-1] = EMPTY_MARK
    random.shuffle(field)

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for row in range(0, len(field), 4):
        print(field[row:row+4])
    print('\n')


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    return field == [
        1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, EMPTY_MARK,
    ]


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    index = field.index(EMPTY_MARK)
    delta = MOVES[key]

    if (12 <= index <= 15 and key == 's') or \
    (0 <= index <= 3 and key == 'w') or \
    (index % 4 == 0 and key == 'a') or \
    (index % 4 == 3 and key == 'd'):
        raise IndexError('Move can not be done')

    new_index = index + delta

    field[index], field[new_index] = field[new_index], field[index]
    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move.
    """
    message = "Make your move {}: ".format(MOVES.keys())
    move = input(message)

    while move not in MOVES.keys():
        move = input(message)
    return move



def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    turns_count = 0
    field = shuffle_field()
    print_field(field)

    while is_game_finished(field) == False:
        try:
            move = handle_user_input()
            field = perform_move(field, move)
            print_field(field)
            turns_count += 1
        except IndexError as ex:
            print(ex)
    else:
        print("You win! You have made {} steps".format(turns_count))

if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    try:
        main()
    except KeyboardInterrupt:
        print("\nOk, I'm done.")
        sys.exit()

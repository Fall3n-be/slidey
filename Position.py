# Positions are used to identify cells on the board
import Dimension


def is_proper_position(position):
    """
        Check whether the given position is a proper position.
        - True if and only if the given position is a tuple of length 2
          whose first element is a lower-case letter or the letter 'X',
          and whose second element is a positive integer number.
        ASSUMPTIONS
        - None
    """
    if isinstance(position, tuple) and len(position) == 2:
        if isinstance(position[0], str) and len(position[0]) == 1 and (97 <= ord(position[0]) <= 122 or position[0] == 'X'):
            if isinstance(position[1], int) and position[1] > 0:
                return True
    return False


def get_row(position):
    """
        Return the row of the given position.
        ASSUMPTIONS
        - The given position is a proper position
    """
    return position[0]


def get_column(position):
    """
        Return the column of the given position.
        ASSUMPTIONS
        - The given position is a proper position
    """
    return position[1]


def nb_of_row(dimension, row):
    """
        Return the number of the row corresponding to the given letter in
        any board with the given dimension.
        - Rows are numbered starting from 1.
        ASSUMPTIONS
        - The given dimension is a proper dimension
        - The given row is a lower case letter or the letter 'X'.
    """
    if row == "X":
        return dimension[0]
    elif ord(row)-96 >= dimension[0]:
        return 0
    else:
        return ord(row) - 96



def id_of_row(dimension,row_nb):
    """
        Return the identification (the letter) of the nth row (n = row_nb) in
        any board with the given dimension.
        ASSUMPTIONS
        - The given dimension is a proper dimension
        - The given number is a positive integer number and does not exceed the
          number of rows of the given dimension.
    """
    if row_nb == dimension[0]:
        return 'X'
    else:
        char = chr(row_nb+96)
        return char


def is_within_boundaries(dimension, position):
    """
        Check whether the given position is within the boundaries of a
        board of the given dimension.
        - True if and only if (1) the row of the given position is either the
          letter 'X' or its position in the alphabet is in the range of
          the number of rows of the given dimension minus 1, and the column of the
          given position is in the range of the the number of columns of the
          given dimension.
        ASSUMPTIONS
        - The given dimension is a proper dimension.
        - The given position is a proper position
    """
    if nb_of_row(dimension, get_row(position)) and 1 <= get_column(position) <= dimension[1]:
        return True
    else:
        return False


def left(dimension, position, nb_steps=1):
    """
        Return the position on any board with the given dimension corresponding to
        the given number of steps to the left of the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given dimension is a proper dimension.
        - The given position is a proper position within the boundaries of
          any board with the given dimension.
        - The given number of steps is a positive integer number.
    """
    new_col_nb = get_column(position) - nb_steps
    if 1 <= new_col_nb <= dimension[1]:
        return position[0], new_col_nb
    else:
        return None


def right(dimension, position, nb_steps=1):
    """
        Return the position on any board with the given dimension corresponding to
        the given number of steps to the right of the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given dimension is a proper dimension.
        - The given position is a proper position within the boundaries of
          any board with the given dimension.
        - The given number of steps is a positive integer number.
    """
    return left(dimension, position, -nb_steps)


def up(dimension, position, nb_steps=1):
    """
        Return the position on any board with the given dimension corresponding to
        the given number of steps above of the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given dimension is a proper dimension.
        - The given position is a proper position within the boundaries of
          any board with the given dimension.
        - The given number of steps is a positive integer number.
    """
    new_nb_row = nb_of_row(dimension, position[0]) + nb_steps
    if 1 <= new_nb_row <= dimension[0]:
        return id_of_row(dimension, new_nb_row), position[1]
    else:
        return None


def down(dimension, position, nb_steps=1):
    """
        Return the position on any board with the given dimension corresponding to
        the given number of steps below of the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given dimension is a proper dimension.
        - The given position is a proper position within the boundaries of
          any board with the given dimension.
        - The given number of steps is a positive integer number.
    """
    return up(dimension, position, -nb_steps)

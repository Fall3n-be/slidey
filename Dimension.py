# Dimensions are used to specify the number of rows and the number of columns
# of a board.


def is_proper_dimension(dimension):
    """
        Check whether the given dimension is a proper dimension for a rectangular
        area consisting of horizontal rows and vertical columns.
        - True if and only if the given dimension is a tuple consisting of
          exactly two integer numbers greater than or equal to 2.
        - The first number registers the number of rows;
          the second number registers the number of columns.
        ASSUMPTIONS
        - None
    """
    if isinstance(dimension, tuple) and len(dimension) == 2:
        if isinstance(dimension[0], int) and isinstance(dimension[1], int):
            if dimension[0] >= 2 and dimension[1] >= 2:
                return True
    return False


def get_nb_of_rows(dimension):
    """
        Return the number of rows on a board with the given dimension.
        ASSUMPTIONS
        - The given dimension is a proper dimension.
    """
    return dimension[0]


def get_nb_of_columns(dimension):
    """
        Return the number of columns on a board with the given dimension.
        - The given dimension is a proper dimension.
    """
    return dimension[1]

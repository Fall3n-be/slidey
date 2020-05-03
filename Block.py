import Color
import Dimension
import Position

ORDINARY    = 1
ELECTRIFIED = 2
FRAGILE     = 3


def make_block(length, type=ORDINARY, color = Color.BLACK):
    """
      Return a block of the given length, of the given type and with the given
      color.
      ASSUMPTIONS
      - The given length is a positive integer number.
      - The given type is either ORDINARY, ELECTRIFIED or FRAGILE.
      - The given color is a proper color.
    """
    return length, type, color


def is_proper_block(block):
    """
      Check whether the given block is a proper block.
      - True if and only if the given block has a positive length, has a proper type
        and a proper color.
      ASSUMPTIONS
      - None
    """
    if isinstance(block[0], int) and isinstance(block[1], int) and Color.is_proper_color(block[2]):
        if block[0] > 0 and 1 <= block[1] <= 3:
            return True
    return False


def make_random_block(max_length):
    """
        Return a random block whose length does not exceed the given maximum length.
        - On average, 80% of the blocks will be ordinary blocks; 15% will be
          electrified blocks and 5% will be fragile blocks.
        ASSUMPTIONS
        - The given maximum length is a positive integer number.
        NOTE
        - This function is already provided (you do not have to work out this function yourself).
    """
    import random
    assert isinstance(max_length,int)
    assert max_length > 0
    length = random.randint(1,max_length)
    random_type = random.randint(1,20 if length>1 else 16)
    type = ORDINARY if random_type <= 16 \
        else ELECTRIFIED if random_type < 20 else FRAGILE
    color = Color.get_random_color()
    return make_block(length,type,color)


def split_block(block):
    """
      Split the given block in two smaller blocks.
      - The function returns a tuple of two new blocks.
      - The length of the first block in the resulting tuple is equal to the quotient
        of the length of the given block incremented by 1 and divided by 2.
      - The length of the second block in the resulting tuple is equal to the quotient
        of the length of the given block divided by 2.
      - Blocks in the resulting tuple with an even length are fragile; blocks with an
        odd length are ordinary blocks.
      - Both blocks have the same color as the given block.
      ASSUMPTIONS
      - The given block is a proper block.
    """
    len_1 = int((block[0]+1)//2)
    len_2 = int(block[0]//2)
    block_1 = len_1, ORDINARY if len_1 % 2 else FRAGILE, block[2]
    block_2 = len_2, ORDINARY if len_2 % 2 else FRAGILE, block[2]
    return block_1, block_2


def is_proper_block_for_dimension(block,dimension):
    """
      Check whether the given block is a proper block for a board with
      the given dimension.
      - True if and only if the length of the given block does not exceed
        half the number of columns of the given dimension.
      ASSUMPTIONS
      - The given block is a proper block
      - The given dimension is a proper dimension
    """
    if block[0] <= Dimension.get_nb_of_columns(dimension)/2:
        return True
    else:
        return False


def get_length(block):
    """
      Return the length of the given block.
      ASSUMPTIONS
      - The given block is a proper block
    """
    return block[0]


def get_type(block):
    """
      Return the type of the given block.
      ASSUMPTIONS
      - The given block is a proper block
    """
    return block[1]


def get_color(block):
    """
      Return the color of the given block.
      ASSUMPTIONS
      - The given block is a proper block
    """
    return block[2]


def get_symbol(block):
    """
      Return the symbol to display a single cell of the given block.
      ASSUMPTIONS
      - The given block is a proper block
      NOTE
      - The body of this function must be included in the skelet.
    """
    assert is_proper_block(block)
    if get_type(block) == ORDINARY:
        return "\u25A2"
    elif get_type(block) == ELECTRIFIED:
        return "\u25A3"
    else:
        return "\u25A4"

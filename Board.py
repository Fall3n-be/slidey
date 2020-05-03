import Color
import Dimension
import Position
import Block
from collections import defaultdict, OrderedDict
import random
import copy


def is_proper_board(board):
    """
        Check whether the given board is a proper board.
        - ...
        ASSUMPTIONS
        - None
        NOTE
        - You need to work out the conditions yourself as they depend on how
          you store the state of a board.
        (as they depend on the internal representation you have chosen for the board)
    """
    return isinstance(board, defaultdict) and 'dimension' in board


def make_board(dimension):
    """
        Return a new board of the given dimension without any blocks yet.
        ASSUMPTIONS
        - The given dimension is a proper dimension.
    """
    board = defaultdict(dict)
    board['dimension'] = dimension
    return board


def copy_board(board):
    """
        Return a copy of the given board loaded with copies of the blocks on
        the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    return copy.deepcopy(board)


def get_dimension(board):
    """
        Return the dimension of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    return board['dimension']


def get_block_at(board, position):
    """
        Return the block occupying the given position of the given board.
        - The function returns None if (1) the given position is outside the
          boundaries of the given board, or if (2) no block occupies the
          given position of the given board
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
    """
    if Position.is_within_boundaries(get_dimension(board), position):
        try:
            return board[Position.get_row(position)][Position.get_column(position)]
        except KeyError:
            return None
    else:
        return None


def is_free_at(board, position):
    """
      Check whether the cell at the given position on the given board is free.
      - True if and only if (1) the given position is within the boundaries of
        the given board, and (2) none of the blocks on the board occupies the
        given position.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
    """
    if Position.is_within_boundaries(get_dimension(board), position):
        try:
            board[Position.get_row(position)][Position.get_column(position)]
            return False
        except KeyError:
            return True
    else:
        return False


def get_leftmost_position_of(board, block):
    """
        Return the leftmost position occupied by the given block on the given board.
        - The function returns None if the given block is not loaded on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block for the dimension of the given board.
    """
    for i in range(1, Dimension.get_nb_of_rows(get_dimension(board)) + 1):
        row_id = Position.id_of_row(get_dimension(board), i)
        for j in range(1, Dimension.get_nb_of_columns(get_dimension(board)) + 1):
            try:
                if board[row_id][j] is block:
                    return row_id, j
            except KeyError:
                pass
    return None


def get_all_positions_of(board, block):
    """
        Return a tuple containing all the positions of all the cells occupied by
        the given block on the given board.
        - Positions are ordered from left to right in the resulting tuple.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block for the dimension of the given board.
        - The given block is loaded on the given board.
    """
    positions = ()
    for row, dict in board.items():
        if row == 'dimension':
            continue
        for column, value in dict.items():
            if value is block:
                positions += ((row, column),)
    return positions


def get_random_position_for(board, block, row="a"):
    """
        Return a position in the given row of the given board at which the given
        block can be placed without overlapping with blocks already on the given board.
        - The function returns None if no position exists to place the given block
          in the given row.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block for the given board.
        - The given row is within the boundaries of the given board.
    """
    solutions = ()
    length = Block.get_length(block)
    max_columns = Dimension.get_nb_of_columns(get_dimension(board))
    for i in range(1, max_columns + 1):
        if is_free_at(board, (row, i)):
            for j in range(1, length + 1):
                if not is_free_at(board, (row, i + j - 1)):
                    break
                if j == length:
                    solutions += ((row, i),)
    try:
        return random.choice(solutions)
    except IndexError:
        return None


def get_all_blocks_in_row(board, row):
    """
        Return a list of all the blocks in the given row of the given board.
        - Each block in the given row is stored exactly once in the resulting
          list.
        - The blocks are stored in the resulting list as they occur in the given
          row in the order from left to right.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given row is within the boundaries of the given board.
    """
    blocks = []
    i = 1
    while i <= Dimension.get_nb_of_columns(get_dimension(board)):
        try:
            blocks.append(board[row][i])
            i += Block.get_length(board[row][i])
        except KeyError:
            i += 1
    return blocks


def get_length_largest_gap_in_row(board, row):
    """
        Return the length of the largest gap (largest consecutive sequence of
        empty cells) in the given row on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given row is within the range of the given board.
    """
    max_columns = Dimension.get_nb_of_columns(get_dimension(board))
    if row not in board:
        return Dimension.get_nb_of_columns(get_dimension(board))
    for i in range(1, max_columns + 1):
        block = Block.make_block(i)
        if get_random_position_for(board, block, row) is None:
            return i - 1


def is_empty_row(board, row):
    """
        Check whether the given row on the given board is empty.
        - True if and only if the given row does not contain any block.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given row is within the range of the given board.
    """
    try:
        if board[row]:
            return False
        else:
            return True
    except KeyError:
        return True


def is_full_row(board, row):
    """
        Check whether the given row on the given board is completely filled
        with blocks.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given row is within the range of the given board.
    """
    max_columns = Dimension.get_nb_of_columns(get_dimension(board))
    if len(board[row]) == max_columns:
        return True
    else:
        return False


def get_all_full_rows(board):
    """
        Return a frozen set of the letters of all the rows that are completely
        filled with blocks.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    full_rows = []
    max_rows = Dimension.get_nb_of_rows(get_dimension(board))
    for i in range(1, max_rows + 1):
        row_id = Position.id_of_row(get_dimension(board), i)
        if is_full_row(board, row_id):
            full_rows.append(row_id)
    return frozenset(full_rows)


def get_all_blocks(board):
    """
        Return a list of all the blocks on the given board.
        - Each block on the given board is stored exactly once in the resulting
          list.
        - The blocks are ordered according to their position on the board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    all_blocks = []
    max_rows = Dimension.get_nb_of_rows(get_dimension(board))
    for i in range(1, max_rows + 1):
        all_blocks.extend(get_all_blocks_in_row(board, Position.id_of_row(get_dimension(board), i)))
    return all_blocks


def contains_block(board, block):
    """
        Check whether the given board contains the given block.
        - The function returns True if and only if one of the blocks on the
          given board is the same (referential equality) as the given block.
        - The function returns False if none of the blocks is the same as the
          given block, even if some blocks on the board are identical (same length,
          same type, same position) to the given block.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
    """
    for item in get_all_blocks(board):
        if item is block:
            return True
    return False


def can_accept_block_at(board, block, position):
    """
      Check whether the given board can accept the given block at the given
      position.
      - True if and only if (1) the given block is a proper block for
        the dimension of the given board, (2) the given block is not already
        loaded on the given board and (3) all the cells that would
        be occupied by the given block are free and within the boundaries
        of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given position is a proper position.
    """
    length = Block.get_length(block)
    if Block.is_proper_block_for_dimension(block, get_dimension(board)) and not contains_block(board, block):
        for i in range(length):
            if not is_free_at(board, (Position.get_row(position), Position.get_column(position) + i)):
                return False
        return True
    return False


def add_block_at(board, block, position):
    """
        Add the given block at the given position on the given board.
        - If the given position is equal to (r,c), the given block will occupy the
          cells (r,c), (r,c+1), ..., (r,c+L-1) on the given board, in which L denotes
          the length of the given block.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given position is a proper position.
        - The given board can accept the given block at the given position.
    """
    for i in range(Block.get_length(block)):
        board[Position.get_row(position)][Position.get_column(position) + i] = block


def remove_block_from(board, block):
    """
        Remove the given block from the given board.
        - No other blocks change their position as a result of removing the given
          block.
        - Nothing happens if the given block is not loaded on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
    """
    if contains_block(board, block):
        position = get_leftmost_position_of(board, block)
        for i in range(Block.get_length(block)):
            del board[Position.get_row(position)][Position.get_column(position) + i]


def is_airborne(board, block):
    """
        Check whether the given block is airborne on the given board.
        - True if and only if the given block is (1) not positioned on the bottom row
          of the given board, and (2) not fully or partially on top of some other block
          on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
    """
    position = get_leftmost_position_of(board, block)
    if not Position.get_row(position) == 'a':
        positions = get_all_positions_of(board, block)
        for pos in positions:
            if not is_free_at(board, Position.down(get_dimension(board), pos)):
                return False
        return True
    else:
        return False


def get_adjacent_blocks_above(board, block):
    """
        Return a list of all the blocks on the given board directly adjacent
        to the top of the given block on the given board.
        - Each block in the resulting list has some part of its bottom border
          in common with some part of the top border of the given block.
        - The blocks in the resulting list are ordered in ascending order of their
          position.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
        NOTE
        - This function must be worked out in an ITERATIVE way.
    """
    blocks = []
    cache = None
    pos = get_leftmost_position_of(board, block)
    if Position.get_row(pos) == 'X':
        return blocks
    pos_above = Position.up(get_dimension(board), pos)
    for i in range(Block.get_length(block)):
        block_above = get_block_at(board, (Position.get_row(pos_above), Position.get_column(pos_above) + i))
        if block_above is not None and block_above is not cache:
            blocks.append(block_above)
        cache = block_above
    return blocks


def get_adjacent_block_left(board, block):
    """
        Return the block adjacent to the left of the given block on the given board.
        - None is returned if no such block exists.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
    """
    position = get_leftmost_position_of(board, block)
    position_left = Position.left(get_dimension(board), position)
    if position_left is None:
        return None
    return get_block_at(board, position_left)


def get_adjacent_blocks_below(board, block, from_position=None):
    """
        Return a list of all the blocks on the given board directly adjacent
        to the bottom of the given block on the given board.
        - Each block in the resulting list has some part of its top border
          in common with some part of the bottom border of the given block.
        - The blocks in the resulting list are ordered in ascending order of their
          position.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
        NOTE
        - This function must be worked out in a recursive way.
    """
    if from_position is None:
        from_position = get_leftmost_position_of(board, block)
        if Position.get_row(get_leftmost_position_of(board, block)) == 'a':
            return []
    elif get_block_at(board, from_position) is not block:
        return []

    dim = get_dimension(board)
    block_below = get_block_at(board, Position.down(dim, from_position))
    right = Position.right(dim, from_position)
    if right is None:
        if block_below is None:
            return []
        else:
            return [block_below]
    recursive_blocks = get_adjacent_blocks_below(board, block, right)

    if block_below and (len(recursive_blocks) == 0 or recursive_blocks[0] is not block_below):
        return [block_below] + recursive_blocks
    else:
        return recursive_blocks


def get_adjacent_block_right(board, block):
    """
        Return the block adjacent to the right of the given block on the given board.
        - None is returned if no such block exists.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
    """
    position = get_leftmost_position_of(board, block)
    position_right = Position.right(get_dimension(board), position, Block.get_length(block))
    if not position_right:
        return None
    return get_block_at(board, position_right)


def get_supporting_blocks(board, block):
    """
        Return a frozen set of all the positions of the blocks on the given board
        directly or indirectly supporting the given block on the given board.
        - The resulting set only includes the position of the leftmost cell of each
          of the supporting blocks (and not all positions it occupies).
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
        NOTE
        - This function must be worked out in an ITERATIVE way.
    """
    to_check = get_adjacent_blocks_below(board, block)
    solutions = to_check.copy()
    while to_check:
        check = to_check.pop()
        blocks_below = get_adjacent_blocks_below(board, check)
        solutions.extend(blocks_below)
        to_check.extend(blocks_below)

    pos_solutions = []
    for block in solutions:
        pos_solutions.append(get_leftmost_position_of(board, block))

    return frozenset(pos_solutions)


def get_supported_blocks(board, block):
    """
        Return a mutable set of all the positions of the blocks on the given board
        directly or indirectly supported by the given block on the given board.
        - A block B directly supports another block S if the top border of at least
          one of B's cells coincides with the bottom border of block S.
        - A block B indirectly supports another block S if it supports at least one
          other block X that directly or indirectly supports block S.
        - The resulting set only includes the position of the leftmost cell of each
          of the supported blocks (and not all positions it occupies).
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
        NOTE
        - This function must be worked out in a RECURSIVE way.
    """
    solutions = set()
    for item in get_adjacent_blocks_above(board, block):
        solutions.add(get_leftmost_position_of(board, item))
        solutions = solutions.union(get_supported_blocks(board, item))
    return solutions


def let_fall(board, block):
    """
        Let the given block fall down until it is no longer airborne.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
    """
    while is_airborne(board, block):
        position = get_leftmost_position_of(board, block)
        remove_block_from(board, block)
        add_block_at(board, block, Position.down(get_dimension(board), position))


def let_all_blocks_fall(board):
    """
        Let all the blocks in the given board fall down until none of them is still
        airborne.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    for block in get_all_blocks(board):
        let_fall(board, block)


def let_explode(board, block):
    """
        Let the given block on the given board explode.
        - The function returns the score resulting from the explosion.
        - If the given block is an ordinary block, the given block is removed from
          the given board. The score for having an ordinary block explode is equal
          to the length of that block.
        - If the given block is a fragile block, the given block is replaced on the
          given board by the blocks obtained from splitting the given block. The score
          for having a fragile block explode is equal to twice the length of that block.
        - If the given block is an electrified block, the given block is removed from
          the given board, and all the blocks immediately below and above the given block
          explode. The score for having an electrified block explode is equal to
          the length of that block incremented with the scores of explosions of blocks
          above and below the given block.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
    """
    score = 0
    if Block.get_type(block) is Block.ORDINARY:
        score += Block.get_length(block)
        remove_block_from(board, block)
    elif Block.get_type(block) is Block.FRAGILE:
        score += 2 * Block.get_length(block)
        position = get_leftmost_position_of(board, block)
        remove_block_from(board, block)
        block1, block2 = Block.split_block(block)
        add_block_at(board, block1, position)
        add_block_at(board, block2, Position.right(get_dimension(board), position, round(Block.get_length(block) / 2)))
    else:
        score += Block.get_length(block)
        to_explode = get_adjacent_blocks_below(board, block) + get_adjacent_blocks_above(board, block)
        remove_block_from(board, block)
        for item in to_explode:
            score += let_explode(board, item)
    return score


def is_stable(board):
    """
        Check whether the given board is stable.
        - True if and only if none of the blocks on the given board are airborne.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    for block in get_all_blocks(board):
        if is_airborne(board, block):
            return False
    return True


def push_all_blocks_in_row_up(board, row):
    """
        Push all the blocks in the given row of the given board one row up.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given row is within the boundaries of the given board.
        - The given row is not the overflow row of the given board.
        - The row above the given row is empty.
    """
    dim = get_dimension(board)
    new_row_id = Position.id_of_row(dim, Position.nb_of_row(dim, row) + 1)
    board[new_row_id] = board[row]
    del board[row]


def push_all_blocks_up(board):
    """
        Push all the blocks on the given board one row up.
        ASSUMPTIONS
        - The given board is a proper board.
        - The overflow row of the given board is empty.
    """
    amount_rows = Dimension.get_nb_of_rows(get_dimension(board))
    for i in range(1, amount_rows):
        row_id = Position.id_of_row(get_dimension(board), amount_rows - i)
        push_all_blocks_in_row_up(board, row_id)


def fill_bottom_row(board, max_block_length):
    """
        Fill the bottom row of the given board with new blocks whose length does
        not exceed the given maximum length.
        - Upon completion, there will be at least one free cell in the bottom row and
          it will not be possible to add an additional block of the given maximum
          length to the bottom row.
        ASSUMPTIONS
        - The given board is a proper board.
        - The bottom row of the given board is empty.
        - The given maximum length is at least 2 and does not exceed halve the number
          of columns in the given board.
        NOTE
        - This function is already provided (you do not have to work out this function yourself).
    """
    nb_filled_cells = 0
    block_to_add = Block.make_random_block(max_block_length)
    position_for_block = get_random_position_for(board, block_to_add)
    while (position_for_block is not None) and \
            (nb_filled_cells + Block.get_length(block_to_add) < \
             Dimension.get_nb_of_columns(get_dimension(board))):
        add_block_at(board, block_to_add, position_for_block)
        nb_filled_cells += Block.get_length(block_to_add)
        block_to_add = Block.make_random_block(max_block_length)
        position_for_block = get_random_position_for(board, block_to_add)


def insert_bottom_row(board, blocks):
    """
        Push all blocks on the given board one row up, and subsequently fill the
        bottom row of the given board with the given sequence of blocks.
        ASSUMPTIONS
        - The given board is a proper board.
        - The overflow row of the given board is empty.
        - Each basic element in the list of blocks ((blocks[I][J]) is a tuple
          involving a (leftmost) position in the bottom row of the board followed by
          a proper block for a board with the given dimension.
        NOTE
        - This function is already provided (you do not have to work out this function yourself).
    """
    push_all_blocks_up(board)
    for (leftmost_position, block) in blocks:
        add_block_at(board, block, leftmost_position)


def can_move_over(board, block, nb_steps):
    """
        Check whether the given block on the given board can be moved horizontally
        over the given number of steps .
        - The movement is to the left if the given number of steps is negative;
          it is to the right if the given number of steps is positive.
        - True if and only if each of the cells over which the block has to move
          (1) is within the boundaries of the given board and (2) is free.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
    """
    if not isinstance(nb_steps, int):
        return False
    position = get_leftmost_position_of(board, block)
    cboard = copy_board(board)
    remove_block_from(cboard, block)
    moved_position = Position.right(get_dimension(board), position, nb_steps)
    if not moved_position:
        return False
    if can_accept_block_at(cboard, block, moved_position):
        return True
    return False


def move_block_horizontally(board, block, nb_steps):
    """
        Move the given block on the given board over the given number of steps.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given block is loaded on the given board.
        - The given block can move over the given number of steps.
    """
    position = get_leftmost_position_of(board, block)
    remove_block_from(board, block)
    add_block_at(board, block, Position.right(get_dimension(board), position, nb_steps))


def print_board(board):
    """
        Print the given board on the standard output stream.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - This function is already provided (you do not have to work out this function yourself).
    """
    current_position = ("X", 1)
    while current_position is not None:
        for lines in range(0, 2):
            if lines == 1:
                print("\033[1;31;48m" + '{:2}'.format(Position.get_row(current_position)), end="  ")
            else:
                print("\033[1;30;48m" + "  ", end="  ")
            column_position = current_position
            left_position = None
            while column_position is not None:
                current_block = get_block_at(board, column_position)
                right_position = Position.right(get_dimension(board), column_position)
                if current_block is None:
                    print("\033[1;30;48m" + ("|   " if lines == 1 else "----"), end="")
                else:
                    block_symbol = Block.get_symbol(current_block)
                    if (left_position is None) or \
                            (get_block_at(board, left_position) is not current_block):
                        # Leftmost cell of a block.
                        if lines == 1:
                            print("\033[1;" + str(Block.get_color(current_block)) + ";48m|" + block_symbol * 3, end="")
                        else:
                            print("\033[1;30;48m----", end="")
                    else:
                        if lines == 1:
                            print("\033[1;" + str(Block.get_color(current_block)) + ";48m" + block_symbol * 4, end="")
                        else:
                            print("\033[1;30;48m----", end="")
                left_position = column_position
                column_position = right_position
            print("\033[1;30;48m" + ("|" if lines == 1 else "-"))
        current_position = Position.down(get_dimension(board), current_position)
    print("   ", "\033[1;30;48m" + ("-" * (Dimension.get_nb_of_columns(get_dimension(board)) * 4 + 1)))
    print("    ", end="")
    for column in range(1, Dimension.get_nb_of_columns(get_dimension(board)) + 1):
        print("\033[1;30;48m" + '{:3d}'.format(column), end=" ")
    print()

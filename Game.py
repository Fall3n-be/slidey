import Color
import Dimension
import Position
import Block
import Board


def let_all_full_rows_explode(board):
    """
        Let all the blocks in all the full rows on the given board explode.
        - The function starts with examining the given board collecting all the
          blocks in all rows that are completely filled. Hereafter, it will let
          each of these blocks explode exactly once in ascending order of their
          position.
        - If part of a full row has already exploded because of explosions of
          (electrified) blocks in lower rows, other blocks in that row will still
          explode (even if the row is no longer completely filled).
        - If a fragile block in a full row has already exploded because of explosions
          of (electrified) blocks in lower rows, the replacing blocks will not explode
          on their own. They may, however, explode as a result of other electrified
          blocks exploding.
        - The function returns the score resulting from all explosions.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - This function is already provided (you do not have to work out this function yourself).
    """
    assert Board.is_proper_board(board)
    blocks_to_explode = []
    full_rows_sorted = list(Board.get_all_full_rows(board))
    list.sort(full_rows_sorted)
    for row in full_rows_sorted:
        list.extend(blocks_to_explode, Board.get_all_blocks_in_row(board, row))
    total_score = 0
    for block in blocks_to_explode:
        if Board.contains_block(board, block):
            total_score += Board.let_explode(board, block)
    return total_score


def adjust_score(score, level, score_from_explosions, nb_full_rows, nb_columns):
    """
        Return the new score and the new level in view of the given score, the given
        level, the score resulting from explosions that have taken place, the total
        number of full rows in which these explosions took place and the number of
        columns on the board.
        NOTE
        - This function is already provided (you do not have to work out this function yourself). Its details are irrelevant.
    """

    def treshold_for_level(level):
        if level == 1:
            return 11 * nb_columns
        else:
            return treshold_for_level(level - 1) + (10 + level) * nb_columns * level

    extra_score = score_from_explosions * nb_full_rows * level
    score += extra_score
    if score > treshold_for_level(level):
        level += 1
    return (score, level)


def stabilize_board(level, score, board):
    """
        Stabilize the given board and return the updated level and score in view of
        the given level and given score.
        - The function continuously lets all blocks on the given board fall down,
          followed by explosions of all full rows, until the board is stable.
        - The function returns a tuple (l,s) in which l is the new level and s is
          the new score in view of the given level and given score.
        ASSUMPTIONS
        - The given level is a positive integer number.
        - The given score is a non-negative integer number.
        - The given board is a proper board.
        NOTE
        - This function is already provided (you do not have to work out this function yourself).
    """
    assert isinstance(level, int) and (level >= 1)
    assert isinstance(score, int) and (score >= 0)
    assert Board.is_proper_board(board)
    Board.let_all_blocks_fall(board)
    nb_full_rows = len(Board.get_all_full_rows(board))
    while (nb_full_rows > 0):
        if nb_full_rows > 0:
            score_from_explosions = let_all_full_rows_explode(board)
            score, level = \
                adjust_score(score, level, score_from_explosions, nb_full_rows,
                             Dimension.get_nb_of_columns(Board.get_dimension(board)))
        Board.let_all_blocks_fall(board)
        nb_full_rows = len(Board.get_all_full_rows(board))
    return (level, score)


def get_all_possible_moves(board):
    all_possible_moves = []
    for block in Board.get_all_blocks(board):
        i = 1
        check1 = False
        check2 = False
        while 1:
            if Board.can_move_over(board, block, i) and not check1:
                all_possible_moves.append((block, i))
            else:
                check1 = True
            if Board.can_move_over(board, block, -i) and not check2:
                all_possible_moves.append((block, -i))
            else:
                check2 = True
            if check1 and check2:
                break
            i += 1
    return all_possible_moves


def play_greedy(blocks, dimension=(8, 10)):
    """
       Play the game in a greedy way on a board with the given dimension,
       using the given blocks to fill the bottom row in each step of the game.
       The function repeatedly shifts all blocks up one row, adds new blocks to the
       bottom row and stabilizes the board, computes the move that yields the highest
       score, and makes that move.
       - The given blocks are collected in a list of which each element is a list of
         blocks to fill the bottom row once.
       - The function computes and executes in each step the move yielding the
         highest score.
       - The function returns a tuple consisting of the total score after all
         the given blocks have been used or as soon as the game has come to an end,
         followed by a list of all the moves that have been made. Each move in the
         latter list is a tuple containing the block to move, followed by the
         distance over which that block has been moved.
       ASSUMPTIONS
       - The given dimension is a proper dimension.
       - Each element in the list of blocks ((blocks[I]) is a sequence that can be
         used to fill the bottom row once in a valid way (i.e., no overlapping
         positions, no remaining gap larger than half the number of columns after
         a complete fill, ...)
       - The elements in the list of blocks (blocks[I]) are used in the order from left
         to right.
       - Each basic element in the list of blocks ((blocks[I][J]) is a tuple
         involving a (leftmost) position in the bottom row of the board followed by
         a proper block for a board with the given dimension.
    """
    if not blocks:
        return 0, []

    board = Board.make_board(dimension)
    level = 1
    score = 0
    total_moves = []
    while blocks:
        Board.insert_bottom_row(board, blocks.pop(0))
        level, score = stabilize_board(level, score, board)
        all_possible_moves = get_all_possible_moves(board)
        max_score = 0
        best_moves = []
        for move in all_possible_moves:
            board_copy = Board.copy_board(board)
            Board.move_block_horizontally(board_copy, move[0], move[1])
            temp_level, temp_score = stabilize_board(level, score, board_copy)
            if temp_score > max_score:
                max_score = temp_score
                best_moves = [move]
            elif temp_score == max_score:
                best_moves.append(move)
        if len(best_moves) > 1:
            lowest_block_moves = []
            lowest_row = Dimension.get_nb_of_rows(dimension)
            lowest_column = Dimension.get_nb_of_columns(dimension)
            for move in best_moves:
                pos = Board.get_leftmost_position_of(board, move[0])
                row_nb = Position.nb_of_row(dimension, Position.get_row(pos))
                col = Position.get_column(pos)
                if row_nb <= lowest_row:
                    lowest_row = row_nb
                    if col < lowest_column:
                        lowest_column = col
                        lowest_block_moves = [move]
                    elif col == lowest_column:
                        lowest_block_moves.append(move)
            if len(lowest_block_moves) > 1:
                lowest_move = Dimension.get_nb_of_columns(dimension)
                for move in lowest_block_moves:
                    if move[1] < lowest_move:
                        lowest_move = move[1]
                        best_moves = [move]
            else:
                best_moves = lowest_block_moves
        total_moves.append(best_moves[0])
        Board.move_block_horizontally(board, best_moves[0][0], best_moves[0][1])
        level, score = stabilize_board(level, score, board)
    return score, total_moves


def get_top_moves(board, blocks, min_score=100, max_nb_moves=10, level=1, score=0):
    """
       Compute the best possible moves to play the game on the given board starting from
       the given level and the given score using the given blocks to fill the bottom row
       in each step of the game to reach a score at least as high as the given minimal
       score in no more than the given maximum number of moves.
       Play starts with moving all blocks up one row, adding new blocks to the bottom
       row and stabilizing the board.
       - The given blocks are collected in a list of which each element is a list of
         blocks to fill the bottom row once.
       - The function returns None if the given minimal score cannot be reached.
         Otherwise, the function returns a list of all the moves to reach at least
         the minimal score. Each move in the latter list is a tuple containing
         the lefmost position of the block to move, followed by the block itself,
         followed by the distance over which that block has to be moved.
         The position of the block is taken at the time of the move, which may obviously
         differ from the initial position taken by that block on the board.
       - If several solutions exist to reach at least the minimal score, the function
         returns the shortest of them in terms of number of moves. If several
         shortest solutions exist, the function returns the solution that is less
         than all other solutions of the same length using Python's operator to compare
         lists.
       - Upon exit, the given board and the given list of blocks must be in the same
         state they were in upon entry.
       ASSUMPTIONS
       - The given board is a proper and stable board.
       - Each element in the list of blocks ((blocks[I]) is a sequence that can be
         used to fill the bottom row once in a valid way (i.e., no overlapping
         positions, no remaining gap larger than half the number of columns after
         a complete fill, ...)
       - The elements in the list of blocks (blocks[I]) are used in the order from left
         to right.
       - Each basic element in the list of blocks ((blocks[I][J]) is a tuple
         involving a (leftmost) position in the bottom row of the board followed by
         a proper block for a board with the given dimension.
       - The given minimal score is a non-negative integer number.
       - The given maximum number of moves is an integer number. If it is negative,
         the function must return None.
       - The given level is a positive integer number.
       - The given score is a non-negative integer number.
       NOTE:
       -  This function must use the given functions let_all_full_rows_explode
          and stabilize_board each time all rows of the board must explode,
          respectively the board must be stabilized.
    """
    if max_nb_moves < 0:
        return None
    if max_nb_moves == 0 or not blocks:
        if min_score > 0:
            return None
        else:
            return []

    blocks = blocks.copy()
    cboard = Board.copy_board(board)
    if blocks:
        Board.insert_bottom_row(cboard, blocks.pop(0))
    else:
        return []
    level, score = stabilize_board(level, score, cboard)

    solutions = []

    for move in get_all_possible_moves(cboard):
        copy = Board.copy_board(cboard)
        pos = Board.get_leftmost_position_of(copy, move[0])
        Board.move_block_horizontally(copy, move[0], move[1])
        if not Board.is_empty_row(copy, 'X'):
            continue
        temp_level, temp_score = stabilize_board(level, score, copy)
        if temp_score >= min_score:
            solutions.append([(pos,) + move])
        else:
            other_moves = get_top_moves(copy, blocks.copy(), min_score, max_nb_moves-1, temp_level, temp_score)
            if other_moves is not None:
                solutions.append([(pos,) + move] + other_moves)


    if len(solutions) == 0:
        return None

    if len(solutions) > 1:
        min = max_nb_moves + 1
        for i in solutions:
            if len(i) < min:
                min = len(i)
                solutions = [i]
            elif len(i) == min and i not in solutions:
                solutions.append(i)

    if len(solutions) > 1:
        min = None
        for i in solutions:
            if not min or i < min:
                min = i
        solutions = [min]

    return solutions[0]





def let_player_move_block(board):
    """
        Let the player move one of the blocks on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The bottom row of the given board is not empty.
    """
    assert Board.is_proper_board(board)
    assert not Board.is_empty_row(board, "a")
    block_to_move = None
    distance_to_move_over = None
    while (block_to_move is None) or (distance_to_move_over is None):
        players_position = \
            input("Some position of block to move: ").split(',')
        if (len(players_position) > 1) and str.isdigit(players_position[1]):
            players_position[1] = eval(players_position[1])
        players_position = tuple(players_position)
        if not Position.is_proper_position(players_position):
            print("   ---> A proper position consists of a letter, a comma and some digits!")
        elif not Position.is_within_boundaries(Board.get_dimension(board), players_position):
            print("   ---> The position is outside the boundaries of the board!")
        elif Board.is_free_at(board, players_position):
            print("   ---> No block at the given position")
        else:
            the_block = Board.get_block_at(board, players_position)
            players_distance = int(input("Enter distance to move block over : "))
            if (not isinstance(players_distance, int)) or (players_distance == 0):
                print("   ---> The distance must be a non-zero integer number.!")
            elif not Board.can_move_over(board, the_block, players_distance):
                print("   ---> The given block cannot move over the given distance")
            else:
                block_to_move = the_block
                distance_to_move_over = players_distance
    Board.move_block_horizontally(board, block_to_move, distance_to_move_over)


def play_keyboard(blocks = [], nb_rows=10, nb_columns=8):
    """
        Function to play the game on a board with the given number of rows and the
        given number of columns via the keyboard, using the given blocks to fill
        the bottom row.
       - The given blocks are collected in a list of which each element is a list of
         blocks to fill the bottom row once. The function will first use elements from
         that list until the list is exhausted. From that point on, the function will
         generate blocks to fill the bottom row in a random way.
        ASSUMPTIONS
        - The given number of rows and the given number of columns are integer numbers
          greater than 1.
    """
    assert (nb_rows > 1) and (nb_columns > 1)
    score = 0
    level = 1
    the_board = Board.make_board((nb_rows, nb_columns))
    while Board.is_empty_row(the_board, "X"):
        if len(blocks) > 0:
            Board.insert_bottom_row(the_board,blocks.pop(0))
        else:
            Board.push_all_blocks_up(the_board)
            max_block_length = max(2, \
                               round(nb_columns / 4) if level <= 3 else \
                                   round(nb_columns / 3) if level <= 6 else
                                   round(nb_columns / 2))
            Board.fill_bottom_row(the_board, max_block_length)
        level, score = stabilize_board(level, score, the_board)
        Board.print_board(the_board)
        let_player_move_block(the_board)
        level, score = stabilize_board(level, score, the_board)
        print("Score: ", score, "[level: ", level, "]")
    print("Einde spel!")


if __name__ == '__main__':
    # You are free to change the content of blocks_to_fill
    block1_1 = Block.make_block(1, color=Color.RED)
    block1_2 = Block.make_block(3, color=Color.RED)
    block1_3 = Block.make_block(4, color=Color.RED)
    block2_1 = Block.make_block(1, color=Color.BLUE)
    block2_2 = Block.make_block(2, color=Color.BLUE)
    block2_3 = Block.make_block(4, color=Color.BLUE)
    block3_1 = Block.make_block(3, color=Color.MAGENTA)
    block3_2 = Block.make_block(1, color=Color.MAGENTA)
    block3_3 = Block.make_block(2, color=Color.MAGENTA)
    block3_4 = Block.make_block(1, color=Color.MAGENTA)
    block4_1 = Block.make_block(3, color=Color.GREEN)
    block4_2 = Block.make_block(3, color=Color.GREEN)
    block4_3 = Block.make_block(1, color=Color.GREEN)
    blocks_to_fill = \
        [[(("a", 1), block1_1), (("a", 2), block1_2)], #(("a", 5), block1_3)],
         [(("a", 1), block2_1), (("a", 3), block2_2), (("a", 5), block2_3)],
         [(("a", 1), block3_1), (("a", 5), block3_2), (("a", 6), block3_3), (("a", 8), block3_4)],
         [(("a", 1), block4_1), (("a", 5), block4_2), (("a", 8), block4_3)]
         ]
    play_keyboard(blocks_to_fill,nb_columns=9)

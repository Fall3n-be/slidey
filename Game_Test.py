import Color
import Game
import Board
import Block


# Tests for let_all_full_rows_explode

def test_Let_All_Full_Rows_Explode__Single_Case(score, max_score):
    """Function let_all_full_rows_explode: single case."""
    max_score.value += 1
    try:
        the_board = Board.make_board((5, 9))
        Board.add_block_at(the_board, Block.make_block(3), ("b", 2))
        non_exploding_block = Block.make_block(2, Block.FRAGILE)
        Board.add_block_at(the_board, non_exploding_block, ("b", 7))
        Board.add_block_at(the_board, Block.make_block(2), ("c", 1))
        Board.add_block_at(the_board, Block.make_block(3, Block.ELECTRIFIED), ("c", 3))
        Board.add_block_at(the_board, Block.make_block(4), ("c", 6))
        Board.add_block_at(the_board, Block.make_block(4), ("d", 1))
        fragile_block_to_explode = Block.make_block(3, Block.FRAGILE)
        Board.add_block_at(the_board, fragile_block_to_explode, ("d", 5))
        Board.add_block_at(the_board, Block.make_block(2), ("d", 8))
        non_exploding_block_2 = Block.make_block(3)
        Board.add_block_at(the_board, non_exploding_block_2, ("X", 3))
        score_from_explosions = Game.let_all_full_rows_explode(the_board)
        if score_from_explosions != 3 + 2 + 3 + 4 + 4 + 2 * 3 + 2:
            raise Exception
        if len(Board.get_all_blocks(the_board)) != 4:
            raise Exception
        if Board.get_all_blocks(the_board)[0] is not non_exploding_block:
            raise Exception
        if Board.get_all_blocks(the_board)[-1] is not non_exploding_block_2:
            raise Exception
        if Board.is_free_at(the_board, ("d", 5)):
            raise Exception
        if Board.is_free_at(the_board, ("d", 7)):
            raise Exception
        if Board.get_block_at(the_board, ("d", 5)) == \
                Board.get_block_at(the_board, ("d", 7)):
            raise Exception
        if Board.get_leftmost_position_of(the_board,fragile_block_to_explode) is not None:
            raise Exception
        score.value += 1
    except:
        pass


# Tests for play_greedy

def test_Play_Greedy__No_Blocks(score, max_score):
    """Function play_greedy: no blocks to fill bottom row."""
    max_score.value += 1
    try:
        total_score, moves = Game.play_greedy([])
        if total_score != 0:
            raise Exception
        if moves != []:
            raise Exception
        score.value += 1
    except:
        pass


def test_Play_Greedy__Single_Row(score, max_score):
    """Function play_greedy: blocks to fill a single row."""
    max_score.value += 2
    try:
        block1 = Block.make_block(2)
        block2 = Block.make_block(2)
        blocks_to_fill = [[(("a", 3), block1), (("a", 7), block2)]]
        # All possible moves yield the same score of 0 points. The function
        # must return the move for the first block 2 steps to the left, because
        # (1) that block is the leftmost of all blocks that can move, and
        # (2) the step brings the block to the lowest possible position.
        total_score, moves = Game.play_greedy(blocks_to_fill, (6, 8))
        if total_score != 0:
            raise Exception
        if moves != [(block1, -2)]:
            raise Exception
        score.value += 2
    except:
        pass


def test_Play_Greedy__Two_Rows_Single_Solution(score, max_score):
    """Function play_greedy: blocks to fill two rows with one best solution."""
    max_score.value += 3
    try:
        block1_1 = Block.make_block(2, color=Color.RED)
        block1_2 = Block.make_block(2, color=Color.RED)
        block1_3 = Block.make_block(1, color=Color.RED)
        block2_1 = Block.make_block(2, color=Color.BLUE)
        block2_2 = Block.make_block(3, color=Color.BLUE)
        blocks_to_fill = \
            [[(("a", 1), block1_1), (("a", 5), block1_2), (("a", 7), block1_3)],
             [(("a", 1), block2_1), (("a", 5), block2_2)]]
        # In the first step, block1_1 is moved 1 step to the right.
        # In the second step, the same block is again moved 1 step to the right.
        # This will make it fall in the bottom row, which is then completely
        # filled and yields a score of 7 points.
        total_score, moves = Game.play_greedy(blocks_to_fill, (6, 7))
        if total_score != 7:
            raise Exception
        if moves != [(block1_1, 1), (block1_1, 1)]:
            raise Exception
        if moves[0][0] is not block1_1:
            raise Exception
        score.value += 3
    except:
        pass


def test_Play_Greedy__Two_Rows_Several_Solutions(score, max_score):
    """Function play_greedy: blocks to fill two rows with several best solutions."""
    max_score.value += 5
    try:
        block1_1 = Block.make_block(1, color=Color.RED)
        block1_2 = Block.make_block(1, color=Color.RED)
        block1_3 = Block.make_block(2, color=Color.RED)
        block1_4 = Block.make_block(1, color=Color.RED)
        block2_1 = Block.make_block(2, color=Color.BLUE)
        block2_2 = Block.make_block(2, color=Color.BLUE)
        block2_3 = Block.make_block(2, color=Color.BLUE)
        blocks_to_fill = \
            [[(("a", 1), block1_1), (("a", 4), block1_2), (("a", 5), block1_3), (("a", 7), block1_4)],
             [(("a", 1), block2_1), (("a", 4), block2_2), (("a", 6), block2_3)]]
        # In the last step, moving block1_1 1 step to the right or moving block1_2
        # one step to the left both yield the same score. The function must return
        # the former move.
        total_score, moves = Game.play_greedy(blocks_to_fill, (6, 7))
        if total_score != 7:
            raise Exception
        if moves != [(block1_1, 1), (block1_1, 1)]:
            raise Exception
        score.value += 5
    except:
        pass


def test_Play_Greedy__Different_Blocks_Same_Score(score, max_score):
    """Function play_greedy: different blocks with same score."""
    max_score.value += 12
    try:
        block1_1 = Block.make_block(2, color=Color.RED)
        block1_2 = Block.make_block(2, color=Color.RED)
        block2_1 = Block.make_block(3, color=Color.BLUE)
        block2_2 = Block.make_block(2, color=Color.BLUE)
        block3_1 = Block.make_block(2, color=Color.GREEN)
        block3_2 = Block.make_block(1, color=Color.GREEN)
        block3_3 = Block.make_block(1, color=Color.GREEN)
        blocks_to_fill = [[(("a", 1), block1_1), (("a", 6), block1_2)],
                          [(("a", 2), block2_1), (("a", 6), block2_2)],
                          [(("a", 1), block3_1), (("a", 4), block3_2), (("a", 7), block3_3)]]
        # block2_1 and block2_2 can both be moved to yield a full row.
        # The function must return the move for block2_1.
        total_score, moves = Game.play_greedy(blocks_to_fill, (6, 7))
        if total_score != 7:
            raise Exception
        if moves != [(block1_1, +1), (block2_1, -1), (block2_2, -2)]:
            raise Exception
        score.value += 12
    except:
        pass


def test_Play_Greedy__Full_Row_After_Filling_Bottom_Row(score, max_score):
    """Function play_greedy: filling the bottom row yields full rows that explode."""
    max_score.value += 10
    try:
        block1_1 = Block.make_block(2, color=Color.RED)
        block1_2 = Block.make_block(2, color=Color.RED)
        block2_1 = Block.make_block(3, color=Color.BLUE)
        block2_2 = Block.make_block(2, color=Color.BLUE)
        block3_1 = Block.make_block(2, color=Color.GREEN)
        block3_2 = Block.make_block(1, color=Color.GREEN)
        block3_3 = Block.make_block(2, color=Color.GREEN)
        blocks_to_fill = [[(("a", 1), block1_1), (("a", 6), block1_2)],
                          [(("a", 2), block2_1), (("a", 6), block2_2)],
                          [(("a", 1), block3_1), (("a", 3), block3_2), (("a", 4), block3_3)]]
        # The addition of the 3rd row makes blocks fall down, yielding a full bottom
        # row. After the explosion of that row, all blocks can be cleared by moving
        # the remaining block in the 2nd row.
        total_score, moves = Game.play_greedy(blocks_to_fill, (6, 7))
        if total_score != 14:
            raise Exception
        if moves != [(block1_1, +1), (block2_1, -1), (block1_1, 2)]:
            raise Exception
        score.value += 10
    except:
        pass


def test_Play_Greedy__End_Of_Game(score, max_score):
    """Function play_greedy: end of game before all blocks have been used."""
    max_score.value += 8
    try:
        block1_1 = Block.make_block(2, color=Color.RED)
        block1_2 = Block.make_block(3, color=Color.RED)
        block2_1 = Block.make_block(3, color=Color.BLUE)
        block2_2 = Block.make_block(2, color=Color.BLUE)
        block3_1 = Block.make_block(2, color=Color.GREEN)
        block3_2 = Block.make_block(1, color=Color.GREEN)
        block3_3 = Block.make_block(1, color=Color.GREEN)
        blocks_to_fill = [[(("a", 1), block1_1), (("a", 5), block1_2)],
                          [(("a", 2), block2_1), (("a", 6), block2_2)],
                          [(("a", 1), block3_1), (("a", 4), block3_2), (("a", 7), block3_3)]]
        # block2_1 and block2_2 can both be moved to yield a full row.
        # The function must return the move for block2_1.
        total_score, moves = Game.play_greedy(blocks_to_fill, (3, 7))
        if total_score != 0:
            raise Exception
        if moves != [(block1_1, +1), (block2_1, -1), (block3_1, +1)]:
            raise Exception
        score.value += 8
    except:
        pass


def test_Play_Greedy__Large_Case(score, max_score):
    """Function play_greedy: large case."""
    max_score.value += 40
    try:
        # This test may take several minutes to come to an end.
        block1_1 = Block.make_block(2, color=Color.RED)
        block1_2 = Block.make_block(3, color=Color.RED)
        block2_1 = Block.make_block(3, color=Color.BLUE)
        block2_2 = Block.make_block(2, color=Color.BLUE)
        block3_1 = Block.make_block(2, color=Color.GREEN)
        block3_2 = Block.make_block(1, color=Color.GREEN)
        block3_3 = Block.make_block(1, color=Color.GREEN)
        block4_1 = Block.make_block(1, color=Color.CYAN)
        block4_2 = Block.make_block(3, color=Color.CYAN)
        block4_3 = Block.make_block(2, color=Color.CYAN)
        block5_1 = Block.make_block(1, color=Color.MAGENTA)
        block5_2 = Block.make_block(1, color=Color.MAGENTA)
        block5_3 = Block.make_block(1, color=Color.MAGENTA)
        block5_4 = Block.make_block(1, color=Color.MAGENTA)
        block6_1 = Block.make_block(2, Block.ELECTRIFIED, color=Color.BLACK)
        block6_2 = Block.make_block(3, color=Color.BLACK)
        block7_1 = Block.make_block(2, Block.FRAGILE, color=Color.YELLOW)
        block7_2 = Block.make_block(1, color=Color.YELLOW)
        block7_3 = Block.make_block(2, Block.ELECTRIFIED, color=Color.YELLOW)
        blocks_to_fill = [[(("a", 1), block1_1), (("a", 5), block1_2)],
                          [(("a", 2), block2_1), (("a", 6), block2_2)],
                          [(("a", 1), block3_1), (("a", 4), block3_2), (("a", 7), block3_3)],
                          [(("a", 1), block4_1), (("a", 3), block4_2), (("a", 6), block4_3)],
                          [(("a", 1), block5_1), (("a", 3), block5_2), (("a", 5), block5_3), (("a", 7), block5_4)],
                          [(("a", 2), block6_1), (("a", 4), block6_2)],
                          [(("a", 1), block7_1), (("a", 3), block7_2), (("a", 4), block7_3)],
                          ]
        total_score, moves = Game.play_greedy(blocks_to_fill, (9, 7))
        if total_score != 33:
            raise Exception
        if moves[0:6] != [(block1_1, +1), (block2_1, -1), (block3_1, +1), (block4_1, 1),
                          (block3_1, -1), (block5_3, 1), (block2_2, -3)][0:6]:
            raise Exception
        score.value += 40
    except:
        pass


# Tests for get_top_moves

def test_Get_Top_Moves__No_Blocks(score, max_score):
    """Function get_top_moves: no blocks to fill bottom row."""
    max_score.value += 3
    try:
        the_board = Board.make_board((6, 10))
        Board.add_block_at(the_board, Block.make_block(3), ("a", 2))
        best_moves = Game.get_top_moves(the_board, blocks=[], min_score=0, max_nb_moves=0)
        if best_moves != []:
            raise Exception
        best_moves = Game.get_top_moves(the_board, blocks=[], min_score=0, max_nb_moves=5)
        if best_moves != []:
            raise Exception
        best_moves = Game.get_top_moves(the_board, blocks=[], min_score=10)
        if best_moves is not None:
            raise Exception
        score.value += 3
    except:
        pass


def test_Get_Top_Moves__Single_Row_Single_Solution(score, max_score):
    """Function get_top_moves: single row, single best solution."""
    max_score.value += 12
    try:
        the_board = Board.make_board((6, 10))
        block1_1 = Block.make_block(1, color=Color.RED)
        Board.add_block_at(the_board, block1_1, ("a", 3))
        block1_2 = Block.make_block(2, color=Color.RED)
        Board.add_block_at(the_board, block1_2, ("a", 8))
        block2_1 = Block.make_block(2, color=Color.BLUE)
        block2_2 = Block.make_block(3, color=Color.BLUE)
        block2_3 = Block.make_block(2, color=Color.BLUE)
        blocks_to_fill = [[(("a", 1), block2_1), (("a", 4), block2_2), (("a", 9), block2_3)]]
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=10, max_nb_moves=1)
        if best_moves != [(("b", 8), block1_2, -1)]:
            raise Exception
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=6, max_nb_moves=3)
        if best_moves != [(("b", 8), block1_2, -1)]:
            raise Exception
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=12, max_nb_moves=2)
        if best_moves is not None:
            raise Exception
        score.value += 12
    except:
        pass


def test_Get_Top_Moves__Single_Row_Several_Solutions_Different_Blocks(score, max_score):
    """Function get_top_moves: single row, several best solutions with different blocks."""
    max_score.value += 10
    try:
        the_board = Board.make_board((6, 10))
        block1_1 = Block.make_block(1, color=Color.RED)
        Board.add_block_at(the_board, block1_1, ("a", 2))
        block1_2 = Block.make_block(1, color=Color.RED)
        Board.add_block_at(the_board, block1_2, ("a", 5))
        block1_3 = Block.make_block(2, color=Color.RED)
        Board.add_block_at(the_board, block1_3, ("a", 7))
        copy_board = Board.copy_board(the_board)
        block2_1 = Block.make_block(2, color=Color.BLUE)
        block2_2 = Block.make_block(3, color=Color.BLUE)
        block2_3 = Block.make_block(2, color=Color.BLUE)
        blocks_to_fill = [[(("a", 1), block2_1), (("a", 4), block2_2), (("a", 9), block2_3)]]
        copy_blocks_to_fill = list.copy(blocks_to_fill)
        # Both moving block1_1 one step to the right and moving block1_2 two steps to
        # the left yield the requested score. The function must return the move of
        # block1_1.
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=10, max_nb_moves=1)
        if best_moves != [(("b", 2), block1_1, 1)]:
            raise Exception
        if blocks_to_fill != copy_blocks_to_fill:
            raise Exception
        if the_board != copy_board:
            raise Exception
        score.value += 10
    except:
        pass


def test_Get_Top_Moves__Single_Row_Several_Solutions_Same_Blocks(score, max_score):
    """Function get_top_moves: single row, several best solutions with same blocks."""
    max_score.value += 14
    try:
        the_board = Board.make_board((6, 10))
        block1_1 = Block.make_block(1, color=Color.RED)
        Board.add_block_at(the_board, block1_1, ("a", 2))
        block1_2 = Block.make_block(1, color=Color.CYAN)
        Board.add_block_at(the_board, block1_2, ("a", 9))
        block2_1 = Block.make_block(2, color=Color.BLUE)
        block2_2 = Block.make_block(2, color=Color.CYAN)
        block2_3 = Block.make_block(2, color=Color.YELLOW)
        block2_4 = Block.make_block(2, color=Color.MAGENTA)
        block3_1 = Block.make_block(4, color=Color.GREEN)
        block3_2 = Block.make_block(1, color=Color.GREEN)
        block3_3 = Block.make_block(3, color=Color.GREEN)
        blocks_to_fill = \
            [[(("a", 1), block2_1), (("a", 4), block2_2), (("a", 6), block2_3), (("a", 9), block2_4)],
             [(("a", 1), block3_1), (("a", 6), block3_2), (("a", 7), block3_3)]]
        # Moving block1_1 one step to the right followed by moving block1_2 one step to
        # the left, yield the requested score. The same score is obtained from moving
        # block1_1 6 steps to the right followed by moving block1_2 6 steps to the
        # left. The function must return the first solution.
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=10, max_nb_moves=2)
        if best_moves != [(("b", 2), block1_1, 1), (("c", 9), block1_2, -1)]:
            raise Exception
        score.value += 14
    except:
        pass


def test_Get_Top_Moves__Minimal_Score_Out_Of_Reach(score, max_score):
    """Function get_top_moves: minimal score is out of reach in given number of steps."""
    max_score.value += 18
    try:
        the_board = Board.make_board((8, 10))
        block1_1 = Block.make_block(3, color=Color.MAGENTA)
        block1_2 = Block.make_block(2, color=Color.MAGENTA)
        block1_3 = Block.make_block(1, color=Color.MAGENTA)
        block1_4 = Block.make_block(1, color=Color.RED)
        block2_1 = Block.make_block(4, Block.FRAGILE, color=Color.GREEN)
        block2_2 = Block.make_block(3, color=Color.GREEN)
        block3_1 = Block.make_block(3, Block.ELECTRIFIED, color=Color.BLUE)
        block3_2 = Block.make_block(1, color=Color.BLUE)
        block3_3 = Block.make_block(2, Block.ELECTRIFIED, color=Color.BLUE)
        block3_4 = Block.make_block(1, color=Color.YELLOW)
        block4_1 = Block.make_block(2, color=Color.RED)
        block4_2 = Block.make_block(3, color=Color.RED)
        block4_3 = Block.make_block(2, color=Color.GREEN)
        blocks_to_fill = \
            [[(("a", 1), block1_1), (("a", 5), block1_2), (("a", 8), block1_3), (("a", 10), block1_4)],
             [(("a", 1), block2_1), (("a", 7), block2_2)],
             [(("a", 3), block3_1), (("a", 6), block3_2), (("a", 7), block3_3), (("a", 10), block3_4)],
             [(("a", 1), block4_1), (("a", 4), block4_2), (("a", 9), block4_3)]
             ]
        # Moving block1_1 one step to the right results in a full row after the second rwo
        # has been added. The second move cannot result in an additional score.
        # If a third move would be possible, a score of 32 would be possible.
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=15, max_nb_moves=2)
        if best_moves is not None:
            raise Exception
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=32, max_nb_moves=3)
        # if best_moves != [(("a",1), block1_1, 1),
        #                   (("a",3), Block.make_block(2, Block.FRAGILE, Color.GREEN), 2),
        #                   (("b",8), block1_3, 1)]:
        #     raise Exception
        # Check above changed because some students introduce a unique id for each block.
        if len(best_moves) != 3:
            raise Exception
        if best_moves[0] != (("a",1), block1_1, 1):
            raise Exception
        if (best_moves[1][0] != ("a",3)) or (best_moves[1][2] != 2):
            raise Exception
        if best_moves[2] != (("b",8), block1_3, 1):
            raise Exception
        score.value += 18
    except:
        pass


def test_Get_Top_Moves__End_Of_Game_Before_Reaching_Score(score, max_score):
    """Function get_top_moves: end of game before reaching minimal score."""
    max_score.value += 15
    try:
        the_board = Board.make_board((3, 10))
        block1_1 = Block.make_block(3, Block.FRAGILE, color=Color.GREEN)
        block1_2 = Block.make_block(1, color=Color.GREEN)
        block1_3 = Block.make_block(4, color=Color.GREEN)
        block2_1 = Block.make_block(3, color=Color.MAGENTA)
        block2_2 = Block.make_block(3, color=Color.MAGENTA)
        block2_3 = Block.make_block(1, color=Color.MAGENTA)
        block2_4 = Block.make_block(2, color=Color.MAGENTA)
        block3_1 = Block.make_block(3, Block.ELECTRIFIED, color=Color.BLUE)
        block3_2 = Block.make_block(2, color=Color.BLUE)
        block3_3 = Block.make_block(2, Block.ELECTRIFIED, color=Color.BLUE)
        block3_4 = Block.make_block(1, color=Color.BLUE)
        block4_1 = Block.make_block(2, color=Color.RED)
        block4_2 = Block.make_block(3, color=Color.RED)
        block4_3 = Block.make_block(2, color=Color.RED)
        blocks_to_fill = \
            [
                [(("a", 2), block1_1), (("a", 5), block1_2), (("a", 6), block1_3)],
                [(("a", 1), block2_1), (("a", 5), block2_2), (("a", 8), block2_3), (("a", 9), block2_4)],
                [(("a", 3), block3_1), (("a", 6), block3_2), (("a", 8), block3_3), (("a", 10), block3_4)],
                [(("a", 1), block4_1), (("a", 4), block4_2), (("a", 9), block4_3)]
            ]
        # Moving block2_2 one step to the left after having moved block1_1 one step to the right
        # results in a full row.
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=7, max_nb_moves=2)
        if best_moves != [(("a",2), block1_1, -1), (("b",5), block1_2, -1)]:
            raise Exception
        # If more moves are allowed, the highest possible score is 26 before reaching the end of the
        # game.
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=27, max_nb_moves=5)
        if best_moves is not None:
            raise Exception
        score.value += 15
    except:
        pass


def test_Get_Top_Moves__Several_Rows_To_Explode_In_Same_Move(score, max_score):
    """Function get_top_moves: several rows to explode to reach top score."""
    max_score.value += 30
    try:
        the_board = Board.make_board((5, 9))
        block1_1 = Block.make_block(1, color=Color.RED)
        block1_2 = Block.make_block(3, color=Color.RED)
        block1_3 = Block.make_block(4, color=Color.RED)
        block2_1 = Block.make_block(1, color=Color.BLUE)
        block2_2 = Block.make_block(2, color=Color.BLUE)
        block2_3 = Block.make_block(4, color=Color.BLUE)
        block3_1 = Block.make_block(3, color=Color.MAGENTA)
        block3_2 = Block.make_block(1, color=Color.MAGENTA)
        block3_3 = Block.make_block(2, color=Color.MAGENTA)
        block3_4 = Block.make_block(2, color=Color.MAGENTA)
        block4_1 = Block.make_block(3, color=Color.GREEN)
        block4_2 = Block.make_block(3, color=Color.GREEN)
        block4_3 = Block.make_block(2, color=Color.GREEN)
        blocks_to_fill = \
            [[(("a", 1), block1_1), (("a", 2), block1_2), (("a", 5), block1_3)],
             [(("a", 1), block2_1), (("a", 3), block2_2), (("a", 5), block2_3)],
             [(("a", 1), block3_1), (("a", 5), block3_2), (("a", 6), block3_3), (("a", 8), block3_4)],
             [(("a", 1), block4_1), (("a", 5), block4_2), (("a", 8), block4_3)]
             ]
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, min_score=36, max_nb_moves=4)
        if best_moves != \
                [(("a",5), block1_3, 1), (("a",5), block2_3, 1),
                 (("b",3), block2_2, 1), (("b",5), block3_2, -1)]:
            return
        score.value += 30
    except:
        pass


def test_Get_Top_Moves__Large_Case(score, max_score):
    """Function play_greedy: large case (same as large greedy case)."""
    max_score.value += 80
    try:
        block1_1 = Block.make_block(2, color=Color.RED)
        block1_2 = Block.make_block(1, color=Color.RED)
        block1_3 = Block.make_block(3, color=Color.RED)
        block2_1 = Block.make_block(3, color=Color.BLUE)
        block2_2 = Block.make_block(2, color=Color.BLUE)
        block3_1 = Block.make_block(2, color=Color.GREEN)
        block3_2 = Block.make_block(1, color=Color.GREEN)
        block3_3 = Block.make_block(1, color=Color.GREEN)
        block4_1 = Block.make_block(3, color=Color.CYAN)
        block4_2 = Block.make_block(1, color=Color.CYAN)
        block4_3 = Block.make_block(2, Block.FRAGILE, color=Color.CYAN)
        block5_1 = Block.make_block(1, color=Color.MAGENTA)
        block5_2 = Block.make_block(1, color=Color.MAGENTA)
        block5_3 = Block.make_block(1, color=Color.MAGENTA)
        block5_4 = Block.make_block(2, color=Color.MAGENTA)
        block6_1 = Block.make_block(2, Block.ELECTRIFIED, color=Color.BLACK)
        block6_2 = Block.make_block(3, color=Color.BLACK)
        block7_1 = Block.make_block(2, Block.FRAGILE, color=Color.YELLOW)
        block7_2 = Block.make_block(1, color=Color.YELLOW)
        block7_3 = Block.make_block(2, Block.ELECTRIFIED, color=Color.YELLOW)
        blocks_to_fill = [[(("a", 1), block1_1), (("a", 4), block1_2), (("a", 5), block1_3)],
                          [(("a", 2), block2_1), (("a", 6), block2_2)],
                          [(("a", 1), block3_1), (("a", 4), block3_2), (("a", 7), block3_3)],
                          [(("a", 1), block4_1), (("a", 5), block4_2), (("a", 6), block4_3)],
                          [(("a", 1), block5_1), (("a", 2), block5_2), (("a", 3), block5_3), (("a", 4), block5_4)],
                          [(("a", 2), block6_1), (("a", 4), block6_2)],
                          [(("a", 1), block7_1), (("a", 3), block7_2), (("a", 4), block7_3)],
                          ]
        the_board = Board.make_board((8, 7))
        # We must not use a very high score in the test, because the backtracking algorithm will
        # then take too much time.
        best_moves = Game.get_top_moves(the_board, blocks_to_fill, 45, 5)
        # if best_moves != \
        #         [(("a",4), block1_2, -1), (("a",2), block2_1, 1), (("b",5), block1_3, -1),
        #          (("a",6), block4_2, -5), (("b",1), block4_2, 5)]:
        #     return
        if len(best_moves) != 5:
            return
        if best_moves[0] != (("a", 4), block1_2, -1):
            return
        if best_moves[1] != (("a", 2), block2_1, 1):
            return
        if best_moves[2] != (("b", 5), block1_3, -1):
            return
        if best_moves[3][0] != ("a", 6) or best_moves[3][2] != -5:
            return
        if best_moves[4][0] != ("b", 1) or best_moves[4][2] != 5:
            return
        score.value += 80
    except:
        pass


# collection of game test functions

game_test_functions = \
    {
        test_Let_All_Full_Rows_Explode__Single_Case,

        test_Play_Greedy__No_Blocks,
        test_Play_Greedy__Single_Row,
        test_Play_Greedy__Two_Rows_Single_Solution,
        test_Play_Greedy__Two_Rows_Several_Solutions,
        test_Play_Greedy__Different_Blocks_Same_Score,
        test_Play_Greedy__Full_Row_After_Filling_Bottom_Row,
        test_Play_Greedy__End_Of_Game,
        test_Play_Greedy__Large_Case,

        test_Get_Top_Moves__No_Blocks,
        test_Get_Top_Moves__Single_Row_Single_Solution,
        test_Get_Top_Moves__Single_Row_Several_Solutions_Different_Blocks,
        test_Get_Top_Moves__Single_Row_Several_Solutions_Same_Blocks,
        test_Get_Top_Moves__Minimal_Score_Out_Of_Reach,
        test_Get_Top_Moves__End_Of_Game_Before_Reaching_Score,
        test_Get_Top_Moves__Several_Rows_To_Explode_In_Same_Move,
        test_Get_Top_Moves__Large_Case,
    }

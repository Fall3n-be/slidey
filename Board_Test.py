import Color
import Position
import Board
import Block

# Tests for make_board

def test_Make_Board__Single_Case(score, max_score):
    """Function make_board: single case."""
    max_score.value += 4
    try:
        the_board = Board.make_board((4,7))
        if Board.get_dimension(the_board) != (4,7):
            return
        if Board.get_all_blocks(the_board) != []:
            return
        score.value += 4
    except:
        pass


# Tests for copy_board

def test_Copy_Board__Empty_Board(score, max_score):
    """Function copy_board: empty board."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,7))
        copy_board = Board.copy_board(the_board)
        if Board.get_dimension(copy_board) != (4,7):
            return
        if Board.get_all_blocks(copy_board) != []:
            return
        score.value += 1
    except:
        pass

def test_Copy_Board__Non_Empty_Board(score, max_score):
    """Function copy_board: non empty board."""
    max_score.value += 6
    try:
        the_board = Board.make_board((4,7))
        block1 = Block.make_block(3)
        Board.add_block_at(the_board,block1,("a",2))
        block2 = Block.make_block(1,Block.ELECTRIFIED,Color.RED)
        Board.add_block_at(the_board,block2,("b",1))
        block3 = Block.make_block(2,Block.FRAGILE,Color.CYAN)
        Board.add_block_at(the_board,block3,("X",5))
        copy_board = Board.copy_board(the_board)
        if Board.get_dimension(copy_board) != (4,7):
            return
        if len(Board.get_all_blocks(copy_board)) != 3:
            return
        copy_block1 = Board.get_all_blocks(copy_board)[0]
        if Block.get_length(copy_block1) != 3:
            return
        if Block.get_type(copy_block1) != Block.ORDINARY:
            return
        if Block.get_color(copy_block1) != Block.get_color(block1):
            return
        copy_block2 = Board.get_all_blocks(copy_board)[1]
        if Block.get_length(copy_block2) != 1:
            return
        if Block.get_type(copy_block2) != Block.ELECTRIFIED:
            return
        if Block.get_color(copy_block2) != Color.RED:
            return
        copy_block3 = Board.get_all_blocks(copy_board)[2]
        if Block.get_length(copy_block3) != 2:
            return
        if Block.get_type(copy_block3) != Block.FRAGILE:
            return
        if Block.get_color(copy_block3) != Color.CYAN:
            return
        score.value += 6
    except:
        pass


# Tests for get_block_at

def test_Get_Block_At__No_Block(score, max_score):
    """Function get_block_at: no block at given position."""
    max_score.value += 2
    try:
        the_board = Board.make_board((2,5))
        if Board.get_block_at(the_board,("b",3)) is not None:
            return
        if Board.get_block_at(the_board,("e",9)) is not None:
            return
        score.value += 2
    except:
        pass


# Tests for is_free_at

def test_Is_Free_At__True_Cases(score, max_score):
    """Function is_free_at: true cases."""
    max_score.value += 1
    try:
        the_board = Board.make_board((5,7))
        if not Board.is_free_at(the_board,("b",3)):
            return
        if not Board.is_free_at(the_board,("X",2)):
            return
        score.value += 1
    except:
        pass

def test_Is_Free_At__False_Cases(score, max_score):
    """Function is_free_at: false cases."""
    max_score.value += 1
    try:
        the_board = Board.make_board((5,7))
        Board.add_block_at(the_board,Block.make_block(2),("a",3))
        if Board.is_free_at(the_board,("a",3)):
            return
        if Board.is_free_at(the_board,("a",4)):
            return
        if Board.is_free_at(the_board,("m",20)):
            return
        score.value += 1
    except:
        pass


# Tests for get_leftmost_position

def test_Get_Leftmost_Position__Block_Not_On_Board(score, max_score):
    """Function get_leftmost_position: block not on board."""
    max_score.value += 1
    try:
        the_board = Board.make_board((5,7))
        the_block = Block.make_block(3)
        if Board.get_leftmost_position_of(the_board,the_block) is not None:
            return
        score.value += 1
    except:
        pass

def test_Get_Leftmost_Position__Block_On_Board(score, max_score):
    """Function get_leftmost_position: block on board."""
    max_score.value += 1
    try:
        the_board = Board.make_board((5,7))
        the_block = Block.make_block(3)
        Board.add_block_at(the_board,the_block,("b",2))
        if Board.get_leftmost_position_of(the_board,the_block) != ("b",2):
            return
        score.value += 1
    except:
        pass

def test_Get_Leftmost_Position__Block_At_Edges(score, max_score):
    """Function get_leftmost_position: block at edges."""
    max_score.value += 2
    try:
        the_board = Board.make_board((5,7))
        the_block = Block.make_block(1)
        Board.add_block_at(the_board,the_block,("a",1))
        if Board.get_leftmost_position_of(the_board,the_block) != ("a",1):
            return
        the_block = Block.make_block(1)
        Board.add_block_at(the_board,the_block,("X",7))
        if Board.get_leftmost_position_of(the_board,the_block) != ("X",7):
            return
        score.value += 2
    except:
        pass

def test_Get_Leftmost_Position__Identical_Blocks_On_Board(score, max_score):
    """Function get_leftmost_position: identical blocks on board."""
    max_score.value += 4
    try:
        the_board = Board.make_board((5,7))
        block1 = Block.make_block(3)
        Board.add_block_at(the_board,block1,("b",2))
        block2 = Block.make_block(3)
        Board.add_block_at(the_board,block2,("c",4))
        block3 = Block.make_block(3)
        Board.add_block_at(the_board,block3,("X",1))
        if Board.get_leftmost_position_of(the_board,block1) != ("b",2):
            return
        if Board.get_leftmost_position_of(the_board,block2) != ("c",4):
            return
        if Board.get_leftmost_position_of(the_board,block3) != ("X",1):
            return
        score.value += 4
    except:
        pass


# Tests for get_all_positions_of

def test_Get_All_Positions_Of__Single_Case(score, max_score):
    """Function get_all_positions_of: single case."""
    max_score.value += 3
    try:
        the_board = Board.make_board((5,7))
        the_block = Block.make_block(3)
        Board.add_block_at(the_board,the_block,("b",2))
        if Board.get_all_positions_of(the_board,the_block) != \
               (("b",2), ("b",3), ("b",4)):
            return
        score.value += 3
    except:
        pass


# Tests for get_random_position_for

def test_Get_Random_Position_For__Positions_Possible(score, max_score):
    """Function get_random_position_for: at least one position is possible."""
    max_score.value += 8
    try:
        the_board = Board.make_board((4,7))
        the_block = Block.make_block(3)
        Board.add_block_at(the_board,the_block,("b",2))
        block_to_place = Block.make_block(2)
        random_position = Board.get_random_position_for(the_board,block_to_place,"b")
        if Position.get_row(random_position) != "b":
            return
        if (Position.get_column(random_position) != 5) and\
               (Position.get_column(random_position) != 6):
            return
        block_to_place = Block.make_block(3)
        random_position = Board.get_random_position_for(the_board,block_to_place)
        if Position.get_row(random_position) != "a":
            return
        if not Board.can_accept_block_at(the_board,block_to_place,random_position):
            return
        score.value += 8
    except:
        pass

def test_Get_Random_Position_For__No_Position_Possible(score, max_score):
    """Function get_random_position_for: no position possible."""
    max_score.value += 10
    try:
        the_board = Board.make_board((4,7))
        Board.add_block_at(the_board,Block.make_block(3),("b",1))
        Board.add_block_at(the_board,Block.make_block(2),("b",5))
        if Board.get_random_position_for(the_board, Block.make_block(2), "b") is not None:
            return
        Board.add_block_at(the_board,Block.make_block(3),("X",1))
        if not Board.is_proper_board(the_board):
            return
        Board.add_block_at(the_board,Block.make_block(1),("X",4))
        if not Board.is_proper_board(the_board):
            return
        Board.add_block_at(the_board,Block.make_block(3),("X",5))
        if Board.get_random_position_for(the_board, Block.make_block(1), "X") is not None:
            return
        score.value += 10
    except:
        pass


# Tests for get_all_blocks_in_row

def test_Get_All_Blocks_In_Row__Empty_Row(score, max_score):
    """Function get_all_blocks_in_row: empty row."""
    max_score.value += 2
    try:
        the_board = Board.make_board((4,10))
        if Board.get_all_blocks_in_row(the_board,"b") != []:
            return
        score.value += 2
    except:
        pass

def test_Get_All_Blocks_In_Row__Partially_Filled_Row(score, max_score):
    """Function get_all_blocks_in_row: partially filled row."""
    max_score.value += 8
    try:
        the_board = Board.make_board((4,10))
        block1 = Block.make_block(4)
        Board.add_block_at(the_board,block1,("b",3))
        if Board.get_all_blocks_in_row(the_board,"b") != [block1]:
            return
        block2 = Block.make_block(2)
        Board.add_block_at(the_board,block2,("b",1))
        if Board.get_all_blocks_in_row(the_board,"b") != [block2,block1]:
            return
        block3 = Block.make_block(1)
        Board.add_block_at(the_board,block3,("b",10))
        if Board.get_all_blocks_in_row(the_board,"b") != [block2,block1,block3]:
            return
        score.value += 8
    except:
        pass

def test_Get_All_Blocks_In_Row__Full_Row(score, max_score):
    """Function get_all_blocks_in_row: full row."""
    max_score.value += 4
    try:
        the_board = Board.make_board((4,10))
        block1 = Block.make_block(4)
        Board.add_block_at(the_board,block1,("X",3))
        block2 = Block.make_block(2)
        Board.add_block_at(the_board,block2,("X",1))
        block3 = Block.make_block(3)
        Board.add_block_at(the_board,block3,("X",8))
        block4 = Block.make_block(1)
        Board.add_block_at(the_board,block4,("X",7))
        if Board.get_all_blocks_in_row(the_board,"X") !=\
               [block2,block1,block4,block3]:
            return
        score.value += 4
    except:
        pass


# Tests for get_length_largest_gap_in_row

def test_Get_Length_Largest_Gap_In_Row__Empty_Row(score, max_score):
    """Function get_length_largest_gap_in_row: empty row."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        if Board.get_length_largest_gap_in_row(the_board,"b") != 10:
            return
        score.value += 1
    except:
        pass

def test_Get_Length_Largest_Gap_In_Row__Full_Row(score, max_score):
    """Function get_length_largest_gap_in_row: full row."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        Board.add_block_at(the_board,Block.make_block(5),("b",1))
        Board.add_block_at(the_board,Block.make_block(5),("b",6))
        if Board.get_length_largest_gap_in_row(the_board,"b") != 0:
            return
        score.value += 1
    except:
        pass

def test_Get_Length_Largest_Gap_In_Row__Gap_In_Middle(score, max_score):
    """Function get_length_largest_gap_in_row: largest gap in middle."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        Board.add_block_at(the_board,Block.make_block(2),("b",1))
        Board.add_block_at(the_board,Block.make_block(3),("b",6))
        if Board.get_length_largest_gap_in_row(the_board,"b") != 3:
            return
        score.value += 1
    except:
        pass

def test_Get_Length_Largest_Gap_In_Row__Gap_Beginning(score, max_score):
    """Function get_length_largest_gap_in_row: largest gap in in the beginning."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        Board.add_block_at(the_board,Block.make_block(2),("b",4))
        Board.add_block_at(the_board,Block.make_block(3),("b",8))
        if Board.get_length_largest_gap_in_row(the_board,"b") != 3:
            return
        score.value += 1
    except:
        pass

def test_Get_Length_Largest_Gap_In_Row__Gap_At_End(score, max_score):
    """Function get_length_largest_gap_in_row: largest gap at the end."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        Board.add_block_at(the_board,Block.make_block(2),("b",2))
        Board.add_block_at(the_board,Block.make_block(3),("b",4))
        if Board.get_length_largest_gap_in_row(the_board,"b") != 4:
            return
        score.value += 1
    except:
        pass


# Tests for is_empty_row

def test_Is_Empty_Row__Single_Test(score, max_score):
    """Function is_empty_row: single test."""
    max_score.value += 3
    try:
        the_board = Board.make_board((4,10))
        if not Board.is_empty_row(the_board,"b"):
            return
        if not Board.is_empty_row(the_board,"X"):
            return
        Board.add_block_at(the_board,Block.make_block(5),("a",3))
        if Board.is_empty_row(the_board,"a"):
            return
        Board.add_block_at(the_board,Block.make_block(1),("b",1))
        if Board.is_empty_row(the_board,"b"):
            return
        Board.add_block_at(the_board,Block.make_block(1),("X",10))
        if Board.is_empty_row(the_board,"X"):
            return
        score.value += 3
    except:
        pass


# Tests for is_full_row

def test_Is_Full_Row__True_Cases(score, max_score):
    """Function is_full_row: true cases."""
    max_score.value += 4
    try:
        the_board = Board.make_board((4,10))
        Board.add_block_at(the_board,Block.make_block(5),("b",1))
        Board.add_block_at(the_board,Block.make_block(5),("b",6))
        if not Board.is_full_row(the_board,"b"):
            return
        the_board = Board.make_board((4,2))
        Board.add_block_at(the_board,Block.make_block(1),("X",1))
        Board.add_block_at(the_board,Block.make_block(1),("X",2))
        if not Board.is_full_row(the_board,"X"):
            return
        score.value += 4
    except:
        pass

def test_Is_Full_Row__False_Cases(score, max_score):
    """Function is_full_row: false cases."""
    max_score.value += 4
    try:
        the_board = Board.make_board((4,10))
        # Empty row
        if Board.is_full_row(the_board,"b"):
            return
        # Row with block in the middle
        Board.add_block_at(the_board,Block.make_block(3),("X",1))
        if Board.is_full_row(the_board,"X"):
            return
        # Row with last cell empty
        Board.add_block_at(the_board,Block.make_block(5),("a",1))
        Board.add_block_at(the_board,Block.make_block(4),("a",6))
        if Board.is_full_row(the_board,"a"):
            return
        # Row with first cell empty
        Board.add_block_at(the_board,Block.make_block(4),("c",2))
        Board.add_block_at(the_board,Block.make_block(5),("c",6))
        if Board.is_full_row(the_board,"c"):
            return
        score.value += 4
    except:
        pass


# Tests for get_all_full_rows

def test_Get_All_Full_Rows__No_Full_Rows(score, max_score):
    """Function get_all_full_rows: no full rows."""
    max_score.value += 3
    try:
        the_board = Board.make_board((4,10))
        if Board.get_all_full_rows(the_board) != frozenset():
            return
        Board.add_block_at(the_board,Block.make_block(5),("b",1))
        Board.add_block_at(the_board,Block.make_block(3),("X",6))
        if Board.get_all_full_rows(the_board) != frozenset():
            return
        score.value += 3
    except:
        pass

def test_Get_All_Full_Rows__Some_Full_Rows(score, max_score):
    """Function get_all_full_rows: some full rows."""
    max_score.value += 3
    try:
        the_board = Board.make_board((4,10))
        Board.add_block_at(the_board,Block.make_block(5),("b",1))
        Board.add_block_at(the_board,Block.make_block(5),("b",6))
        Board.add_block_at(the_board,Block.make_block(3),("X",1))
        Board.add_block_at(the_board,Block.make_block(3),("X",4))
        Board.add_block_at(the_board,Block.make_block(4),("X",7))
        if Board.get_all_full_rows(the_board) != frozenset({"b","X"}):
            return
        score.value += 3
    except:
        pass

def test_Get_All_Full_Rows__All_Full_Rows(score, max_score):
    """Function get_all_full_rows: all full rows."""
    max_score.value += 3
    try:
        the_board = Board.make_board((2,5))
        Board.add_block_at(the_board,Block.make_block(2),("a",1))
        Board.add_block_at(the_board,Block.make_block(1),("a",3))
        Board.add_block_at(the_board,Block.make_block(2),("a",4))
        Board.add_block_at(the_board,Block.make_block(2),("X",1))
        Board.add_block_at(the_board,Block.make_block(2),("X",3))
        Board.add_block_at(the_board,Block.make_block(1),("X",5))
        if Board.get_all_full_rows(the_board) != frozenset({"a","X"}):
            return
        score.value += 3
    except:
        pass


# Tests for get_all_blocks

def test_Get_All_Blocks__Empty_Board(score, max_score):
    """Function get_all_blocks: empty board."""
    max_score.value += 2
    try:
        the_board = Board.make_board((4,10))
        if Board.get_all_blocks(the_board) != []:
            return
        score.value += 2
    except:
        pass

def test_Get_All_Blocks__Partially_Filled_Board(score, max_score):
    """Function get_all_blocks: partially filled board."""
    max_score.value += 8
    try:
        the_board = Board.make_board((6,10))
        block1 = Block.make_block(4)
        Board.add_block_at(the_board,block1,("b",3))
        if Board.get_all_blocks(the_board) != [block1]:
            return
        block2 = Block.make_block(2)
        Board.add_block_at(the_board,block2,("a",1))
        if Board.get_all_blocks(the_board) != [block2,block1]:
            return
        block3 = Block.make_block(1)
        Board.add_block_at(the_board,block3,("a",8))
        if Board.get_all_blocks(the_board) != [block2,block3,block1]:
            return
        block4 = Block.make_block(3)
        Board.add_block_at(the_board,block4,("d",8))
        if Board.get_all_blocks(the_board) != [block2,block3,block1,block4]:
            return
        block5 = Block.make_block(4)
        Board.add_block_at(the_board,block5,("X",2))
        if Board.get_all_blocks(the_board) != [block2,block3,block1,block4,block5]:
            return
        score.value += 8
    except:
        pass

def test_Get_All_Blocks__Full_Board(score, max_score):
    """Function get_all_blocks: full board."""
    max_score.value += 4
    try:
        the_board = Board.make_board((3,4))
        blockX3 = Block.make_block(2)
        Board.add_block_at(the_board,blockX3,("X",3))
        blockX1 = Block.make_block(2)
        Board.add_block_at(the_board,blockX1,("X",1))
        blockb4 = Block.make_block(1)
        Board.add_block_at(the_board,blockb4,("b",4))
        blockb3 = Block.make_block(1)
        Board.add_block_at(the_board,blockb3,("b",3))
        blockb2 = Block.make_block(1)
        Board.add_block_at(the_board,blockb2,("b",2))
        blockb1 = Block.make_block(1)
        Board.add_block_at(the_board,blockb1,("b",1))
        blocka3 = Block.make_block(2)
        Board.add_block_at(the_board,blocka3,("a",3))
        blocka1 = Block.make_block(2)
        Board.add_block_at(the_board,blocka1,("a",1))
        if Board.get_all_blocks(the_board) !=\
               [blocka1,blocka3,blockb1,blockb2,blockb3,blockb4,blockX1,blockX3]:
            return
        score.value += 4
    except:
        pass


# Tests for contains_block

def test_Contains_Block__True_Cases(score, max_score):
    """Function contains_block: true cases."""
    max_score.value += 2
    try:
        the_board = Board.make_board((4,10))
        block1 = Block.make_block(4)
        Board.add_block_at(the_board,block1,("b",3))
        block2 = Block.make_block(2)
        Board.add_block_at(the_board,block2,("a",1))
        block3 = Block.make_block(1)
        Board.add_block_at(the_board,block3,("X",8))
        if not Board.contains_block(the_board,block1):
            return
        if not Board.contains_block(the_board,block2):
            return
        if not Board.contains_block(the_board,block3):
            return
        score.value += 2
    except:
        pass

def test_Contains_Block__False_Cases(score, max_score):
    """Function contains_block: false cases."""
    max_score.value += 12
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4,Block.ORDINARY,Color.CYAN)
        if Board.contains_block(the_board,the_block):
            return
        block2 = Block.make_block(2)
        Board.add_block_at(the_board,block2,("a",1))
        if Board.contains_block(the_board,the_block):
            return
        identical_block = Block.make_block(4,Block.ORDINARY,Color.CYAN)
        Board.add_block_at(the_board,identical_block,("X",5))
        if Board.contains_block(the_board,the_block):
            return
        score.value += 12
    except:
        pass


# Tests for can_accept_block_at

def test_Can_Accept_Block_At__True_Cases(score, max_score):
    """Function can_accept_block_at: acceptable block in the middle of a row."""
    max_score.value += 8
    try:
        the_board = Board.make_board((4,7))
        the_block = Block.make_block(3)
        if not Board.can_accept_block_at(the_board,the_block,("b",2)):
            return
        if not Board.can_accept_block_at(the_board,the_block,("X",1)):
            return
        if not Board.can_accept_block_at(the_board,the_block,("a",5)):
            return
        score.value += 8
    except:
        pass

def test_Can_Accept_Block_At__Adjacent_To_Occupied_Positions(score, max_score):
    """Function can_accept_block_at: adjacent to occupied positions."""
    max_score.value += 6
    try:
        the_board = Board.make_board((7,12))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("d",3))
        the_block = Block.make_block(2)
        if not Board.can_accept_block_at(the_board,the_block,("d",1)):
            return
        if not Board.can_accept_block_at(the_board,the_block,("d",7)):
            return
        score.value += 6
    except:
        pass

def test_Can_Accept_Block_At__Identical_Block_On_Board(score, max_score):
    """Function can_accept_block_at: identical block on board."""
    max_score.value += 6
    try:
        the_board = Board.make_board((7,12))
        Board.add_block_at(the_board,Block.make_block(4),("d",3))
        Board.add_block_at(the_board,Block.make_block(4),("a",1))
        the_block = Block.make_block(4)
        if not Board.can_accept_block_at(the_board,the_block,("a",5)):
            return
        if not Board.can_accept_block_at(the_board,the_block,("X",2)):
            return
        score.value += 6
    except:
        pass

def test_Can_Accept_Block_At__Block_Too_Long(score, max_score):
    """Function can_accept_block_at: block is too long for the given board."""
    max_score.value += 2
    try:
        the_board = Board.make_board((4,7))
        the_block = Block.make_block(4)
        if Board.can_accept_block_at(the_board,the_block,("b",2)):
            return
        score.value += 2
    except:
        pass

def test_Can_Accept_Block_At__Block_Does_Not_Fully_Fit(score, max_score):
    """Function can_accept_block_at: given block does not fully fit."""
    max_score.value += 2
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4)
        if Board.can_accept_block_at(the_board,the_block,("b",8)):
            return
        if Board.can_accept_block_at(the_board,the_block,("b",9)):
            return
        if Board.can_accept_block_at(the_board,the_block,("b",10)):
            return
        score.value += 2
    except:
        pass

def test_Can_Accept_Block_At__Given_Position_Out_Of_Bounds(score, max_score):
    """Function can_accept_block_at: given position outside boundaries of board."""
    max_score.value += 2
    try:
        the_board = Board.make_board((4,7))
        the_block = Block.make_block(2)
        if Board.can_accept_block_at(the_board,the_block,("b",8)):
            return
        if Board.can_accept_block_at(the_board,the_block,("d",2)):
            return
        score.value += 2
    except:
        pass

def test_Can_Accept_Block_At__Area_Not_Free(score, max_score):
    """Function can_accept_block_at: some cells are not free."""
    max_score.value += 2
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("b",3))
        the_block = Block.make_block(3)
        if Board.can_accept_block_at(the_board,the_block,("b",4)):
            return
        if Board.can_accept_block_at(the_board,the_block,("b",1)):
            return
        if Board.can_accept_block_at(the_board,the_block,("b",6)):
            return
        score.value += 2
    except:
        pass

def test_Can_Accept_Block_At__Block_Already_on_Board(score, max_score):
    """Function can_accept_block_at: block already on board."""
    max_score.value += 5
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4,Block.ORDINARY)
        Board.add_block_at(the_board,the_block,("b",2))
        if Board.can_accept_block_at(the_board,the_block,("a",1)):
            return
        if Board.can_accept_block_at(the_board,the_block,("X",4)):
            return
        score.value += 5
    except:
        pass


# Tests for add_block

def test_Add_Block_At__Simple_Case(score, max_score):
    """Function add_block_at: simple case."""
    max_score.value += 6
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("b",3))
        if not Board.is_free_at(the_board,("b",2)):
            return
        for col in range(3,7):
            if Board.get_block_at(the_board,("b",col)) is not the_block:
                return
        if not Board.is_free_at(the_board,("b",7)):
            return
        the_block = Block.make_block(3)
        Board.add_block_at(the_board,the_block,("X",1))
        for col in range(1,4):
            if Board.get_block_at(the_board,("X",col)) is not the_block:
                return
        if not Board.is_free_at(the_board,("X",4)):
            return
        score.value += 6
    except:
        pass

def test_Add_Block_At__Identical_Block_On_Board(score, max_score):
    """Function add_block_at: identical block on board."""
    max_score.value += 6
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("b",3))
        identical_block = Block.make_block(4)
        Board.add_block_at(the_board,identical_block,("c",7))
        for col in range(7,11):
            if Board.get_block_at(the_board,("c",col)) is not identical_block:
                return
        if not Board.is_free_at(the_board,("c",6)):
            return
        score.value += 6
    except:
        pass


# Tests for remove_block_from

def test_Remove_Block_From__Block_On_Board(score, max_score):
    """Function remove_block_from: block on board."""
    max_score.value += 4
    try:
        the_board = Board.make_board((4,10))
        block_to_remove = Block.make_block(4)
        Board.add_block_at(the_board,block_to_remove,("b",3))
        block1 = Block.make_block(3)
        Board.add_block_at(the_board,block1,("X",1))
        block2 = Block.make_block(1)
        Board.add_block_at(the_board,block2,("a",1))
        Board.remove_block_from(the_board,block_to_remove)
        for col in range(3,7):
            if not Board.is_free_at(the_board,("b",col)):
                return
        if Board.get_all_blocks(the_board) != [block2,block1]:
            return
        score.value += 4
    except:
        pass

def test_Remove_Block_From__Block_Not_On_Board(score, max_score):
    """Function remove_block_from: block not on board."""
    max_score.value += 3
    try:
        the_board = Board.make_board((4, 10))
        block1 = Block.make_block(4)
        Board.add_block_at(the_board, block1, ("X", 1))
        block2 = Block.make_block(4)
        Board.add_block_at(the_board, block2, ("a", 1))
        block_to_remove = Block.make_block(3)
        Board.remove_block_from(the_board, block_to_remove)
        if Board.get_all_blocks(the_board) != [block2, block1]:
            return
        score.value += 3
    except:
        pass

def test_Remove_Block_From__Identical_Block_On_Board(score, max_score):
    """Function remove_block_from: identical block on board."""
    max_score.value += 10
    try:
        the_board = Board.make_board((4, 10))
        block_to_remove = Block.make_block(3)
        block1 = Block.make_block(3)
        Board.add_block_at(the_board, block1, ("X", 1))
        block2 = Block.make_block(1)
        Board.add_block_at(the_board, block2, ("a", 1))
        Board.remove_block_from(the_board, block_to_remove)
        if Board.get_all_blocks(the_board) != [block2, block1]:
            return
        score.value += 10
    except:
        pass


# Tests for is_airborne

def test_Is_Airborne__Bottom_Row(score, max_score):
    """Function is_airborne: bottom row."""
    max_score.value += 3
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("a",1))
        if Board.is_airborne(the_board,the_block):
            return
        score.value += 3
    except:
        pass

def test_Is_Airborne__True_Case(score, max_score):
    """Function is_airborne: true case."""
    max_score.value += 6
    try:
        the_board = Board.make_board((4,12))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("b",3))
        if not Board.is_airborne(the_board,the_block):
            return
        Board.add_block_at(the_board,Block.make_block(2),("a",1))
        Board.add_block_at(the_board,Block.make_block(3),("a",9))
        if not Board.is_airborne(the_board,the_block):
            return
        score.value += 6
    except:
        pass

def test_Is_Airborne__Support_For_Some_Cells(score, max_score):
    """Function is_airborne: support for some cells."""
    max_score.value += 3
    try:
        the_board = Board.make_board((6,10))
        Board.add_block_at(the_board,Block.make_block(1),("b",4))
        Board.add_block_at(the_board,Block.make_block(3),("b",6))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("c",3))
        if Board.is_airborne(the_board,the_block):
            return
        score.value += 3
    except:
        pass

def test_Is_Airborne__Support_For_Leftmost_Cell(score, max_score):
    """Function is_airborne: support for leftmost cell."""
    max_score.value += 3
    try:
        the_board = Board.make_board((6,10))
        Board.add_block_at(the_board,Block.make_block(2),("b",2))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("c",3))
        if Board.is_airborne(the_board,the_block):
            return
        score.value += 3
    except:
        pass

def test_Is_Airborne__Support_For_Rightmost_Cell(score, max_score):
    """Function is_airborne: support for rightmost cell."""
    max_score.value += 3
    try:
        the_board = Board.make_board((6,10))
        Board.add_block_at(the_board,Block.make_block(2),("b",7))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("c",3))
        if Board.is_airborne(the_board,the_block):
            return
        score.value += 3
    except:
        pass


# Tests for get_adjacent_blocks_above

def test_Get_Adjacent_Blocks_Above__No_Blocks(score, max_score):
    """Function get_adjacent_blocks_above: no blocks."""
    max_score.value += 2
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(2)
        Board.add_block_at(the_board,the_block,("X",1))
        if len(Board.get_adjacent_blocks_above(the_board,the_block)) != 0:
            return
        Board.add_block_at(the_board,Block.make_block(1),("X",8))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("c",3))
        if len(Board.get_adjacent_blocks_above(the_board,the_block)) != 0:
            return
        score.value += 2
    except:
        pass

def test_Get_Adjacent_Blocks_Above__Some_Blocks(score, max_score):
    """Function get_adjacent_blocks_above: some blocks."""
    max_score.value += 6
    try:
        the_board = Board.make_board((4,10))
        adjacent_block_1 = Block.make_block(3)
        Board.add_block_at(the_board,adjacent_block_1,("X",1))
        adjacent_block_2 = Block.make_block(1)
        Board.add_block_at(the_board,adjacent_block_2,("X",5))
        adjacent_block_3 = Block.make_block(1)
        Board.add_block_at(the_board, adjacent_block_3, ("X", 7))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,Block.make_block(1),("X",9))
        Board.add_block_at(the_board,Block.make_block(2),("c",1))
        Board.add_block_at(the_board,Block.make_block(2),("c",8))
        Board.add_block_at(the_board,Block.make_block(4),("b",5))
        Board.add_block_at(the_board,the_block,("c",3))
        if Board.get_adjacent_blocks_above(the_board,the_block) != \
            [adjacent_block_1,adjacent_block_2,adjacent_block_3]:
            return
        score.value += 6
    except:
        pass

def test_Get_Adjacent_Blocks_Above__Block_At_Edges(score, max_score):
    """Function get_adjacent_blocks_above: given block at edges."""
    max_score.value += 4
    try:
        the_board = Board.make_board((4,10))
        non_adjacent_block = Block.make_block(3)
        Board.add_block_at(the_board,non_adjacent_block,("X",3))
        adjacent_block = Block.make_block(1)
        Board.add_block_at(the_board,adjacent_block,("X",10))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("c",6))
        if Board.get_adjacent_blocks_above(the_board,the_block) != \
            [adjacent_block]:
            return
        the_board = Board.make_board((4,10))
        non_adjacent_block = Block.make_block(3)
        Board.add_block_at(the_board,non_adjacent_block,("b",4))
        adjacent_block = Block.make_block(2)
        Board.add_block_at(the_board,adjacent_block,("b",1))
        the_block = Block.make_block(3)
        Board.add_block_at(the_board,the_block,("a",1))
        if Board.get_adjacent_blocks_above(the_board,the_block) != \
            [adjacent_block]:
            return
        score.value += 4
    except:
        pass


# Tests for get_adjacent_block_left

def test_Get_Adjacent_Block_Left__No_Block(score, max_score):
    """Function get_adjacent_block_left: no block."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(2)
        Board.add_block_at(the_board,the_block,("X",1))
        if Board.get_adjacent_block_left(the_board,the_block) is not None:
            return
        Board.add_block_at(the_board,Block.make_block(1),("X",6))
        the_block = Block.make_block(1)
        Board.add_block_at(the_board,the_block,("X",8))
        if Board.get_adjacent_block_left(the_board,the_block) is not None:
            return
        score.value += 1
    except:
        pass

def test_Get_Adjacent_Block_Left__Effective_Block(score, max_score):
    """Function get_adjacent_block_left: effective block to the left."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(2)
        Board.add_block_at(the_board,the_block,("X",3))
        adjacent_block = Block.make_block(1)
        Board.add_block_at(the_board,adjacent_block,("X",2))
        if Board.get_adjacent_block_left(the_board,the_block) != adjacent_block:
            return
        score.value += 1
    except:
        pass


# Tests for get_adjacent_blocks_below

def test_Get_Adjacent_Blocks_Below__No_Blocks(score, max_score):
    """Function get_adjacent_blocks_below: no blocks."""
    max_score.value += 2
    #try:
    the_board = Board.make_board((5,10))
    the_block = Block.make_block(2)
    Board.add_block_at(the_board,the_block,("a",1))
    if len(Board.get_adjacent_blocks_below(the_board,the_block)) != 0:
        return
    Board.add_block_at(the_board,Block.make_block(1),("c",2))
    Board.add_block_at(the_board,Block.make_block(1),("c",8))
    Board.add_block_at(the_board,Block.make_block(4),("d",4))
    the_block = Block.make_block(5)
    Board.add_block_at(the_board,the_block,("c",3))
    if len(Board.get_adjacent_blocks_below(the_board,the_block)) != 0:
        return
    score.value += 2
    #except:
    #    pass

def test_Get_Adjacent_Blocks_Below__Some_Blocks(score, max_score):
    """Function get_adjacent_blocks_below: some blocks."""
    max_score.value += 6
   # try:
    the_board = Board.make_board((4,10))
    adjacent_block_1 = Block.make_block(3)
    Board.add_block_at(the_board,adjacent_block_1,("a",1))
    adjacent_block_2 = Block.make_block(1)
    Board.add_block_at(the_board,adjacent_block_2,("a",5))
    adjacent_block_3 = Block.make_block(1)
    Board.add_block_at(the_board, adjacent_block_3, ("a", 7))
    the_block = Block.make_block(5)
    Board.add_block_at(the_board,Block.make_block(1),("b",2))
    Board.add_block_at(the_board,Block.make_block(2),("b",9))
    Board.add_block_at(the_board,Block.make_block(2),("c",4))
    Board.add_block_at(the_board,the_block,("b",3))
    if Board.get_adjacent_blocks_below(the_board,the_block) != \
        [adjacent_block_1,adjacent_block_2,adjacent_block_3]:
        return
    score.value += 6
   # except:
   #     pass

def test_Get_Adjacent_Blocks_Below__Block_At_Edges(score, max_score):
    """Function get_adjacent_blocks_below: given block at edges."""
    max_score.value += 4
    #try:
    the_board = Board.make_board((4,10))
    non_adjacent_block = Block.make_block(3)
    Board.add_block_at(the_board,non_adjacent_block,("b",3))
    adjacent_block = Block.make_block(1)
    Board.add_block_at(the_board,adjacent_block,("b",10))
    the_block = Block.make_block(5)
    Board.add_block_at(the_board,the_block,("c",6))
    if Board.get_adjacent_blocks_below(the_board,the_block) != \
        [adjacent_block]:
        return
    the_board = Board.make_board((4,10))
    non_adjacent_block = Block.make_block(3)
    Board.add_block_at(the_board,non_adjacent_block,("a",4))
    adjacent_block = Block.make_block(2)
    Board.add_block_at(the_board,adjacent_block,("a",1))
    the_block = Block.make_block(3)
    Board.add_block_at(the_board,the_block,("b",1))
    if Board.get_adjacent_blocks_below(the_board,the_block) != \
        [adjacent_block]:
        return
    score.value += 4
    #except:
    #    pass


# Tests for get_adjacent_block_right

def test_Get_Adjacent_Block_Right__No_Block(score, max_score):
    """Function get_adjacent_block_right: no block."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("X",7))
        if Board.get_adjacent_block_right(the_board,the_block) is not None:
            return
        Board.add_block_at(the_board,Block.make_block(1),("X",4))
        the_block = Block.make_block(1)
        Board.add_block_at(the_board,the_block,("X",2))
        if Board.get_adjacent_block_right(the_board,the_block) is not None:
            return
        score.value += 1
    except:
        pass

def test_Get_Adjacent_Block_Right__Effective_Block(score, max_score):
    """Function get_adjacent_block_right: effective block to the right."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(2)
        Board.add_block_at(the_board,the_block,("X",3))
        adjacent_block = Block.make_block(1)
        Board.add_block_at(the_board,adjacent_block,("X",5))
        if Board.get_adjacent_block_right(the_board,the_block) != adjacent_block:
            return
        score.value += 1
    except:
        pass


# Tests for get_supporting_blocks

def test_Get_Supporting_Blocks__No_Blocks(score, max_score):
    """Function get_supporting_blocks: no blocks."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("c",3))
        if len(Board.get_supporting_blocks(the_board,the_block)) != 0:
            return
        score.value += 1
    except:
        pass

def test_Get_Supporting_Blocks__Only_Direct_Blocks(score, max_score):
    """Function get_supporting_blocks: only directly supporting blocks."""
    max_score.value += 4
    try:
        the_board = Board.make_board((6,14))
        the_block = Block.make_block(7)
        Board.add_block_at(the_board,the_block,("c",3))
        Board.add_block_at(the_board,Block.make_block(2),("b",3))
        Board.add_block_at(the_board,Block.make_block(3),("b",6))
        Board.add_block_at(the_board,Block.make_block(1),("b",9))
        if Board.get_supporting_blocks(the_board,the_block) != \
                frozenset({ ("b",3),("b",6),("b",9) }):
            return
        score.value += 4
    except:
        pass

def test_Get_Supporting_Blocks__Direct_And_Indirect_Blocks(score, max_score):
    """Function get_supporting_blocks: both directly and indirectly supported blocks."""
    max_score.value += 12
    try:
        the_board = Board.make_board((6,14))
        the_block = Block.make_block(7)
        Board.add_block_at(the_board,the_block,("X",3))
        Board.add_block_at(the_board,Block.make_block(4),("e",1))
        Board.add_block_at(the_board,Block.make_block(2),("d",3))
        Board.add_block_at(the_board,Block.make_block(5),("c",2))
        Board.add_block_at(the_board,Block.make_block(3),("e",6))
        Board.add_block_at(the_board,Block.make_block(1),("d",8))
        Board.add_block_at(the_board,Block.make_block(5),("c",8))
        Board.add_block_at(the_board,Block.make_block(2),("a",2))
        if Board.get_supporting_blocks(the_board,the_block) != \
               frozenset( { ("d",3),("e",1),("c",2),("e",6),("d",8),("c",8) }):
            return
        score.value += 12
    except:
        pass


# Tests for get_supported_blocks

def test_Get_Supported_Blocks__No_Blocks(score, max_score):
    """Function get_supported_blocks: no blocks."""
    max_score.value += 1
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("c",3))
        if len(Board.get_supported_blocks(the_board,the_block)) != 0:
            return
        score.value += 1
    except:
        pass

def test_Get_Supported_Blocks__Only_Direct_Blocks(score, max_score):
    """Function get_supported_blocks: only directly supported blocks."""
    max_score.value += 4
    try:
        the_board = Board.make_board((6,14))
        the_block = Block.make_block(7)
        Board.add_block_at(the_board,the_block,("c",3))
        Board.add_block_at(the_board,Block.make_block(2),("d",3))
        Board.add_block_at(the_board,Block.make_block(3),("d",6))
        Board.add_block_at(the_board,Block.make_block(1),("d",9))
        if Board.get_supported_blocks(the_board,the_block) != \
                { ("d",3),("d",6),("d",9) }:
            return
        score.value += 4
    except:
        pass

def test_Get_Supported_Blocks__Direct_And_Indirect_Blocks(score, max_score):
    """Function get_supported_blocks: both directly and indirectly supported blocks."""
    max_score.value += 12
    try:
        the_board = Board.make_board((6,14))
        the_block = Block.make_block(7)
        Board.add_block_at(the_board,the_block,("c",3))
        Board.add_block_at(the_board,Block.make_block(2),("d",3))
        Board.add_block_at(the_board,Block.make_block(4),("e",1))
        Board.add_block_at(the_board,Block.make_block(5),("X",2))
        Board.add_block_at(the_board,Block.make_block(3),("d",6))
        Board.add_block_at(the_board,Block.make_block(1),("d",9))
        Board.add_block_at(the_board,Block.make_block(5),("e",9))
        Board.add_block_at(the_board,Block.make_block(1),("d",2))
        if Board.get_supported_blocks(the_board,the_block) != \
                { ("d",3),("e",1),("X",2),("d",6),("d",9),("e",9) }:
            return
        score.value += 12
    except:
        pass


# Tests for let_fall

def test_Let_Fall__Block_Not_Airborne(score, max_score):
    """Function let_fall: the given block is not airborne."""
    max_score.value += 4
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("c",1))
        Board.add_block_at(the_board,Block.make_block(3),("b",4))
        Board.let_fall(the_board,the_block)
        if Board.get_all_positions_of(the_board,the_block) != \
               (("c",1),("c",2),("c",3),("c",4),("c",5)):
            return
        score.value += 4
    except:
        pass

def test_Let_Fall__Block_Falls_One_Row(score, max_score):
    """Function let_fall: the given block falls down one row."""
    max_score.value += 7
    try:
        the_board = Board.make_board((7,10))
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("e",4))
        Board.add_block_at(the_board,Block.make_block(3),("c",2))
        Board.let_fall(the_board,the_block)
        if Board.get_all_positions_of(the_board,the_block) != \
               (("d",4),("d",5),("d",6),("d",7),("d",8)):
            return
        score.value += 7
    except:
        pass

def test_Let_Fall__Block_Falls_Several_Rows(score, max_score):
    """Function let_fall: the given block falls down several rows."""
    max_score.value += 5
    try:
        the_board = Board.make_board((12,10))
        the_block = Block.make_block(3)
        Board.add_block_at(the_board,the_block,("X",4))
        Board.add_block_at(the_board,Block.make_block(1),("f",4))
        Board.let_fall(the_board,the_block)
        if Board.get_all_positions_of(the_board,the_block) != \
               (("g",4),("g",5),("g",6)):
            return
        score.value += 5
    except:
        pass

def test_Let_Fall__Falling_Block_Reaches_Bottom(score, max_score):
    """Function let_fall: the block falls down to reach the bottom of the board."""
    max_score.value += 5
    try:
        the_board = Board.make_board((12,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("f",4))
        Board.let_fall(the_board,the_block)
        if Board.get_all_positions_of(the_board,the_block) != \
               (("a",4),("a",5),("a",6),("a",7),):
            return
        score.value += 5
    except:
        pass


# Tests for let_all_blocks_fall

def test_Let_All_Blocks_Fall__Single_Case(score, max_score):
    """Function let_all_blocks_fall: single case."""
    max_score.value += 10
    try:
        the_board = Board.make_board((8,10))
        block1 = Block.make_block(2)
        Board.add_block_at(the_board,block1,("a",8))
        block2 = Block.make_block(4)
        Board.add_block_at(the_board,block2,("b",7))
        block3 = Block.make_block(3)
        Board.add_block_at(the_board,block3,("c",3))
        block4 = Block.make_block(2)
        Board.add_block_at(the_board,block4,("d",5))
        block5 = Block.make_block(4)
        Board.add_block_at(the_board,block5,("X",4))
        Board.let_all_blocks_fall(the_board)
        if Board.get_all_blocks(the_board) != \
            [block3,block1,block4,block2,block5]:
            return
        if Board.get_block_at(the_board,("a",8)) is not block1:
            return
        if Board.get_block_at(the_board,("b",7)) is not block2:
            return
        if Board.get_block_at(the_board,("a",3)) is not block3:
            return
        if Board.get_block_at(the_board,("b",5)) is not block4:
            return
        if Board.get_block_at(the_board,("c",4)) is not block5:
            return
        score.value += 10
    except:
        pass


# Tests for let_explode

def test_Let_Explode__Ordinary_Block(score, max_score):
    """Function let_explode: ordinary block."""
    max_score.value += 8
    try:
        the_board = Board.make_board((4,10))
        block_above = Block.make_block(5,Block.ELECTRIFIED)
        Board.add_block_at(the_board, block_above, ("c", 1))
        block_to_explode = Block.make_block(3)
        Board.add_block_at(the_board, block_to_explode, ("b", 4))
        block_below = Block.make_block(2,Block.FRAGILE)
        Board.add_block_at(the_board, block_below, ("a", 6))
        score_for_explosion = Board.let_explode(the_board,block_to_explode)
        if score_for_explosion != Block.get_length(block_to_explode):
            return
        if Board.get_leftmost_position_of(the_board,block_to_explode) is not None:
            return
        if not Board.is_free_at(the_board,("b",4)):
            return
        if Board.get_all_blocks(the_board) != [block_below,block_above]:
            return
        if Board.get_leftmost_position_of(the_board,block_above) != ("c",1):
            return
        if Board.get_leftmost_position_of(the_board,block_below) != ("a",6):
            return
        score.value += 8
    except:
        pass

def test_Let_Explode__Fragile_Block(score, max_score):
    """Function let_explode: fragile block."""
    max_score.value += 10
    try:
        the_board = Board.make_board((4,10))
        block_above = Block.make_block(5,Block.ELECTRIFIED)
        Board.add_block_at(the_board, block_above, ("c", 1))
        block_to_explode = Block.make_block(5,Block.FRAGILE)
        Board.add_block_at(the_board, block_to_explode, ("b", 4))
        block_below = Block.make_block(2)
        Board.add_block_at(the_board, block_below, ("a", 6))
        score_for_explosion = Board.let_explode(the_board,block_to_explode)
        if score_for_explosion != 2*Block.get_length(block_to_explode):
            return
        if Board.get_leftmost_position_of(the_board,block_to_explode) is not None:
            return
        new_block_left = Board.get_block_at(the_board,("b",4))
        if Block.get_length(new_block_left) != 3:
            return
        if Block.get_type(new_block_left) != Block.ORDINARY:
            return
        new_block_right = Board.get_block_at(the_board,("b",7))
        if Block.get_length(new_block_right) != 2:
            return
        if Block.get_type(new_block_right) != Block.FRAGILE:
            return
        if Board.get_all_blocks(the_board) != \
            [block_below,new_block_left,new_block_right,block_above]:
            return
        if Board.get_leftmost_position_of(the_board,block_above) != ("c",1):
            return
        if Board.get_leftmost_position_of(the_board,block_below) != ("a",6):
            return
        score.value += 10
    except:
        pass

def test_Let_Explode__Electrified_Block_No_Adjacent_Blocks(score, max_score):
    """Function let_explode: electrified block with no adjacent blocks below nor above."""
    max_score.value += 6
    try:
        the_board = Board.make_board((6,10))
        block_above = Block.make_block(5,Block.ELECTRIFIED)
        Board.add_block_at(the_board, block_above, ("e", 1))
        block_to_explode = Block.make_block(5,Block.ELECTRIFIED)
        Board.add_block_at(the_board, block_to_explode, ("c", 4))
        block_below = Block.make_block(2)
        Board.add_block_at(the_board, block_below, ("a", 6))
        score_for_explosion = Board.let_explode(the_board,block_to_explode)
        if score_for_explosion != Block.get_length(block_to_explode):
            return
        if Board.get_leftmost_position_of(the_board,block_to_explode) is not None:
            return
        if Board.get_block_at(the_board,("c",4)) is not None:
            return
        if Board.get_all_blocks(the_board) != [block_below,block_above]:
            return
        if Board.get_leftmost_position_of(the_board,block_above) != ("e",1):
            return
        if Board.get_leftmost_position_of(the_board,block_below) != ("a",6):
            return
        score.value += 6
    except:
        pass


def test_Let_Explode__Electrified_Block_No_Adjacent_Electrified_Blocks(score, max_score):
    """Function let_explode: electrified block with no adjacent electrified blocks."""
    max_score.value += 12
    try:
        the_board = Board.make_board((6,10))
        block_above_above = Block.make_block(3)
        Board.add_block_at(the_board,block_above_above,("e",2))
        block_above = Block.make_block(5,Block.FRAGILE)
        Board.add_block_at(the_board, block_above, ("d", 1))
        block_to_explode = Block.make_block(5,Block.ELECTRIFIED)
        Board.add_block_at(the_board, block_to_explode, ("c", 4))
        block_below = Block.make_block(2)
        Board.add_block_at(the_board, block_below, ("b", 6))
        block_below_below = Block.make_block(4,Block.ELECTRIFIED)
        Board.add_block_at(the_board,block_below_below,("a",3))
        score_for_explosion = Board.let_explode(the_board,block_to_explode)
        if score_for_explosion != \
            Block.get_length(block_to_explode) + \
            2*Block.get_length(block_above) + \
            Block.get_length(block_below):
            return
        if Board.get_leftmost_position_of(the_board,block_to_explode) is not None:
            return
        if Board.get_block_at(the_board,("c",4)) is not None:
            return
        if Board.get_leftmost_position_of(the_board,block_above) is not None:
            return
        new_block_1 = Board.get_block_at(the_board,("d",1))
        new_block_2 = Board.get_block_at(the_board,("d",4))
        if Board.get_leftmost_position_of(the_board,block_below) is not None:
            return
        if Board.get_block_at(the_board,("b",6)) is not None:
            return
        if Board.get_all_blocks(the_board) != \
            [block_below_below,new_block_1,new_block_2,block_above_above]:
            return
        if Board.get_leftmost_position_of(the_board,block_above_above) != ("e",2):
            return
        if Board.get_leftmost_position_of(the_board,block_below_below) != ("a",3):
            return
        score.value += 12
    except:
        pass

def test_Let_Explode__Electrified_Block_Cascading_Explosions(score, max_score):
    """Function let_explode: electrified block with cascading explosions."""
    max_score.value += 18
    try:
        the_board = Board.make_board((6,14))
        non_exploding_block_1 = Block.make_block(3,Block.ELECTRIFIED,Color.WHITE)
        Board.add_block_at(the_board,non_exploding_block_1,("e",6))
        block_above_above = Block.make_block(3,Block.ELECTRIFIED,Color.CYAN)
        Board.add_block_at(the_board,block_above_above,("e",2))
        block_above = Block.make_block(5,Block.ELECTRIFIED,Color.RED)
        Board.add_block_at(the_board, block_above, ("d", 1))
        block_to_explode = Block.make_block(5,Block.ELECTRIFIED,Color.MAGENTA)
        Board.add_block_at(the_board, block_to_explode, ("c", 4))
        block_to_the_left = Block.make_block(2,Block.ORDINARY,Color.BLUE)
        Board.add_block_at(the_board,block_to_the_left,("c",1))
        block_to_the_right_1 = Block.make_block(1,Block.ORDINARY,Color.BLACK)
        Board.add_block_at(the_board,block_to_the_right_1,("c",11))
        non_exploding_block_2 = Block.make_block(2,Block.ELECTRIFIED,Color.WHITE)
        Board.add_block_at(the_board,non_exploding_block_2,("c",12))
        block_below = Block.make_block(2,Block.ELECTRIFIED,Color.GREEN)
        Board.add_block_at(the_board, block_below, ("b", 6))
        block_to_the_right_2 = Block.make_block(3,Block.ELECTRIFIED,Color.YELLOW)
        Board.add_block_at(the_board,block_to_the_right_2,("b",9))
        block_below_below = Block.make_block(6,Block.ELECTRIFIED,Color.CYAN)
        Board.add_block_at(the_board,block_below_below,("a",5))
        score_for_explosion = Board.let_explode(the_board,block_to_explode)
        if score_for_explosion != \
            Block.get_length(block_to_explode) + \
            Block.get_length(block_above_above) + \
            Block.get_length(block_above) + \
            Block.get_length(block_to_the_left) + \
            Block.get_length(block_to_the_right_1) + \
            Block.get_length(block_to_the_right_2) + \
            Block.get_length(block_below) + \
            Block.get_length(block_below_below):
            return
        if Board.get_all_blocks(the_board) != \
            [non_exploding_block_2,non_exploding_block_1]:
            return
        score.value += 18
    except:
        pass


# Tests for is_stable

def test_Is_Stable__True_Cases(score, max_score):
    """Function is_stable: true cases."""
    max_score.value += 8
    try:
        the_board = Board.make_board((4,10))
        if not Board.is_stable(the_board):
            return
        Board.add_block_at(the_board, Block.make_block(5), ("c", 1))
        Board.add_block_at(the_board,Block.make_block(3),("b",4))
        Board.add_block_at(the_board,Block.make_block(2),("a",6))
        if not Board.is_stable(the_board):
            return
        the_board = Board.make_board((3,10))
        Board.add_block_at(the_board, Block.make_block(2), ("X", 1))
        Board.add_block_at(the_board,Block.make_block(3),("b",2))
        Board.add_block_at(the_board,Block.make_block(4),("a",3))
        if not Board.is_stable(the_board):
            return
        score.value += 8
    except:
        pass

def test_Is_Stable__False_Cases(score, max_score):
    """Function is_stable: false cases."""
    max_score.value += 8
    try:
        the_board = Board.make_board((4,10))
        Board.add_block_at(the_board, Block.make_block(5), ("c", 1))
        if Board.is_stable(the_board):
            return
        the_board = Board.make_board((4,10))
        Board.add_block_at(the_board, Block.make_block(5), ("c", 1))
        Board.add_block_at(the_board,Block.make_block(3),("b",4))
        Board.add_block_at(the_board,Block.make_block(2),("a",7))
        if Board.is_stable(the_board):
            return
        the_board = Board.make_board((4,10))
        Board.add_block_at(the_board, Block.make_block(1), ("X", 1))
        if Board.is_stable(the_board):
            return
        score.value += 8
    except:
        pass


# Tests for push_all_blocks_in_row_up

def test_Push_All_Blocks_In_Row_Up__No_Blocks_In_Row(score, max_score):
    """Function push_all_blocks_in_row_up: no blocks in row."""
    max_score.value += 4
    try:
        the_board = Board.make_board((6,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("b",5))
        Board.push_all_blocks_in_row_up(the_board,"c")
        if Board.get_all_blocks_in_row(the_board,"c") != []:
            return
        if Board.get_all_blocks_in_row(the_board,"d") != []:
            return
        score.value += 4
    except:
        pass

def test_Push_All_Blocks_In_Row_Up__Some_Blocks_In_Row(score, max_score):
    """Function push_all_blocks_in_row_up: some blocks in row"""
    max_score.value += 8
    try:
        the_board = Board.make_board((6,10))
        block1 = Block.make_block(4)
        Board.add_block_at(the_board,block1,("b",5))
        block2 = Block.make_block(2)
        Board.add_block_at(the_board,block2,("b",2))
        Board.push_all_blocks_in_row_up(the_board,"b")
        if Board.get_all_blocks_in_row(the_board,"b") != []:
            return
        if Board.get_all_blocks_in_row(the_board,"c") != [block2,block1]:
            return
        if Board.get_block_at(the_board,("c",5)) != block1:
            return
        if Board.get_block_at(the_board,("c",8)) != block1:
            return
        if Board.get_block_at(the_board,("c",2)) != block2:
            return
        if Board.get_block_at(the_board, ("c",3)) != block2:
            return
        score.value += 8
    except:
        pass

def test_Push_All_Blocks_In_Row_Up__Full_Row(score, max_score):
    """Function push_all_blocks_in_row_up: full row"""
    max_score.value += 6
    try:
        the_board = Board.make_board((6,10))
        block1 = Block.make_block(4)
        Board.add_block_at(the_board,block1,("e",1))
        block2 = Block.make_block(1)
        Board.add_block_at(the_board,block2,("e",5))
        block3 = Block.make_block(5)
        Board.add_block_at(the_board,block3,("e",6))
        Board.push_all_blocks_in_row_up(the_board,"e")
        if Board.get_all_blocks_in_row(the_board,"e") != []:
            return
        if Board.get_all_blocks_in_row(the_board,"X") != [block1,block2,block3]:
            return
        if Board.get_block_at(the_board,("X",1)) != block1:
            return
        if Board.get_block_at(the_board,("X",4)) != block1:
            return
        if Board.get_block_at(the_board,("X",5)) != block2:
            return
        if Board.get_block_at(the_board,("X",6)) != block3:
            return
        if Board.get_block_at(the_board,("X",10)) != block3:
            return
        score.value += 6
    except:
        pass


# Tests for push_all_blocks_up

def test_Push_All_Blocks_Up__Single_Case(score, max_score):
    """Function push_all_blocks_up: single case."""
    max_score.value += 6
    try:
        the_board = Board.make_board((6,10))
        block1 = Block.make_block(4)
        Board.add_block_at(the_board,block1,("b",5))
        block2 = Block.make_block(2)
        Board.add_block_at(the_board,block2,("b",2))
        block3 = Block.make_block(1)
        Board.add_block_at(the_board,block3,("d",5))
        block4 = Block.make_block(2)
        Board.add_block_at(the_board,block4,("e",8))
        Board.push_all_blocks_up(the_board)
        if not Board.is_empty_row(the_board,"a"):
            return
        if not Board.is_empty_row(the_board,"b"):
            return
        if Board.get_all_blocks_in_row(the_board,"c") != [block2,block1]:
            return
        if Board.get_block_at(the_board,("c",5)) != block1:
            return
        if Board.get_block_at(the_board,("c",2)) != block2:
            return
        if not Board.is_empty_row(the_board,"d"):
            return
        if Board.get_all_blocks_in_row(the_board,"e") != [block3]:
            return
        if Board.get_block_at(the_board,("e",5)) != block3:
            return
        if Board.get_all_blocks_in_row(the_board,"X") != [block4]:
            return
        if Board.get_block_at(the_board,("X",8)) != block4:
            return
        score.value += 6
    except:
        pass


# Tests for can_move_over

def test_Can_Move_Over__Illegal_Number_of_Steps(score, max_score):
    """Function can_move_over: illegal number of steps."""
    max_score.value += 2
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("b",3))
        if Board.can_move_over(the_board,the_block,"abc"):
            return
        if Board.can_move_over(the_board,the_block,(1,2)):
            return
        score.value += 2
    except:
        pass

def test_Can_Move_Over__True_Cases(score, max_score):
    """Function can_move_over: true cases."""
    max_score.value += 7
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("b",3))
        if not Board.can_move_over(the_board,the_block,-1):
            return
        if not Board.can_move_over(the_board,the_block,-2):
            return
        if not Board.can_move_over(the_board,the_block,1):
            return
        if not Board.can_move_over(the_board,the_block,4):
            return
        score.value += 7
    except:
        pass

def test_Can_Move_Over__False_Cases(score, max_score):
    """Function can_move_over: false cases."""
    max_score.value += 7
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("b",3))
        if Board.can_move_over(the_board,the_block,-3):
            return
        if Board.can_move_over(the_board,the_block,5):
            return
        the_block = Block.make_block(3)
        Board.add_block_at(the_board,the_block,("X",1))
        if Board.can_move_over(the_board,the_block,-1):
            return
        the_block = Block.make_block(5)
        Board.add_block_at(the_board,the_block,("a",6))
        if Board.can_move_over(the_board,the_block,1):
            return
        score.value += 7
    except:
        pass


# Tests for move_block_horizontally

def test_Move_Block__Move_Left(score, max_score):
    """Function move_block_horizontally: move to the left."""
    max_score.value += 4
    try:
        the_board = Board.make_board((4,10))
        the_block = Block.make_block(4)
        Board.add_block_at(the_board,the_block,("b",5))
        Board.move_block_horizontally(the_board, the_block, -3)
        if not Board.is_free_at(the_board,("b",1)):
            return
        if Board.get_block_at(the_board,("b",2)) != the_block:
            return
        if Board.get_block_at(the_board,("b",5)) != the_block:
            return
        if not Board.is_free_at(the_board,("b",6)):
            return
        score.value += 4
    except:
        pass

def test_Move_Block__Move_Right(score, max_score):
    """Function move_block_horizontally: move to the right."""
    max_score.value += 4
    try:
        the_board = Board.make_board((8,12))
        the_block = Block.make_block(1)
        Board.add_block_at(the_board,the_block,("X",5))
        Board.move_block_horizontally(the_board, the_block, 7)
        if not Board.is_free_at(the_board,("X",5)):
            return
        if not Board.is_free_at(the_board,("X",11)):
            return
        if Board.get_block_at(the_board,("X",12)) != the_block:
            return
        score.value += 4
    except:
        pass



# collection of board test functions


board_test_functions= \
    {
        test_Make_Board__Single_Case,

        test_Copy_Board__Empty_Board,
        test_Copy_Board__Non_Empty_Board,

        test_Get_Block_At__No_Block,

        test_Is_Free_At__True_Cases,
        test_Is_Free_At__False_Cases,

        test_Get_Leftmost_Position__Block_Not_On_Board,
        test_Get_Leftmost_Position__Block_On_Board,
        test_Get_Leftmost_Position__Block_At_Edges,
        test_Get_Leftmost_Position__Identical_Blocks_On_Board,

        test_Get_Random_Position_For__Positions_Possible,
        test_Get_Random_Position_For__No_Position_Possible,

        test_Get_All_Blocks_In_Row__Empty_Row,
        test_Get_All_Blocks_In_Row__Partially_Filled_Row,
        test_Get_All_Blocks_In_Row__Full_Row,

        test_Get_Length_Largest_Gap_In_Row__Empty_Row,
        test_Get_Length_Largest_Gap_In_Row__Full_Row,
        test_Get_Length_Largest_Gap_In_Row__Gap_In_Middle,
        test_Get_Length_Largest_Gap_In_Row__Gap_Beginning,
        test_Get_Length_Largest_Gap_In_Row__Gap_At_End,

        test_Is_Empty_Row__Single_Test,

        test_Is_Full_Row__True_Cases,
        test_Is_Full_Row__False_Cases,

        test_Get_All_Full_Rows__No_Full_Rows,
        test_Get_All_Full_Rows__Some_Full_Rows,
        test_Get_All_Full_Rows__All_Full_Rows,

        test_Get_All_Blocks__Empty_Board,
        test_Get_All_Blocks__Partially_Filled_Board,
        test_Get_All_Blocks__Full_Board,

        test_Contains_Block__True_Cases,
        test_Contains_Block__False_Cases,

        test_Can_Accept_Block_At__True_Cases,
        test_Can_Accept_Block_At__Adjacent_To_Occupied_Positions,
        test_Can_Accept_Block_At__Identical_Block_On_Board,
        test_Can_Accept_Block_At__Block_Too_Long,
        test_Can_Accept_Block_At__Block_Does_Not_Fully_Fit,
        test_Can_Accept_Block_At__Given_Position_Out_Of_Bounds,
        test_Can_Accept_Block_At__Area_Not_Free,
        test_Can_Accept_Block_At__Block_Already_on_Board,

        test_Add_Block_At__Simple_Case,
        test_Add_Block_At__Identical_Block_On_Board,

        test_Get_All_Positions_Of__Single_Case,

        test_Remove_Block_From__Block_On_Board,
        test_Remove_Block_From__Block_Not_On_Board,
        test_Remove_Block_From__Identical_Block_On_Board,

        test_Is_Airborne__Bottom_Row,
        test_Is_Airborne__True_Case,
        test_Is_Airborne__Support_For_Some_Cells,
        test_Is_Airborne__Support_For_Leftmost_Cell,
        test_Is_Airborne__Support_For_Rightmost_Cell,

        test_Get_Adjacent_Blocks_Above__No_Blocks,
        test_Get_Adjacent_Blocks_Above__Some_Blocks,
        test_Get_Adjacent_Blocks_Above__Block_At_Edges,

        test_Get_Adjacent_Block_Left__No_Block,
        test_Get_Adjacent_Block_Left__Effective_Block,

        test_Get_Adjacent_Blocks_Below__No_Blocks,
        test_Get_Adjacent_Blocks_Below__Some_Blocks,
        test_Get_Adjacent_Blocks_Below__Block_At_Edges,

        test_Get_Adjacent_Block_Right__No_Block,
        test_Get_Adjacent_Block_Right__Effective_Block,

        test_Get_Supporting_Blocks__No_Blocks,
        test_Get_Supporting_Blocks__Only_Direct_Blocks,
        test_Get_Supporting_Blocks__Direct_And_Indirect_Blocks,

        test_Get_Supported_Blocks__No_Blocks,
        test_Get_Supported_Blocks__Only_Direct_Blocks,
        test_Get_Supported_Blocks__Direct_And_Indirect_Blocks,

        test_Let_Fall__Block_Not_Airborne,
        test_Let_Fall__Block_Falls_One_Row,
        test_Let_Fall__Block_Falls_Several_Rows,
        test_Let_Fall__Falling_Block_Reaches_Bottom,

        test_Let_All_Blocks_Fall__Single_Case,

        test_Let_Explode__Ordinary_Block,
        test_Let_Explode__Fragile_Block,
        test_Let_Explode__Electrified_Block_No_Adjacent_Blocks,
        test_Let_Explode__Electrified_Block_No_Adjacent_Electrified_Blocks,
        test_Let_Explode__Electrified_Block_Cascading_Explosions,

        test_Is_Stable__True_Cases,
        test_Is_Stable__False_Cases,

        test_Push_All_Blocks_In_Row_Up__No_Blocks_In_Row,
        test_Push_All_Blocks_In_Row_Up__Some_Blocks_In_Row,
        test_Push_All_Blocks_In_Row_Up__Full_Row,

        test_Push_All_Blocks_Up__Single_Case,

        test_Can_Move_Over__Illegal_Number_of_Steps,
        test_Can_Move_Over__True_Cases,
        test_Can_Move_Over__False_Cases,

        test_Move_Block__Move_Left,
        test_Move_Block__Move_Right,
    }

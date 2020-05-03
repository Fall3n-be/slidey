import Color
import Block


# Tests for make_block

def test_Make_Block__Ordinary_Block_Default_Type_Color(score, max_score):
    """Function make_block: ordinary block with default type and default color."""
    max_score.value += 1
    try:
        the_block = Block.make_block(100)
        if Block.get_length(the_block) != 100:
            return
        if Block.get_type(the_block) != Block.ORDINARY:
            return
        if Block.get_color(the_block) != Color.BLACK:
            return
        score.value += 1
    except:
        pass

def test_Make_Block__Ordinary_Red_Block(score, max_score):
    """Function make_block: ordinary red block."""
    max_score.value += 1
    try:
        the_block = Block.make_block(55,color=Color.RED)
        if Block.get_length(the_block) != 55:
            return
        if Block.get_type(the_block) != Block.ORDINARY:
            return
        if Block.get_color(the_block) != Color.RED:
            return
        score.value += 1
    except:
        pass

def test_Make_Block__Electrified_Block(score, max_score):
    """Function make_block: electrified block."""
    max_score.value += 1
    try:
        the_block = Block.make_block(66,Block.ELECTRIFIED,Color.BLUE)
        if Block.get_length(the_block) != 66:
            return
        if Block.get_type(the_block) != Block.ELECTRIFIED:
            return
        if Block.get_color(the_block) != Color.BLUE:
            return
        score.value += 1
    except:
        pass

def test_Make_Block__Fragile_Block(score, max_score):
    """Function make_block: fragile block."""
    max_score.value += 1
    try:
        the_block = Block.make_block(77,type=Block.FRAGILE,color=Color.CYAN)
        if Block.get_length(the_block) != 77:
            return
        if Block.get_type(the_block) != Block.FRAGILE:
            return
        if Block.get_color(the_block) != Color.CYAN:
            return
        score.value += 1
    except:
        pass


# Tests for split_block

def test_Split_Block__Even_Length_Sub_Blocks(score, max_score):
    """Function split_block: sub blocks of even length."""
    max_score.value += 2
    try:
        the_block = Block.make_block(8,color=Color.MAGENTA)
        (block1,block2) = Block.split_block(the_block)
        if Block.get_length(block1) != 4:
            return
        if Block.get_type(block1) != Block.FRAGILE:
            return
        if Block.get_color(block1) != Block.get_color(the_block):
            return
        if Block.get_length(block2) != 4:
            return
        if Block.get_type(block2) != Block.FRAGILE:
            return
        if Block.get_color(block2) != Block.get_color(the_block):
            return
        score.value += 2
    except:
        pass

def test_Split_Block__Odd_Length_Sub_Blocks(score, max_score):
    """Function split_block: sub blocks of odd length."""
    max_score.value += 2
    try:
        the_block = Block.make_block(6,Block.FRAGILE,Color.RED)
        (block1,block2) = Block.split_block(the_block)
        if Block.get_length(block1) != 3:
            return
        if Block.get_type(block1) != Block.ORDINARY:
            return
        if Block.get_color(block1) != Block.get_color(the_block):
            return
        if Block.get_length(block2) != 3:
            return
        if Block.get_type(block2) != Block.ORDINARY:
            return
        if Block.get_color(block2) != Block.get_color(the_block):
            return
        score.value += 2
    except:
        pass

def test_Split_Block__Mixed_Length_Sub_Blocks(score, max_score):
    """Function split_block: sub blocks of mixed length."""
    max_score.value += 2
    try:
        the_block = Block.make_block(7)
        (block1,block2) = Block.split_block(the_block)
        if Block.get_length(block1) != 4:
            return
        if Block.get_type(block1) != Block.FRAGILE:
            return
        if Block.get_color(block1) != Block.get_color(the_block):
            return
        if Block.get_length(block2) != 3:
            return
        if Block.get_type(block2) != Block.ORDINARY:
            return
        if Block.get_color(block2) != Block.get_color(the_block):
            return
        score.value += 2
    except:
        pass


# Tests for is_proper_block

def test_Is_Proper_Block__True_Case(score, max_score):
    """Function is_proper_block: true case."""
    max_score.value += 1
    try:
        the_block = Block.make_block(100)
        if not Block.is_proper_block(the_block):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Block__False_Case(score, max_score):
    """Function is_proper_block: false case."""
    max_score.value += 1
    try:
        if Block.is_proper_block("abc"):
            return
        score.value += 1
    except:
        pass


# Tests for is_proper_block_for_dimension

def test_Is_Proper_Block_For_Dimension__True_Cases(score, max_score):
    """Function is_proper_block_for_dimension: true cases."""
    max_score.value += 1
    try:
        the_block = Block.make_block(10)
        if not Block.is_proper_block_for_dimension(the_block,(5,20)):
            return
        if not Block.is_proper_block_for_dimension(the_block,(7,21)):
            return
        if not Block.is_proper_block_for_dimension(the_block,(12,30)):
            return
        the_block = Block.make_block(5)
        if not Block.is_proper_block_for_dimension(the_block,(6,10)):
            return
        if not Block.is_proper_block_for_dimension(the_block,(12,11)):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Block_For_Dimension__False_Cases(score, max_score):
    """Function is_proper_block_for_dimension: false cases."""
    max_score.value += 1
    try:
        the_block = Block.make_block(10)
        if Block.is_proper_block_for_dimension(the_block,(4,19)):
            return
        if Block.is_proper_block_for_dimension(the_block,(11,18)):
            return
        if Block.is_proper_block_for_dimension(the_block,(6,4)):
            return
        the_block = Block.make_block(5)
        if Block.is_proper_block_for_dimension(the_block,(14,9)):
            return
        if Block.is_proper_block_for_dimension(the_block,(7,8)):
            return
        score.value += 1
    except:
        pass


# collection of block test functions

block_test_functions = \
    {
        test_Make_Block__Ordinary_Block_Default_Type_Color,
        test_Make_Block__Ordinary_Red_Block,
        test_Make_Block__Electrified_Block,
        test_Make_Block__Fragile_Block,

        test_Split_Block__Even_Length_Sub_Blocks,
        test_Split_Block__Odd_Length_Sub_Blocks,
        test_Split_Block__Mixed_Length_Sub_Blocks,

        test_Is_Proper_Block__True_Case,
        test_Is_Proper_Block__False_Case,

        test_Is_Proper_Block_For_Dimension__True_Cases,
        test_Is_Proper_Block_For_Dimension__False_Cases,

    }

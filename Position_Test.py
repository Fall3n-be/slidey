# Tests for is_proper_position

import Position

def test_Is_Proper_Position__Legal_Case(score, max_score):
    """Function is_proper_position: given position is proper position."""
    max_score.value += 1
    try:
        if not Position.is_proper_position(("a", 1)):
            return
        if not Position.is_proper_position(("z", 23)):
            return
        if not Position.is_proper_position(("X", 12)):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Position__Not_Tuple(score, max_score):
    """Function is_proper_position: given position is not a tuple."""
    max_score.value += 1
    try:
        if Position.is_proper_position(["a", 2]):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Position__Improper_Length(score, max_score):
    """Function is_proper_position: given position is a tuple of length different from 2."""
    max_score.value += 1
    try:
        if Position.is_proper_position(("a",)):
            return
        if Position.is_proper_position(("b", 2, 3)):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Position__Improper_First_Element(score, max_score):
    """Function is_proper_position: given position is a tuple of length 2 with non-integer as first element."""
    max_score.value += 1
    try:
        if Position.is_proper_position((3.14, 3)):
            return
        if Position.is_proper_position(("A",1)):
            return
        if Position.is_proper_position(("",1)):
            return
        if Position.is_proper_position(("ab",1)):
            return
        if Position.is_proper_position(((1,), 3)):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Position__Improper_Second_Element(score, max_score):
    """Function is_proper_position: given position is a tuple of length 2 with non-integer as second element."""
    max_score.value += 1
    try:
        if Position.is_proper_position(("a", 0)):
            return
        if Position.is_proper_position(("a", -1)):
            return
        if Position.is_proper_position(("a", "b")):
            return
        if Position.is_proper_position((3, [1])):
            return
        score.value += 1
    except:
        pass


# Tests for is_within_boundaries

def test_Is_Within_Boundaries__True_Cases(score, max_score):
    """Function is_within_boundaries: true cases."""
    max_score.value += 1
    try:
        if not Position.is_within_boundaries((7,3),("a",1)):
            return
        if not Position.is_within_boundaries((7,3),("X",2)):
            return
        if not Position.is_within_boundaries((7,3),("f",3)):
            return
        score.value += 1
    except:
        pass

def test_Is_Within_Boundaries__False_Cases(score, max_score):
    """Function is_within_boundaries: true cases."""
    max_score.value += 1
    try:
        if Position.is_within_boundaries((7,3),("g",3)):
            return
        if Position.is_within_boundaries((7,3),("c",4)):
            return
        score.value += 1
    except:
        pass


# Tests for nb_of_row

def test_Nb_Of_Row__Non_Top_Row(score, max_score):
    """Function nb_of_row: non top row"""
    max_score.value += 1
    try:
        if Position.nb_of_row((4,8),"a") != 1:
            return
        if Position.nb_of_row((7,6),"c") != 3:
            return
        if Position.nb_of_row((5,9),"d") != 4:
            return
        score.value += 1
    except:
        pass

def test_Nb_Of_Row__Top_Row(score, max_score):
    """Function nb_of_row: top row"""
    max_score.value += 1
    try:
        if Position.nb_of_row((4,8),"X") != 4:
            return
        if Position.nb_of_row((7,6),"X") != 7:
            return
        score.value += 1
    except:
        pass


# Tests for id_of_row

def test_Id_Of_Row__Non_Top_Row(score, max_score):
    """Function id_of_row: non top row"""
    max_score.value += 1
    try:
        if Position.id_of_row((4,8),1) != "a":
            return
        if Position.id_of_row((7,6),3) != "c":
            return
        if Position.id_of_row((5,9),4) != "d":
            return
        score.value += 1
    except:
        pass

def test_Id_Of_Row__Top_Row(score, max_score):
    """Function id_of_row: top row"""
    max_score.value += 1
    try:
        if Position.id_of_row((4,8),4) != "X":
            return
        if Position.id_of_row((7,6),7) != "X":
            return
        score.value += 1
    except:
        pass


# Tests for left

def test_Left__Position_In_Range(score, max_score):
    """Function left: resulting position in range"""
    max_score.value += 1
    try:
        if Position.left((8,6), ("b", 4)) != ("b", 3):
            return
        if Position.left((10,12), ("X", 8), 5) != ("X", 3):
            return
        if Position.left((5,6), ("a", 4), 3) != ("a", 1):
            return
        score.value += 1
    except:
        pass

def test_Left__Position_Out_Of_Range(score, max_score):
    """Function left: resulting position out of range"""
    max_score.value += 1
    try:
        if Position.left((9,8), ("d",1)) is not None:
            return
        if Position.left((9,8), ("d",4), 4) is not None:
            return
        score.value += 1
    except:
        pass


# Tests for right

def test_Right__Position_In_Range(score, max_score):
    """Function right: resulting position in range"""
    max_score.value += 1
    try:
        if Position.right((7,8), ("c", 4)) != ("c", 5):
            return
        if Position.right((10,12), ("X", 3), 6) != ("X", 9):
            return
        if Position.right((4,6), ("a", 1), 5) != ("a", 6):
            return
        score.value += 1
    except:
        pass

def test_Right__Position_Out_Of_Range(score, max_score):
    """Function right: resulting position out of range"""
    max_score.value += 1
    try:
        if Position.right((4,9), ("c", 9)) is not None:
            return
        if Position.right((10,12), ("X", 6), 7) is not None:
            return
        score.value += 1
    except:
        pass


# Tests for up

def test_Up__Position_In_Range(score, max_score):
    """Function up: resulting position in range"""
    max_score.value += 1
    try:
        if Position.up((6,8), ("c", 6)) != ("d", 6):
            return
        if Position.up((6,8), ("b", 6), 3) != ("e", 6):
            return
        if Position.up((6,9), ("e", 8)) != ("X",8):
            return
        if Position.up((10,10), ("e", 2), 5) != ("X",2):
            return
        score.value += 1
    except:
        pass

def test_Up__Position_Out_Of_Range(score, max_score):
    """Function up: resulting position out of range"""
    max_score.value += 1
    try:
        if Position.up((6,9), ("X", 8)) is not None:
            return
        if Position.up((10,12), ("b", 1), 12) is not None:
            return
        if Position.up((6,4), ("c", 2), 4) is not None:
            return
        score.value += 1
    except:
        pass


# Tests for down

def test_Down__Middle_Position(score, max_score):
    """Function down: middle position"""
    max_score.value += 1
    try:
        if Position.down((8,6), ("d", 2)) != ("c", 2):
            return
        score.value += 1
    except:
        pass

def test_Down__Top_Position(score, max_score):
    """Function down: top position"""
    max_score.value += 1
    try:
        if Position.down((8,6), ("X", 2)) != ("g", 2):
            return
        score.value += 1
    except:
        pass

def test_Down__Bottom_Position(score, max_score):
    """Function down: bottom position"""
    max_score.value += 1
    try:
        if Position.down((4,6), ("a", 3)) is not None:
            return
        score.value += 1
    except:
        pass



# collection of position test functions

position_test_functions = \
    {
        test_Is_Proper_Position__Legal_Case,
        test_Is_Proper_Position__Not_Tuple,
        test_Is_Proper_Position__Improper_Length,
        test_Is_Proper_Position__Improper_First_Element,
        test_Is_Proper_Position__Improper_Second_Element,

        test_Is_Within_Boundaries__True_Cases,
        test_Is_Within_Boundaries__False_Cases,

        test_Nb_Of_Row__Non_Top_Row,
        test_Nb_Of_Row__Top_Row,

        test_Id_Of_Row__Non_Top_Row,
        test_Id_Of_Row__Top_Row,

        test_Left__Position_In_Range,
        test_Left__Position_Out_Of_Range,

        test_Right__Position_Out_Of_Range,
        test_Right__Position_In_Range,

        test_Up__Position_In_Range,
        test_Up__Position_Out_Of_Range,

        test_Down__Middle_Position,
        test_Down__Top_Position,
        test_Down__Bottom_Position,

    }

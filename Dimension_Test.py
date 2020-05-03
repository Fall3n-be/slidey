import Dimension

# Tests for is_proper_dimension

def test_Is_Proper_Dimension__Legal_Case(score, max_score):
    """Function is_proper_dimension: given dimension is a proper dimension."""
    max_score.value += 1
    try:
        if not Dimension.is_proper_dimension((7,3)):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Dimension__Not_Tuple(score, max_score):
    """Function is_proper_dimension: given dimension is not a tuple."""
    max_score.value += 1
    try:
        if Dimension.is_proper_dimension([8, 2]):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Dimension__Improper_Length(score, max_score):
    """Function is_proper_dimension: given dimension is a tuple of
       length different from 2."""
    max_score.value += 1
    try:
        if Dimension.is_proper_dimension((9,)):
            return
        if Dimension.is_proper_dimension((10, 4, 3)):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Dimension__Improper_First_Element(score, max_score):
    """Function is_proper_dimension: given dimension is a tuple of length 2
       with non-integer as first element."""
    max_score.value += 1
    try:
        if Dimension.is_proper_dimension((3.14, 3)):
            return
        if Dimension.is_proper_dimension((-2,1)):
            return
        if Dimension.is_proper_dimension((1,1)):
            return
        if Dimension.is_proper_dimension(("ab",1)):
            return
        if Dimension.is_proper_dimension(((1,), 3)):
            return
        score.value += 1
    except:
        pass

def test_Is_Proper_Dimension__Improper_Second_Element(score, max_score):
    """Function is_proper_dimension: given dimension is a tuple of length 2 with non-integer as second element."""
    max_score.value += 1
    try:
        if Dimension.is_proper_dimension((2, 1)):
            return
        if Dimension.is_proper_dimension((2, -1)):
            return
        if Dimension.is_proper_dimension((7, "b")):
            return
        if Dimension.is_proper_dimension((3, [1])):
            return
        score.value += 1
    except:
        pass


# collection of dimension test functions

dimension_test_functions = \
    {
        test_Is_Proper_Dimension__Legal_Case,
        test_Is_Proper_Dimension__Not_Tuple,
        test_Is_Proper_Dimension__Improper_Length,
        test_Is_Proper_Dimension__Improper_First_Element,
        test_Is_Proper_Dimension__Improper_Second_Element,
    }

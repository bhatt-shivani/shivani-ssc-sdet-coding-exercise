import pytest
from remove_duplicates import remove_duplicates


def test_remove_duplicates_1():
    """
    Test case: Remove duplicates from a list containing mixed values.

    We are testing the normal functionality where the list contains
    repreated values, and we want to ensure the function returns a 
    list of unique elements in the original order.
    """
    input_data = [1, 2, 3, 2, 4, 1, 5]
    expected_output = [1,2,3,4,5]
    assert remove_duplicates(input_data) == expected_output

def test_remove_duplicates_2():
    """
    Test case: Handle the case where all elements are duplicates. 

    The list only contains the same value repeated, and we expect
    the function to return that single value in a list.
    """
    input_data = [1,1,1]
    expected_output = [1]
    assert remove_duplicates(input_data) == expected_output

def test_remove_duplicates_3():
    """
    Test case: Handle an empty list.

    This test checks that an empty list is correctly handled by the function,
    and the function should return an empty list.
    """
    input_data = []
    expected_output = []
    assert remove_duplicates(input_data) == expected_output

def test_remove_duplicates_mixed_types():
    """
    Test case: Handle a list with mixed data types

    This test checks that the function can handle lists with a mix
    of strings and integers to ensure it removes duplicates while
    preserving original order.
    """
    input_data = ["hello", 1, 1, "hello", "hi"]
    expected_output = ["hello", 1, "hi"]
    assert remove_duplicates(input_data) == expected_output

def test_remove_duplicates_with_invalid_input():
    """
    Test Case: Handle invalid input (non-list type).

    This test checks that passing a non-list input raises a TypeError.
    """
    with pytest.raises(TypeError):
        remove_duplicates("not a list")

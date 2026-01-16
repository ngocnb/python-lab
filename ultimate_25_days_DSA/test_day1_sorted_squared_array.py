import pytest

from day1 import sorted_squared_array

def test_positive_integers():
    """Tests an array with only positive integers."""
    assert sorted_squared_array([1, 2, 3, 5, 6, 8, 9]) == [1, 4, 9, 25, 36, 64, 81]

def test_negative_integers():
    """Tests an array with only negative integers."""
    assert sorted_squared_array([-5, -4, -3, -2, -1]) == [1, 4, 9, 16, 25]

def test_mixed_integers():
    """Tests a mix of negative and positive integers (the core challenge)."""
    assert sorted_squared_array([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

def test_zeros_and_duplicates():
    """Tests arrays containing zeros and repeated values."""
    assert sorted_squared_array([-2, -2, 0, 2, 2]) == [0, 4, 4, 4, 4]
    assert sorted_squared_array([0, 0, 0]) == [0, 0, 0]

def test_single_element():
    """Tests an array with a single element."""
    assert sorted_squared_array([-5]) == [25]
    assert sorted_squared_array([0]) == [0]

def test_empty_array():
    """Tests an empty input."""
    assert sorted_squared_array([]) == []

@pytest.mark.parametrize("input_arr, expected", [
    ([-10, -5, 0, 5, 10], [0, 25, 25, 100, 100]),
    ([-1, 1], [1, 1]),
    ([1, 2, 3], [1, 4, 9]),
])
def test_parameterized_cases(input_arr, expected):
    """Bonus: Using parametrization for cleaner multiple test cases."""
    assert sorted_squared_array(input_arr) == expected
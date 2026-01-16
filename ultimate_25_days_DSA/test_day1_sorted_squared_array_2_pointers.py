import pytest

from day1 import sorted_squared_array_2_pointers

@pytest.mark.parametrize("input_arr, expected", [
    ([-10, -5, 0, 5, 10], [0, 25, 25, 100, 100]),
    ([-1, 1], [1, 1]),
    ([1, 2, 3], [1, 4, 9]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([-2, -2, 0, 2, 2], [0, 4, 4, 4, 4]),
    ([-5], [25]), # Tests an array with a single element.
    ([], []) # empty input
])
def test_parameterized_cases(input_arr, expected):
    """Bonus: Using parametrization for cleaner multiple test cases."""
    assert sorted_squared_array_2_pointers(input_arr) == expected
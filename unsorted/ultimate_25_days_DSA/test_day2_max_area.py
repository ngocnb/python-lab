import pytest

from day2 import max_area

@pytest.mark.parametrize("height, expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # Standard case: max is between index 1 and 8
    ([1, 1], 1),                       # Minimum length array
    ([4, 3, 2, 1, 4], 16),             # Max area at the far ends (4 and 4)
    ([1, 2, 1], 2),                    # Small array with middle peak
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25), # Decreasing heights
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25), # Increasing heights
    ([0, 2], 0),                       # One wall has zero height
    ([1, 2, 4, 3], 4),                 # Optimal not at the ends
    ([100, 2, 100], 200),              # Narrow but very tall container
], ids=[
    "standard_example",
    "minimum_length",
    "max_at_boundaries",
    "small_array_peak",
    "decreasing_heights",
    "increasing_heights",
    "zero_height_wall",
    "internal_optimum",
    "tall_narrow_container"
])
def test_max_area(height, expected):
    """
    Tests the max_area function which calculates the maximum amount of water 
    a container can store given an array of heights.
    """
    assert max_area(height) == expected
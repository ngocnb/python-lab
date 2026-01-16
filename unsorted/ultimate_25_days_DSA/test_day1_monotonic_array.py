import pytest

from day1 import is_monotonic

@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5], True),  # Strictly increasing
        ([5, 4, 3, 2, 1], True),  # Strictly decreasing
        ([1, 2, 2, 3, 3, 10], True),  # Monotonic increasing (with duplicates)
        ([10, 10, 5, 5, 2, 1], True),  # Monotonic decreasing (with duplicates)
        ([1, 1, 1, 1], True),  # All same elements
        ([1, 2, 3, 2, 1], False),  # Increasing then decreasing
        ([5, 4, 3, 4, 5], False),  # Decreasing then increasing
        ([1, 2, 1], False),  # Small fluctuation
        ([-1, -5, -10], True),  # Negative monotonic
        ([1], True),  # Single element
        ([], True),  # Empty list
    ],
    ids=[
        "strictly_increasing",
        "strictly_decreasing",
        "increasing_with_duplicates",
        "decreasing_with_duplicates",
        "all_same",
        "up_then_down",
        "down_then_up",
        "small_fluctuation",
        "negative_values",
        "single_element",
        "empty_list",
    ],
)
def test_is_monotonic(arr, expected):
    assert is_monotonic(arr) == expected

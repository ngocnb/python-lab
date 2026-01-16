import pytest

from day2 import rotate_array


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),  # Standard case
        ([1, 2], 3, [2, 1]),  # k is larger than array length (k % n)
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),  # Negative numbers
        ([1, 2, 3], 0, [1, 2, 3]),  # k = 0 (no rotation)
        ([1, 2, 3], 3, [1, 2, 3]),  # k is exactly array length
        ([1], 10, [1]),  # Single element
        ([], 5, []),  # Empty array
        ([1, 2], 0, [1, 2]),  # Small array, no rotation
    ],
    ids=[
        "standard_rotation",
        "k_greater_than_length",
        "mixed_numbers",
        "zero_rotation",
        "full_cycle_rotation",
        "single_element",
        "empty_array",
        "small_array_zero_k",
    ],
)
def test_rotate_array(nums, k, expected):
    # Create a copy to avoid side effects if function modifies in-place
    input_list = list(nums)

    # Call the function
    # If your function returns the array: result = rotate_array(input_list, k)
    # If your function is in-place:
    result = rotate_array(input_list, k)

    assert result == expected


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3], 4, [3, 1, 2]),  # k = length + 1 (Effective k=1)
        ([1, 2, 3], 6, [1, 2, 3]),  # k is exact multiple of length (k % n = 0)
        ([1, 2, 3, 4], 10, [3, 4, 1, 2]),  # k = 2 * length + 2 (Effective k=2)
        ([1, 2], 101, [2, 1]),  # Large odd k on small array (Effective k=1)
        ([1, 2, 3, 4, 5], 1000, [1, 2, 3, 4, 5]),  # Very large multiple of length
        ([1, 2, 3, 4, 5], 1002, [4, 5, 1, 2, 3]),  # Very large k (Effective k=2)
    ],
    ids=[
        "k_is_length_plus_one",
        "k_is_exact_multiple",
        "k_is_more_than_double_length",
        "large_odd_k",
        "very_large_multiple",
        "very_large_k_with_remainder",
    ],
)
def test_rotate_array_large_k(nums, k, expected):
    input_list = list(nums)
    result = rotate_array(input_list, k)
    assert result == expected

from chapter1 import is_even, is_even_bitwise
import pytest

# This decorater runs the test function with each tuple in the list
@pytest.mark.parametrize("n, expected", [
    (20, True),
    (100, True),
    (15, False),
    (-20, True),
    (-7, False),
    ('aa', False),
    (15.5, False),
    (20.15, False),
    (None, False)
])
def test_is_even(n, expected):
    assert is_even(n) == expected

@pytest.mark.parametrize("n, expected", [
    (4, True),      # Positive even
    (7, False),     # Positive odd
    (0, True),      # Zero (even)
    (-2, True),     # Negative even
    (-5, False),    # Negative odd
    (42, True),     # Large even
])
def test_is_even_bitwise_valid_integers(n, expected):
    assert is_even_bitwise(n) == expected

def test_is_even_bitwise_invalid_type():
    # Should return False for non-integers (strings, floats)
    assert is_even_bitwise(4.5) == False
    assert is_even_bitwise("two") == False
from chapter1 import sum_square_comprehension
import pytest

# --- 1. Test Cases for Valid Positive Integers (Core Functionality) ---

@pytest.mark.parametrize("n, expected_sum", [
    # n=1: Sum(1 to 0) = 0
    (1, 0),
    
    # n=2: Sum(1 to 1) = 1^2 = 1
    (2, 1),
    
    # n=3: Sum(1 to 2) = 1^2 + 2^2 = 1 + 4 = 5
    (3, 5),
    
    # n=4: Sum(1 to 3) = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
    (4, 14),
    
    # n=5: Sum(1 to 4) = 1^2 + 2^2 + 3^2 + 4^2 = 14 + 16 = 30
    (5, 30),
    
    # n=11: Sum(1 to 10) = 385 (Using the formula with m=10)
    (11, 385),
])
def test_valid_positive_integers(n, expected_sum):
    """Tests the function for standard positive inputs up to n-1."""
    assert sum_square_comprehension(n) == expected_sum

# --- 2. Test Cases for Edge Cases (n <= 1) ---

def test_n_is_one():
    """Tests the minimum valid input n=1, where the range is empty."""
    assert sum_square_comprehension(1) == 0

def test_n_is_zero():
    """Tests when n is 0, which should result in an empty range (0, 0)."""
    assert sum_square_comprehension(0) == 0

def test_n_is_negative():
    """Tests when n is negative. The range is empty, so the sum should be 0."""
    assert sum_square_comprehension(-5) == 0
    
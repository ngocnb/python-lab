from chapter1 import sum_numbers, sum_numbers_gaussian_formula
import pytest

# --- 1. Test Cases for Valid Positive Integers (Core Functionality) ---

@pytest.mark.parametrize("n, expected_sum", [
    (2, 1),       # Sum up to 2-1 (1) = 1
    (3, 3),       # Sum up to 3-1 (2) = 1 + 2 = 3
    (6, 15),      # Sum up to 6-1 (5) = 1 + ... + 5 = 15
    (11, 55),     # Sum up to 11-1 (10) = 55
    (101, 5050),  # Sum up to 101-1 (100) = 5050
    (1000, 499500),# Sum up to 1000-1 (999)
])
def test_valid_positive_integers(n, expected_sum):
    """Tests the formula for standard positive inputs (sum up to n-1)."""
    assert sum_numbers(n) == expected_sum

# --- 2. Test Cases for Edge Cases (Zero and One) ---

def test_n_is_one():
    """Tests the function when n is 1 (Sum from 1 to 0), should be 0."""
    assert sum_numbers(1) == 0

def test_n_is_zero():
    """Tests the function when n is 0 (Sum from 1 to -1), should also be 0/handled."""
    # Assuming your logic handles n <= 1 by returning 0
    assert sum_numbers(0) == 0

# --- 3. Test Cases for Invalid Data Types and Negative Input (Error Handling) ---

def test_n_is_negative():
    """Tests the function when n is a negative integer (should be handled)."""
    assert sum_numbers(-5) == 0

def test_n_is_string():
    """Tests non-integer input (string) which should cause an error."""
    assert sum_numbers("abc") == False

def test_n_is_convertible_string():
    """Tests a string that can be converted to a valid number."""
    # Sum up to 6-1 (5) = 15
    assert sum_numbers("6") == 15

# --- 1. Test Cases for Valid Positive Integers (Core Functionality) ---

@pytest.mark.parametrize("n, expected_sum", [
    (2, 1),       # Sum up to 2-1 (1) = 1
    (3, 3),       # Sum up to 3-1 (2) = 1 + 2 = 3
    (6, 15),      # Sum up to 6-1 (5) = 1 + ... + 5 = 15
    (11, 55),     # Sum up to 11-1 (10) = 55
    (101, 5050),  # Sum up to 101-1 (100) = 5050
    (1000, 499500),# Sum up to 1000-1 (999)
])
def test_gaussian_formula_valid_positive_integers(n, expected_sum):
    """Tests the formula for standard positive inputs (sum up to n-1)."""
    assert sum_numbers_gaussian_formula(n) == expected_sum

# --- 2. Test Cases for Edge Cases (Zero and One) ---

def test_gaussian_formula_n_is_one():
    """Tests the function when n is 1 (Sum from 1 to 0), should be 0."""
    assert sum_numbers_gaussian_formula(1) == 0

def test_gaussian_formula_n_is_zero():
    """Tests the function when n is 0 (Sum from 1 to -1), should also be 0/handled."""
    # Assuming your logic handles n <= 1 by returning 0
    assert sum_numbers_gaussian_formula(0) == 0

# --- 3. Test Cases for Invalid Data Types and Negative Input (Error Handling) ---

def test_gaussian_formula_n_is_negative():
    """Tests the function when n is a negative integer (should be handled)."""
    assert sum_numbers_gaussian_formula(-5) == 0

def test_gaussian_formula_n_is_string():
    """Tests non-integer input (string) which should cause an error."""
    assert sum_numbers_gaussian_formula("abc") == False

def test_gaussian_formula_n_is_convertible_string():
    """Tests a string that can be converted to a valid number."""
    # Sum up to 6-1 (5) = 15
    assert sum_numbers_gaussian_formula("6") == 15
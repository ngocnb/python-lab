from chapter1 import is_multiple
import pytest

# This decorater runs the test function with each tuple in the list
@pytest.mark.parametrize("n, m, expected", [
    (20, 5, True),    # Your test case: 20 and 5
    (20, 6, False),   # Your test case: 20 and 6
    (7.5, 2.5, True), # Your test case: 7.5 and 2.5
    (20.25, 5, False),# Your test case: 20.25 and 5
    (10, -5, True),   # Negative divisor
    (-10, 5, True),   # Negative dividend
    (0, 5, True),     # 0 is a multiple of any non-zero number
    (5, 0, False),    # Division by zero case
    ("20", 5, False), # Invalid type: string
    (20, "5", False), # Invalid type: string
    (20, None, False),# Invalid type: None
])
def test_valid_numbers(n, m, expected):
    # This single function replaces many individual tests
    assert is_multiple(n, m) == expected


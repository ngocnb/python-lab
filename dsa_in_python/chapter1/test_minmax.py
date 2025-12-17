from chapter1 import minmax
import pytest

@pytest.mark.parametrize("data, expected", [
    (range(1000), (0, 999)),
    (range(200, 700, 3), (200, 698)),
    ([10, 30, 1000, 1, 3], (1, 1000)),
    ([10, 30, 1000.25, 1.75, 3], (1.75, 1000.25)),   # contains float
    ([10, 30, 1000, 'aa', 3], False),     # contains string
    ([], False),                          # empty list
    (10, False)                           # invalid list - integer
])
def test_minmax(data, expected):
    assert minmax(data) == expected
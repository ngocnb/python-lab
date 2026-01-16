import math
import pytest
from my_math.basic import my_abs, my_trunc, my_floor, my_ceil

test_data = [
    0, 1, -1, 
    0.5, -0.5,
    1.2, -1.2,
    1.9, -1.9,
    123.456, -123.456
]

@pytest.mark.parametrize("x", test_data)
def test_abs(x):
    assert my_abs(x) == abs(x)

@pytest.mark.parametrize("x", test_data)
def test_trunc(x):
    assert my_trunc(x) == math.trunc(x)

@pytest.mark.parametrize("x", test_data)
def test_floor(x):
    assert my_floor(x) == math.floor(x)

@pytest.mark.parametrize("x", test_data)
def test_ceil(x):
    assert my_ceil(x) == math.ceil(x)

invalid_inputs = ["a", None, [1], (1,)]

@pytest.mark.parametrize("x", invalid_inputs)
def test_basic_errors(x):
    with pytest.raises(TypeError):
        my_abs(x)
    with pytest.raises(TypeError):
        my_trunc(x)
    with pytest.raises(TypeError):
        my_floor(x)
    with pytest.raises(TypeError):
        my_ceil(x)

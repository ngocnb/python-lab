import math
import pytest
from my_math.trig import my_sin, my_cos

# Test specific angles
angles = [
    0, 
    math.pi/6, 
    math.pi/4, 
    math.pi/3, 
    math.pi/2, 
    math.pi, 
    3*math.pi/2, 
    2*math.pi,
    -math.pi/4,
    10 # arbitrary large number
]

@pytest.mark.parametrize("x", angles)
def test_sin(x):
    assert math.isclose(my_sin(x), math.sin(x), rel_tol=1e-6)

@pytest.mark.parametrize("x", angles)
def test_cos(x):
    assert math.isclose(my_cos(x), math.cos(x), rel_tol=1e-6)

invalid_inputs = ["a", None, [1]]

@pytest.mark.parametrize("x", invalid_inputs)
def test_trig_type_errors(x):
    with pytest.raises(TypeError):
        my_sin(x)
    with pytest.raises(TypeError):
        my_cos(x)

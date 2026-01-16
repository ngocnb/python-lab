import math
import pytest
from my_math.power import my_pow, my_sqrt

pow_data = [
    (2, 3),
    (2, -3),
    (3, 2),
    (3, 0),
    (0.5, 2),
    (2, 0.5),
    (10, 2),
    (100, 0.5),
]


@pytest.mark.parametrize("x, y", pow_data)
def test_pow(x, y):
    # math.pow always returns float, so we cast my_pow result to float if needed implicitly or explicitly
    # But for strict comparison, let's see. math.pow(2,3) is 8.0.
    # Our implementation might eventually return integer 8 for integer inputs?
    # For now, let's check almost equal or type specific behavior.
    # Let's assume we want to mimic math.pow which returns float.
    print(f"math.pow: {math.pow(x, y)} ------ my_pow: {my_pow(x, y)}")
    assert math.isclose(my_pow(x, y), math.pow(x, y), rel_tol=1e-9)


# sqrt_data = [0, 1, 4, 9, 2, 0.5, 12345.6789]


# @pytest.mark.parametrize("x", sqrt_data)
# def test_sqrt(x):
#     assert math.isclose(my_sqrt(x), math.sqrt(x), rel_tol=1e-9)


# invalid_inputs = ["a", None, [1]]


# @pytest.mark.parametrize("x", invalid_inputs)
# def test_sqrt_type_errors(x):
#     with pytest.raises(TypeError):
#         my_sqrt(x)


# def test_pow_type_errors(x):
#     with pytest.raises(TypeError):
#         my_pow(x, 2)
#     with pytest.raises(TypeError):
#         my_pow(2, x)


# def test_sqrt_domain_error():
#     with pytest.raises(ValueError):
#         my_sqrt(-1)


# def test_pow_domain_error():
#     with pytest.raises(ValueError):
#         my_pow(-1, 0.5)

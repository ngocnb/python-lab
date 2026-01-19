import math
import pytest
from my_math.exp import my_exp


@pytest.mark.parametrize(
    "x",
    [
        0.5,  # Small positive
        -0.5,  # Small negative
        2,  # Medium positive
        -2,  # Medium negative
        5,  # Larger positive
        -5,  # Larger negative
        0.1,  # Very small positive
        -0.1,  # Very small negative
        2.718281828459045,  # ln(e)
        0.001,  # Extremely small positive
        -0.001,  # Extremely small negative
        100,  # Very large positive
        -100,  # Very large negative
    ],
    ids=[
        "small_positive",
        "small_negative",
        "medium_positive",
        "medium_negative",
        "larger_positive",
        "larger_negative",
        "very_small_positive",
        "very_small_negative",
        "ln_e",
        "extremely_small_positive",
        "extremely_small_negative",
        "very_large_positive",
        "very_large_negative",
    ],
)
def test_exp(x):
    assert math.isclose(my_exp(x), math.exp(x), rel_tol=1e-9)


# Test special cases
def test_exp_zero():
    assert my_exp(0) == 1.0


def test_exp_one():
    assert math.isclose(my_exp(1), math.e, rel_tol=1e-9)


def test_exp_negative_one():
    assert math.isclose(my_exp(-1), 1 / math.e, rel_tol=1e-9)


# Test error handling
invalid_inputs = ["a", None, [1], (1,)]


@pytest.mark.parametrize(
    "x",
    invalid_inputs,
    ids=[
        "string",
        "none",
        "list",
        "tuple",
    ],
)
def test_exp_errors(x):
    with pytest.raises(TypeError):
        my_exp(x)

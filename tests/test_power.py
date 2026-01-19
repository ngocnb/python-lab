import math
import pytest
from my_math.power import my_pow, my_sqrt


@pytest.mark.parametrize(
    "x, y",
    [
        (2, 3),  # Basic positive integer power
        (2, -3),  # Negative integer power
        (3, 2),  # Another basic case
        (3, 0),  # Zero power
        (0.5, 2),  # Fractional base
        (2, 0.5),  # Fractional exponent
        (10, 2),  # Larger numbers
        (100, 0.5),  # Square root case
        (1, 5),  # Base of 1
        (5, 1),  # Exponent of 1
        (-2, 3),  # Negative base, odd exponent
        (-2, 2),  # Negative base, even exponent
        (0, 5),  # Zero base
    ],
    ids=[
        "basic_positive",
        "negative_exponent",
        "basic_case_2",
        "zero_exponent",
        "fractional_base",
        "fractional_exponent",
        "larger_numbers",
        "square_root_case",
        "base_one",
        "exponent_one",
        "negative_base_odd",
        "negative_base_even",
        "zero_base",
    ],
)
def test_pow(x, y):
    assert math.isclose(my_pow(x, y), math.pow(x, y), rel_tol=1e-9)


@pytest.mark.parametrize(
    "x",
    [
        0,
        1,
        4,
        9,
        2,
        0.5,
        12345.6789,
    ],
    ids=[
        "zero",
        "one",
        "perfect_square_4",
        "perfect_square_9",
        "irrational_2",
        "fractional",
        "large_number",
    ],
)
def test_sqrt(x):
    assert math.isclose(my_sqrt(x), math.sqrt(x), rel_tol=1e-9)


@pytest.mark.parametrize(
    "x",
    ["a", None, [1], (1,)],
    ids=[
        "string",
        "none",
        "list",
        "tuple",
    ],
)
def test_pow_type_errors(x):
    with pytest.raises(TypeError):
        my_pow(x, 2)
    with pytest.raises(TypeError):
        my_pow(2, x)


@pytest.mark.parametrize(
    "x",
    ["a", None, [1], (1,)],
    ids=[
        "string",
        "none",
        "list",
        "tuple",
    ],
)
def test_sqrt_type_errors(x):
    with pytest.raises(TypeError):
        my_sqrt(x)


def test_sqrt_domain_error():
    with pytest.raises(ValueError):
        my_sqrt(-1)


def test_pow_domain_error():
    with pytest.raises(ValueError):
        my_pow(-1, 0.5)


def test_pow_edge_cases():
    # Test very small numbers
    assert math.isclose(my_pow(0.001, 2), math.pow(0.001, 2), rel_tol=1e-9)
    # Test very large numbers
    assert math.isclose(my_pow(1000, 2), math.pow(1000, 2), rel_tol=1e-9)

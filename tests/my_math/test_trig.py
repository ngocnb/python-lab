import math
import pytest
from my_math.trig import my_sin, my_cos

# Common test data for both sin and cos
trig_test_data = [
    (0, "zero"),
    (math.pi / 6, "thirty_degrees"),
    (math.pi / 4, "forty_five_degrees"),
    (math.pi / 3, "sixty_degrees"),
    (math.pi / 2, "ninety_degrees"),
    (math.pi, "one_eighty_degrees"),
    (3 * math.pi / 2, "two_seventy_degrees"),
    (2 * math.pi, "three_sixty_degrees"),
    (-math.pi / 4, "negative_forty_five"),
    (-math.pi / 2, "negative_ninety"),
    (math.pi / 12, "fifteen_degrees"),
    (5 * math.pi / 6, "one_fifty_degrees"),
    (10, "large_positive"),
    (-10, "large_negative"),
    (0.001, "very_small_positive"),
    (-0.001, "very_small_negative"),
]


@pytest.mark.parametrize(
    "x",
    [data[0] for data in trig_test_data],
    ids=[data[1] for data in trig_test_data],
)
def test_sin(x):
    print(f"my_sin({x}) = {my_sin(x)} --------- math.sin({x}) = {math.sin(x)}")
    assert math.isclose(my_sin(x), math.sin(x), rel_tol=1e-9)


# @pytest.mark.parametrize(
#     "x",
#     [data[0] for data in trig_test_data],
#     ids=[data[1] for data in trig_test_data],
# )
# def test_cos(x):
#     assert math.isclose(my_cos(x), math.cos(x), rel_tol=1e-9)


# @pytest.mark.parametrize(
#     "x",
#     ["a", None, [1], (1,)],
#     ids=[
#         "string",
#         "none",
#         "list",
#         "tuple",
#     ],
# )
# def test_sin_type_errors(x):
#     with pytest.raises(TypeError):
#         my_sin(x)


# @pytest.mark.parametrize(
#     "x",
#     ["a", None, [1], (1,)],
#     ids=[
#         "string",
#         "none",
#         "list",
#         "tuple",
#     ],
# )
# def test_cos_type_errors(x):
#     with pytest.raises(TypeError):
#         my_cos(x)


# # Test special trigonometric identities
# def test_trig_identities():
#     # Test sin²(x) + cos²(x) = 1
#     test_angles = [0, math.pi / 4, math.pi / 2, math.pi, 1.234, -0.567]
#     for angle in test_angles:
#         sin_val = my_sin(angle)
#         cos_val = my_cos(angle)
#         assert math.isclose(sin_val**2 + cos_val**2, 1.0, rel_tol=1e-9)


# def test_trig_symmetry():
#     # Test odd/even properties
#     # sin(-x) = -sin(x) (odd function)
#     # cos(-x) = cos(x) (even function)
#     test_angles = [math.pi / 6, math.pi / 4, math.pi / 3, 1.234]
#     for angle in test_angles:
#         assert math.isclose(my_sin(-angle), -my_sin(angle), rel_tol=1e-9)
#         assert math.isclose(my_cos(-angle), my_cos(angle), rel_tol=1e-9)


# def test_trig_periodicity():
#     # Test 2π periodicity
#     # sin(x + 2π) = sin(x)
#     # cos(x + 2π) = cos(x)
#     test_angles = [0, math.pi / 4, math.pi / 2, 1.234]
#     for angle in test_angles:
#         assert math.isclose(my_sin(angle + 2 * math.pi), my_sin(angle), rel_tol=1e-9)
#         assert math.isclose(my_cos(angle + 2 * math.pi), my_cos(angle), rel_tol=1e-9)

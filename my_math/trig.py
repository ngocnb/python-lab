from my_math.basic import my_abs
import math


def my_sin(x):
    """
    Returns the sine of x (measured in radians).
    """

    if x == 0:
        return 0

    """
    Range reduction
    - This keeps x between 0 and 2*PI
    - Also solve the problem with infinite PI number
    """
    x = x % (2 * math.pi)
    print(f"x = {x}")

    """
    formula: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    """
    n = 1
    term = x
    threshold = 1e-18
    total = x
    positive = 1

    while my_abs(term) > threshold:
        n += 2
        positive = -1 if positive > 0 else 1
        term = term * x * x / (n * (n - 1))
        total += positive * term

    return total


def my_cos(x):
    """
    Returns the cosine of x (measured in radians).
    """
    pass

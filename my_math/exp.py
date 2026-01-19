from my_math.basic import my_abs


def my_exp(x):
    """
    Calculate e^x using Taylor series expansion.

    Args:
        x (int or float): The exponent value

    Returns:
        float: e raised to the power of x

    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x is not a number")

    """
    LOGIC FOR my_exp(x):
    --------------------
    1. Setup:
    - Identity: e^x = 1 + x/1! + x^2/2! + x^3/3! + ...
    - Handle negative x: 
        If x < 0, calculate exp(abs(x)) first, then return 1 / result.

    2. Variables to initialize:
    - total: 1.0 (This is the very first term of the series)
    - term: 1.0  (The value of the current term to be added)
    - n: 1       (The counter for the factorial and power)
    - threshold: 1e-10

    3. Loop (while abs(term) > threshold):
    - term = term * x / n  (Efficiently calculates the next term in the series)
    - total += term
    - n += 1

    4. Result:
    - If original x was negative, return 1 / total
    - Else, return total
    """

    is_negative = x < 0
    x = my_abs(x)
    total = 1.0
    term = 1.0
    n = 1
    threshold = 1e-10

    if x == 0:
        return total

    while my_abs(term) > threshold:
        term = term * x / n
        total += term
        n += 1

    return 1 / total if is_negative else total

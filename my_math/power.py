from my_math.exp import my_exp
from my_math.log import my_log


def my_pow(x, y):
    """
    Returns x raised to the power y.
    """
    result = 1

    if y >= 1:
        while y > 0:
            result *= x
            y -= 1

        return result
    if y == 0:
        return result
    if y < 0:
        """
        x^(-y) = 1 / x^y
        """
        result = my_pow(x, y * -1)
        return 1 / result
    if 0 < y and y < 1:
        """
        x^(y) = exp^(y * log(x))
        """
        result = my_exp(y * my_log(x))

    return result


def my_sqrt(x):
    """
    Returns the square root of x.
    """
    if x == 0:
        return 0
    return my_pow(x, 0.5)

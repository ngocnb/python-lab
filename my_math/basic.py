def my_abs(x):
    """
    Returns the absolute value of x.
    """
    return x if x > 0 else x * -1


def my_trunc(x):
    """
    Returns x truncated to an integer (towards 0).
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    s = str(x)
    s = s.split(".")
    result = int(s[0])
    return result


def my_floor(x):
    """
    Returns the largest integer <= x.
    """
    result = my_trunc(x)
    return result if result == x or x >= 0 else result - 1


def my_ceil(x):
    """
    Returns the smallest integer >= x.
    """
    result = my_trunc(x)
    if result == x:
        return result
    
    return result if x < 0 else result + 1

from my_math.basic import my_abs


def my_log(x):
    """
    Returns the log of x.
    LOGIC FOR my_log(x):
    --------------------
    1. Setup:
    - We use the formula: ln(x) = 2 * [ A + (A^3)/3 + (A^5)/5 + ... ]
    - Constant Base (A): (x - 1) / (x + 1)

    2. Variables to initialize:
    - total: 0 (to store the sum of the series)
    - n: 1 (the odd denominator and exponent)
    - current_term: Calculation for the first term where n=1
    - threshold: 1e-10 (our precision limit)

    3. Loop (while current_term > threshold):
    - Add current_term to total
    - Increment n by 2 (to get the next odd number: 1, 3, 5...)
    - Calculate the next current_term: (1/n) * (A**n)

    4. Result:
    - Return 2 * total
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x is not a number")

    if x <= 0:
        raise ValueError("log domain error: x must be positive")
    """
    Range reduction:
    - If x < 0.5, repeatedly multiply x by 2 and decrement k until x is in [0.5, 2].
    - If x > 2, repeatedly divide x by 2 and increment k until x is in [0.5, 2].
    - Then use: log(x) = log(reduced_x) + k * log(2)

    Why range reduction?
    - The Taylor series converges faster for values of x close to 1.
    - By reducing x to the range [0.5, 2], we ensure better convergence and accuracy.

    Without range reduction, the series would converge very slowly for values of x far from 1,
    leading to poor accuracy and increased computation time.

    Example of failed convergence without range reduction:
        when x = 0.01
        with rel_tol = 0.000000001, the assert will failed
        assert math.isclose(my_log(x), math.log(x), rel_tol=0.000000001)
        my_log(x) = -4.605170181258784 ----- math.log = -4.605170185988091
        with rel_tol = 0.00000001, it will be fine 
    """
    if x < 0.5:
        k = 0
        while x < 0.5:
            x *= 2
            k -= 1

        return my_log(x) + k * my_log(2)

    if x > 2:
        k = 0
        while x > 2:
            x /= 2
            k += 1

        return my_log(x) + k * my_log(2)

    A = (x - 1) / (x + 1)
    square_A = A * A
    total = 0
    n = 1
    current_term = A
    temp_term = A
    threshold = 1e-10

    """
    - We use the formula: ln(x) = 2 * [ A + (A^3)/3 + (A^5)/5 + ... ]
    - Constant Base (A): (x - 1) / (x + 1)
    - Current Term = (A^n) / n
    """
    while my_abs(current_term) > threshold:
        total += current_term
        n += 2
        temp_term = temp_term * square_A
        current_term = temp_term / n

    return total * 2

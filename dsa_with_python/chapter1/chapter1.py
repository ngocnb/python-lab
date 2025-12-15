def is_multiple(n, m):
    """Check if n is a multiple of m.

    Args:
        n (int): The number to check.
        m (int): The potential multiple.
    
    Returns:
        bool: True if n is a multiple of m, False otherwise.
    """

    try:
        return n % m == 0
    except Exception as e:
        print("Error message:", e)
        return False

def is_even(n):
    """ Check if n is even or not without using mutiplication, modulo or division operators.

    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if n is even, False otherwise.
    """

    try:
        n = abs(n)    # get the absolute value, for dealing with negative case also

        while n > 1:
            n = n - 2
        
        return n == 0
    except Exception as e:
        print("Error message:", e)
        return False

def is_even_bitwise(n):
    """ Check if n is even or not using bitwise operator.

    Args:
        n (int): The number to check.

    Explaining:
        An even number in binary representation always has its least significant bit (LSB) as 0.
        An odd number always has its LSB as 1.
        By performing a bitwise AND operation between the number and 1 (n & 1), we can determine
        the parity of the number:
            - If the result is 0, the number is even.
            - If the result is 1, the number is odd.
    
    Returns:
        bool: True if n is even, False otherwise.
    """

    try:
        return (n & 1) == 0
    except Exception as e:
        print("Error message:", e)
        return False

def minmax(data):
    """ Return the minimum and maximum values from a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        tuple: A tuple containing the minimum and maximum values.
        bool: False if exception is raised
    """

    try:
        min = max = data[0]
    
        for n in data:
            if min > n:
                min = n
            if max < n:
                max = n
        
        return min, max
    except Exception as e:
        print("Error message:", e)
        return False

def sum_numbers(n):
    """ Return the sum of all numbers from 1 to n - 1.

    Args:
        n (int): The upper limit number.

    Returns:
        int: The sum of all numbers from 1 to n - 1.
        bool: False if exception is raised
    """

    try:
        sum = 0

        n = int(n)  # cast n to integer

        for l in range(n):
            sum += l
        
        return sum
    except Exception as e:
        print ("Error message:", e)
        return False

def sum_numbers_gaussian_formula(n):
    """ Return the sum of all numbers from 1 to n - 1.

    Args:
        n (int): The upper limit number.

    Returns:
        int: The sum of all numbers from 1 to n - 1.
        bool: False if exception is raised
    """

    try:
        n = int(n)
        if n <= 0:
            return 0

        return n * (n - 1) / 2
    except Exception as e:
        print("Error message:", e)
        return False
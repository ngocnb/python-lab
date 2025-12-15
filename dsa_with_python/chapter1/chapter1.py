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

import pytest
import random
from unittest.mock import patch

from chapter1 import random_choice 

# --- 1. Test the Happy Path (Result must be in the input list) ---

def test_result_is_in_data():
    """
    Verifies that the element returned by the function is one of the elements 
    present in the original list, regardless of which element is chosen.
    """
    data = range(1000)
    result = random_choice(data)
    # --- Debugging Print Statement ---
    print(f"DATA USED: {data}, RESULT OBTAINED: {result}")
    assert result in data


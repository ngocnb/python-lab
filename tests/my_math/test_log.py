import math
import pytest
from my_math.log import my_log

# Test various positive values for log
log_test_data = [0.1, 0.5, 1, 2, 10, 100, math.e, math.pi, 1.5, 0.01]


@pytest.mark.parametrize("x", log_test_data)
def test_log(x):
    my_result = my_log(x)
    expected = math.log(x)
    print(f"my_log(x) = {my_result} ----- math.log = {expected}")
    assert math.isclose(my_log(x), math.log(x), rel_tol=1e-9)


invalid_inputs = ["a", None, [1], (1,)]


@pytest.mark.parametrize("x", invalid_inputs)
def test_log_type_errors(x):
    with pytest.raises(TypeError):
        my_log(x)


domain_error_inputs = [0, -1, -0.5, -10]


@pytest.mark.parametrize("x", domain_error_inputs)
def test_log_domain_errors(x):
    with pytest.raises(ValueError):
        my_log(x)

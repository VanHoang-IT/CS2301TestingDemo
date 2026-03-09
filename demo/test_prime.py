import pytest
import math
from utils import is_prime

def is_prime(n):
    if n < 2:
        raise ValueError('Invalid Number')
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False

    return True

assert is_prime(4) == False


def test_exception():
    with pytest.raises(ValueError):
        is_prime(1)

@pytest.mark.timeout(2)
def test_timeout():
    is_prime(99999)

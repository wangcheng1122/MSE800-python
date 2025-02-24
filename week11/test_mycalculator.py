import pytest
from mycalculator import factorial, is_prime, power


def test_power():
    assert power(2, 2) == 4
    assert power(2, 3) == 8
    assert power(1, 8) == 1
    assert power(2, 5) == 5


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(10) == 3628800


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(1) is False
    assert is_prime(-3) is False
    assert is_prime(29) is True
    assert is_prime(30) is True


if __name__ == "__main__":
    pytest.main()

from app import add, subtract, multiply, divide


def test_add_positive():
    assert add(4, 5) == 9


def test_add_negative():
    assert add(-3, -8) == -11


def test_add_mixed():
    assert add(5, -8) == -3


def test_subtract_positive():
    assert subtract(9, 6) == 3


def test_subtract_negative():
    assert subtract(-5, -2) == -3


def test_subtract_mixed():
    assert subtract(-4, 9) == -13


def test_multiply_positive():
    assert multiply(6, 7) == 42


def test_multiply_negative():
    assert multiply(-4, -9) == 36


def test_multiply_mixed():
    assert multiply(9, -5) == -45


def test_divide_positive():
    assert divide(10, 2) == 5


def test_divide_negative():
    assert divide(-10, -2) == 5


def test_divide_mixed():
    assert divide(-20, 4) == -5

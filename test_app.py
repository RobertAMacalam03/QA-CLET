from app import add, subtract, multiply, divide


def test_add_positive():
    assert add(4, 5) == 9


def test_add_negative():
    assert add(-3, -8) == -11

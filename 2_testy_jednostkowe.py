def add(x, y):
    return x + y


def product(x, y):
    return x*y


def test_add():
    assert add(7, 3) == 10
    assert add(7, -1) == 6
    assert add(4.3, 5.6) - 9.9 < 0.0000001


def test_product():
    assert product(0, 0) == 0
    assert product(-1, 0) == 0
    assert product(-1, -1) == 1
    assert product(5, 0) == 0
    assert product(3, 4) == 12



test_add()
test_product()

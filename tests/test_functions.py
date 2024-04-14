from src.math_package import add, substract

def test_add():
    assert add(1,3) == 4
    assert add(2,3) == 5


def test_subtract():
    assert substract(5,3) == 2
    assert substract(2,1) == 1
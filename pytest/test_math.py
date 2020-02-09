# Unit Testing Extensions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def inc(x):
    return x + 1


# Unit Testing Enviroment

def test_subtract():
    assert subtract(3, 2) == 1


def test_add():
    assert add(1, 2) == 3


def test_inc():
    assert inc(2) == 3

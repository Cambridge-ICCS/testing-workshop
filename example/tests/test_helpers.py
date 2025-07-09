from helpers import square
from math import nan, isnan


def test_square():
    assert square(0) == 0
    assert square(1) == 1
    assert square(4) == 16
    assert square(-3) == 9
    assert isnan(square(nan))


def test_inv():
    assert square(4) ** (0.5) == 4

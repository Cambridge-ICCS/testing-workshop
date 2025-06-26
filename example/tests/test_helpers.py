from helpers import square, linspace
from math import nan, isnan
import pytest
import numpy as np

def test_square():
    assert square(0) == 0
    assert square(1) == 1
    assert square(4) == 16
    assert square(-3) == 9
    assert isnan(square(nan))

def test_inv():
    assert square(4)**(0.5) == 4

@pytest.mark.parametrize("value, expected", [
  ((0, 0, 0), [])
  ,((10, 10, 0), [])
  ,((10, 100, 0), [])
  ,((0, 1, 2), [0, 1])
  ])
def test_linspace(value, expected):
    assert linspace(*value) == np.array(expected)
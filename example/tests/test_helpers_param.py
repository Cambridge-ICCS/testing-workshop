from helpers import square
from math import nan, isnan
import pytest

def test_square_nan():
    assert isnan(square(nan))

@pytest.mark.parametrize("value, expected", [
    (0, 0),
    (1, 1),
    (4, 16),
    (-1, 1),
])
def test_square_parametrized(value, expected):
    assert square(value) == expected

@pytest.mark.parametrize("value, expected", [
  ((0, 0, 0), [])
  ,((10, 10, 0), [])
  ,((10, 100, 0), [])
  ,((0, 1, 2), [0, 1])
  ])
def test_linspace(value, expected):
    assert linspace(*value) == np.array(expected)
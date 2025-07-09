from helpers import square, linspace
import numpy as np
from math import nan, isnan
import pytest

# Will be needed for the property-based tests
from hypothesis import given
from hypothesis.strategies import floats, composite


def test_square_nan():
    assert isnan(square(nan))


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0),
        (1, 1),
        (4, 16),
        (-1, 1),
    ],
)
def test_square_parametrized(value, expected):
    assert square(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ((0, 0, 0), [])
     , ((10, 10, 0), [])
     , ((10, 100, 0), [])
     , ((0, 1, 2), [0, 1])
    ],
)
def test_linspace(value, expected):
    # test equality of the two arrays
    assert np.array_equal(linspace(*value), np.array(expected))


# Uncomment for "property-based testing" exercises 2-4
#
# @given(...)
# def test_linspace_property(...):
#     # Write your property here
#     pass

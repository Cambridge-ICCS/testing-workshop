from hypothesis import given
from hypothesis.strategies import floats, lists, composite
from observation import mean_squared_error
import numpy as np

# We have
# ... def mean_squared_error(model : ndarray, observed : ndarray) -> float:

# Composite strategies


@composite
def myfloat(draw):
    return draw(
        floats(allow_infinity=False, allow_nan=False, min_value=-1e10, max_value=1e10)
    )


@composite
def lists_of_same_length(draw):
    pass


# Tests


# What is the MSE if both inputs are the same?
@given(lists(floats(allow_infinity=False, allow_nan=False)))
def test_msqerror_self(input_data):
    pass

# MSE should always be positive, and the operation should be commutative
@given(lists_of_same_length())
def test_msqerror_more(input_data):
    pass

# What happens when you scale both the model and observation data by a known constant?
@given(lists_of_same_length(), myfloat())
def test_msqerror_invariance(input_data, scale):
    pass

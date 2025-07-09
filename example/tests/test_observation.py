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
    list1 = draw(lists(myfloat()))
    list2 = draw(lists(myfloat(), min_size=len(list1), max_size=len(list1)))
    return list1, list2


# Tests


@given(lists(floats(allow_infinity=False, allow_nan=False)))
def test_msqerror_self(input_data):
    assert mean_squared_error(input_data, input_data) == 0


@given(lists_of_same_length())
def test_msqerror_more(input_data):
    # positivity
    model_data, obs_data = input_data
    assert mean_squared_error(model_data, obs_data) >= 0
    # commutativity
    assert mean_squared_error(obs_data, model_data) == mean_squared_error(
        model_data, obs_data
    )


@given(lists_of_same_length(), myfloat())
def test_msqerror_invariance(input_data, scale):
    # Scale invariance
    model_data, obs_data = input_data

    model_data_scaled = scale * np.array(model_data)
    obs_data_scaled = scale * np.array(obs_data)
    mse_scaled = mean_squared_error(model_data_scaled, obs_data_scaled)

    scaled_mse = scale**2 * mean_squared_error(model_data, obs_data)

    assert np.isclose(mse_scaled, scaled_mse)

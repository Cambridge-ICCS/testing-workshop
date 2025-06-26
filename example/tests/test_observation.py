from hypothesis import given
from hypothesis.strategies import floats, lists, composite
from observation import mean_squared_error
import numpy as np

@composite
def myfloats(draw):
   return draw(floats(max_value = 1E10, min_value = -1E10))

@composite
# Generate two lists of the same length
def same_len_float_lists(draw):
    list1 = draw(lists(myfloats()))
    list2 = draw(lists(myfloats(),
        min_size=len(list1),
        max_size=len(list1)
    ))
    return (list1, list2)

@given(lists(floats(allow_infinity=False, allow_nan=False)))
def test_msqerror_self(input_data):
  # No error on self
  assert mean_squared_error(input_data, input_data) == 0

@given(same_len_float_lists())
def test_msqerror_(input_data):
  model_data, obs_data = input_data
  # Positive
  assert mean_squared_error(model_data, obs_data) >= 0
  # Commutativity
  assert mean_squared_error(model_data, obs_data) == mean_squared_error(obs_data, model_data)

@given(same_len_float_lists(), myfloats())
def test_msqerror_invariance(input_data, scale):
  model_data, obs_data = input_data
  model_data = np.array(model_data)
  obs_data   = np.array(obs_data)
  scale = scale + 0.1 # avoid 0 
  # Scale invariance
  scaled_mse = (scale**2) * mean_squared_error(model_data, obs_data)
  mse_scaled = mean_squared_error(scale * model_data, scale * obs_data)
  assert np.isclose(scaled_mse, mse_scaled)

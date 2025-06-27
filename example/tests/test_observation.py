from hypothesis import given
from hypothesis.strategies import floats, lists, composite
from observation import mean_squared_error
import numpy as np


# lists(floats(allow_infinity=False, allow_nan=False))

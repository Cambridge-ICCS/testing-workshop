from energy_balance import temperature_at_energy_balance
from numpy import ndarray

def mean_squared_error(model : ndarray, observed : ndarray) -> float:
  n = len(observed)
  if len(model) != len(observed):
    raise(ValueError("Model length and observation length should match"))
  else:
    if n == 0:
      return 0
    else:
      sum = 0
      for m, o in zip(model, observed):
        sum += (m - o)**2
      return (1/n) * sum

observed = [(0.3, 15.5), (0.4, 20.0)]
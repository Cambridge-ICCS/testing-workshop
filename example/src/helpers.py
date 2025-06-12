def square(x : float) -> float:
  return (x ** 2.0)

def linspace(start: float, stop: float, num: int) -> list[float]:
    """
    Generate a list of evenly spaced numbers over a specified range.

    Input:
    - start: float, the starting value of the sequence
    - stop: float, the end value of the sequence
    - num: int, number of samples to generate

    Output:
    - list[float], a list of evenly spaced numbers
    """
    return [start + i * (stop - start) / (num - 1) for i in range(num)]
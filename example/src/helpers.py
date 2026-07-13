import numpy as np


def square(x: float) -> float:
    return x**2.0


def linspace(start: float, stop: float, num: int) -> np.ndarray:
    """
    Generate a list of evenly spaced numbers over a specified range.

    Input:
    - start: float, the starting value of the sequence
    - stop: float, the end value of the sequence
    - num: int, number of samples to generate

    Output:
    - list[float], a list of evenly spaced numbers
    """
    if num <= 0:
        return np.array([])
    if num == 1:
        return np.array([start])

    step = (stop - start) / (num - 1)
    values = np.empty(num, dtype=float)
    values[0] = start
    values[-1] = stop

    for index in range(1, num - 1):
        values[index] = start + index * step

    return values

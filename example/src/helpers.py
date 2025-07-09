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
    return np.array([start + i * (stop - start) / (num - 1) for i in range(num)])

import energy_balance
import observation
from helpers import linspace

import pytest
from hypothesis import given
from hypothesis.strategies import floats, integers, tuples, lists, composite

import numpy as np

## Unit testing exercises

### Question 2

def test_temp_at_extreme(setup):
    assert energy_balance.temperature_at_energy_balance(1, 0.1) == 0

### Question 3

def test_temp_at_point(setup):
    assert energy_balance.temperature_at_energy_balance(0.5, 0.1) == pytest.approx(416.88, rel=1e-4)

### Question 4

@pytest.mark.parametrize(
        "albedo, expected",
        [
              (1, 0)
            , (0.5, 416.88)
        ]
)
def test_temp_parm(setup, albedo, expected):
    assert energy_balance.temperature_at_energy_balance(albedo, 0.1) == pytest.approx(expected, rel=1e-4)

### Question 5

# We would want more tests than this, but this would improve the coverage
def test_energy_out(setup):
    assert energy_balance.energy_out(0) == 0

## Property-based testing exercises

## Question 1

@given(temperature = floats(min_value = 0, max_value = 1E20))
def test_energy_out_property(temperature):
    # Using fixtures with `hypothesis` based tests requires a bit more work
    # so you can just use initialization directly
    energy_balance.init()
    # Put your property based test here
    assert energy_balance.energy_out(temperature) >= 0.0

## Question 2

# Generate two lists of the same length
@composite
def same_len_float_lists(draw):
    list1 = draw(lists(floats(allow_infinity=False, allow_nan=False, min_value=-1e10, max_value=1e10)))
    list2 = draw(lists(
        floats(
            allow_infinity=False, 
            allow_nan=False, 
            min_value=-1e10, 
            max_value=1e10
        ),
        min_size=len(list1),
        max_size=len(list1)
    ))
    return (list1, list2)

@given(same_len_float_lists())
def test_msqerror2(input_data):
    model_data, obs_data = input_data
    assert observation.mean_squared_error(model_data, obs_data) >= 0.0

## Potential answers...

## Question 3

@given(tuples(floats(allow_infinity=False,allow_nan=False), integers(min_value=2,max_value=1000)))
def test_linspace_property(inp):
    starter, count = inp
    ender = starter + 10
    # Write your property here
    space = linspace(starter,ender,count)
    assert space[0] == starter
    assert space[-1] == ender

## Question 4

@given(tuples(floats(allow_infinity=False,allow_nan=False), integers(min_value=2,max_value=1000)))
def test_linspace_size(inp):
    ender, counter = inp
    space = linspace(0, ender, counter)
    assert len(space) == counter

## Question 5

@given(tuples(floats(allow_infinity=False,allow_nan=False), integers(min_value=2,max_value=1000)))
def test_linspace_mirror(inp):
    ender, counter = inp
    space1 = linspace(0, ender, counter)
    space2 = linspace(ender, 0, counter)
    assert np.allclose(space1, np.flip(space2), rtol=1e-4)
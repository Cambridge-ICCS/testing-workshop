import energy_balance
from helpers import linspace

import pytest
from hypothesis import given
from hypothesis.strategies import floats, integers, tuples

## Unit testing exercises

## Question 2


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

## Potential answers...

@given(tuples(floats(allow_infinity=False,allow_nan=False), integers(min_value=2,max_value=1000)))
def test_linspace_property(inp):
    starter, count = inp
    ender = starter + 10
    # Write your property here
    space = linspace(starter,ender,count)
    assert space[0] == starter
    assert space[-1] == ender

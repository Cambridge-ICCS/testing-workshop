import energy_balance
from testing import setup
import pytest
from math import pi

from hypothesis import given
from hypothesis.strategies import floats

def test_energy_in_albedo_max(setup):
    assert energy_balance.energy_in(1) == 0

def test_energy_in_albedo_zero(setup):
    assert (energy_balance.energy_in(0)
               == energy_balance.solar_constant * (pi * energy_balance.mean_radius**2)), "energy_in function failed for albedo 0"

def test_energy_in_invalid(setup):
    albedo = -0.1
    with pytest.raises(ValueError):
        energy_balance.energy_in(albedo)

def test_energy_in(setup):
    assert energy_balance.energy_in(0.5) == 87348540814.55124

def test_emissivity(setup):
    assert energy_balance.earth_emissivity(0.3, 288) == pytest.approx(0.614618, abs=1e-4)

def test_balance_temperate(setup):
    # Exercise
    pass


# Uncomment for "property-based testing" exercise 1
#
# @given(...)
# def test_energy_out_property():
#     # Note that we cannot use fixtures in `hypothesis` based tests
#     energy_balance.init()
#     # Put your property based test here
#     ...

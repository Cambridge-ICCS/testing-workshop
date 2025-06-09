import energy_balance
import pytest

def test_energy_in_albedo_zero():
    albedo = 0
    assert energy_balance.energy_in(0) == energy_balance.solar_constant * (energy_balance.pi * energy_balance.earth_radius**2), "energy_in function failed for albedo 0"

def test_energy_in_albedo_max():
    albedo = 1
    assert energy_balance.energy_in(1) == 0, "energy_in function failed for albedo 1"

def test_energy_in_invalid():
    albedo = -0.1
    with pytest.raises(ValueError):
        energy_balance.energy_in(albedo)

def test_balance_temperate():
    albedo = 0.3
    temperature = energy_balance.temperature_of_balanced_system(albedo)
    assert energy_balance.temperature_at_energy_balance(albedo, 1) == pytest.approx(255.00218, abs=1e-5), "energy_balance function failed for temperate Earth"

def test_emissivity():
    assert energy_balance.earth_emissivity(0.3, 288) == pytest.approx(0.614618, abs=1e-4)


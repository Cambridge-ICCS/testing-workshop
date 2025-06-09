from typing import Annotated
from math import pi
import numpy as np

## Constants

# Solar Constant: amount of energy the Earth receives from the Sun every second per square metre 
solar_constant : Annotated[float, "J s^-1 m^-2"] = 1370.0

# Stefan-Boltzmann's constant
sigma : Annotated[float, "J s^-1 m^-2 K^-4"] = 5.67e-8

# (Mean) radius of the Earth
earth_radius : Annotated[float, "m"] = 6.371e3

## Energy balance calculations

def energy_in(albedo : float) -> Annotated[float, "J / s"]:
    """
        Calculate the incoming energy from the sun 
        to the earth system as a function of the Earth's albedo

        Input:
        - albedo: float, the fraction of solar energy reflected by the Earth (0 to 1)
        Output:
        - float, the incoming energy in watts (J / s)
    """
    if albedo < 0 or albedo > 1:
        raise ValueError("Albedo must be between 0 and 1")
        
    illuminated_surface_area = pi * earth_radius**2  
    return (solar_constant * illuminated_surface_area * (1 - albedo))

def energy_out(temperature : Annotated[float, "K"]) -> Annotated[float, "J / s"]:
    """
        Calculate the outgoing energy from the Earth system due to
        IR emission back into space, as a function of the Earth's temperature,
        assuming it behaves like a black body emitter.

        Input:
        - temperature: float, the average temperature of the Earth in Kelvin
        Output:
        - float, the outgoing energy in watts (J / s)
    """
    emmiting_surface_area = 4 * pi * earth_radius**2
    return (sigma * temperature**4 * emmiting_surface_area)

def temperature_of_balanced_system(albedo: float) -> Annotated[float, "K"]:
    """
        Calculate the temperature of the Earth system when it is in energy balance,
        given a specific albedo.

        Input:
        - albedo: float, the fraction of solar energy reflected by the Earth (0 to 1)
        Output:
        - float, the temperature in Kelvin
    """
    incoming_energy = energy_in(albedo)
    return ((incoming_energy / (sigma * 4 * pi * earth_radius**2)) ** 0.25)


def earth_emissivity(albedo: float, temperature: Annotated[float, "K"]) -> float:
    """
      Calculate the emissivty of the body (i.e., the proption of black-body
      radiation that actually leaves the body)

      Input:
      - albedo: float, the fraction of solar energy reflected by the Earth (0 to 1)
      - temperature: float, the average temperature of the Earth in Kelvin
      Output:
      - float, the emissivity of the Earth (dimensionless)
    """
    return (solar_constant * (1 - albedo))/(4 * sigma  * temperature**4)

def temperature_at_energy_balance(albedo: float, emissivity: float) -> Annotated[float, "K"]:
    """
        Assume energy balance, calculate the temperature of the Earth given
        albedo and emissivity:

        Input:
        - albedo: float, the fraction of solar energy reflected by the Earth (0 to 1)
        - emissivity: float, the emissivity of the Earth (dimensionless)
        Output:
        - float, the net energy balance in watts (J / s)
    """
    return ((solar_constant * (1 - albedo)) / (4 * sigma * emissivity)) ** 0.25

def kelvin_to_celsius(temperature: Annotated[float, "K"]) -> Annotated[float, "C"]:
    """
        Convert temperature from Kelvin to Celsius.

        Input:
        - temperature: float, the temperature in Kelvin
        Output:
        - float, the temperature in Celsius
    """
    return temperature - 273.15

def plot_temperature_vs_emissivity():
    """
        Plot the temperature of the Earth as a function of emissivity
        for a fixed albedo.
    """
    import matplotlib.pyplot as plt
    epsilon_var = np.linspace(0.5, 0.7, 50)
    albedo = 0.3

    temperatures = kelvin_to_celsius(temperature_at_energy_balance(albedo, epsilon_var))
    
    plt.plot(epsilon_var, temperatures)
    plt.xlabel('Emissivity')
    plt.ylabel('Temperature (C)')
    plt.title('Temperature vs Emissivity at Albedo = {}'.format(albedo))
    plt.grid()
    plt.show()

def plot_temperature_vs_albedo():
    """
        Plot the temperature of the Earth as a function of albedo
        for a fixed emissivity.
    """
    import matplotlib.pyplot as plt
    albedo_var = np.linspace(0.294, 0.286, 50)
    emissivity = 0.614618

    temperatures = kelvin_to_celsius(temperature_at_energy_balance(albedo_var, emissivity))
    
    # Plot from high to low albedo
    plt.plot(albedo_var, temperatures)
    plt.gca().invert_xaxis() # Invert x-axis to show high albedo on the left
    plt.xlabel('Albedo')
    plt.ylabel('Temperature (C)')
    plt.title('Temperature vs Albedo at Emissivity = {}'.format(emissivity))
    plt.grid()
    plt.show()

plot_temperature_vs_albedo()
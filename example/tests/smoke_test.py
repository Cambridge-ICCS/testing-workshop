# Some common package checks
def test_initialization():
    from energy_balance import __init__ as package_init

    assert package_init is not None, "Package initialization failed"


# Main smoke test for energy_balance package
def test_config_loading():
    import energy_balance

    # Check that init does not fail
    energy_balance.init()
    # and that it initializes a global variable
    assert (
        energy_balance.solar_constant is not None
    ), "Solar constant should be initialized"


# Smoke tests for plots
def test_plots_smoke():
    # Use non-interactive backend for headless testing
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import energy_balance

    energy_balance.init()
    try:
        fig1 = energy_balance.plot_temperature_vs_albedo()
        assert (
            fig1 is not None
        ), "plot_temperature_vs_albedo function did not return a Figure"
        fig2 = energy_balance.plot_temperature_vs_emissivity()
        assert (
            fig2 is not None
        ), "plot_temperature_vs_emissivity function did not return a Figure"

    except Exception as e:
        assert False, f"Plotting failed with exception: {e}"
    finally:
        plt.close("all")

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
    assert energy_balance.solar_constant is not None, "Solar constant should be initialized"
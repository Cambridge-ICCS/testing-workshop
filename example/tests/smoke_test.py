import energy_balance

# Some common package checks

def test_initialization():
    from src import __init__ as package_init
    assert package_init is not None, "Package initialization failed"

def test_version():
    from src import __version__
    assert __version__ is not None, "Version should not be None"
    assert isinstance(__version__, str), "Version should be a string"
    assert __version__ != "", "Version should not be an empty string"

# Main smoke test for energy_balance package

def test_config_loading():
    # Check that init does not fail
    energy_balance.init()
    # and that it initializes a global variable
    assert energy_balance.solar_constant is not None, "Solar constant should be initialized"

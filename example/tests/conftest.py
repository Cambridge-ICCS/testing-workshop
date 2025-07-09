import energy_balance
import pytest

@pytest.fixture
def setup():
    energy_balance.init()

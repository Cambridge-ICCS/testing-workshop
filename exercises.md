# Exercises

## Prelim / setup

1. Clone the workshop repo and navigate to the `example` directory

```
git clone https://github.com/Cambridge-ICCS/testing-workshop
cd testing-workshop/exmaple
```

2. Setup a virtual environment (optional step) and install the dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. (Optional) To make it easy to import the Python module for exploration, set the `PYTHONPATH` to include the `src` directory:

```
export set PYTHONPATH=$PYTHONPATH:$(pwd)/src 
```

4. Make sure you can run the smoke tests to check all is working well:

```
pytest tests/smoke_test.py
```

## Unit tests

1. Run the unit tests in `test_energy_balance.py`

```
pytest tests/test_energy_balance.py
```

The `temperature_at_energy_balance` takes two (float) arguments, one for __albedo__ of the Earth (i.e., a value between 0 and 1) and one for the __emissivity__ (ratio of radiation actually emitted versus energy emitted if it were a true black body).

2. Write a unit test for `temperature_at_energy_balance` that
makes two input-output assertions based on some extremal points for which it is possible to work out what the behaviour without running the code.

3. Add a further test of `temperature_at_energy_balance` input-output behaviour by picking some other input values, running the code (i.e., in the repl) to see the output, and then codifying this in a test.

Don't forget to run the `init()` function first!

# Property-based testing

1. The `energy_out` function (from the `energy_balance` module) determines
the energy radiated from the Earth as a function of its temperature (in Kelvin) assuming it is a black body emitter. What is a property that we can always expect of the output? Write a property-based test for this.

Consider what strategy (generator) to use and how you can provide suitable inputs to the test.
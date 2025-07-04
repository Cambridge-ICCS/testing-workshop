# Exercises

## Prelim / setup

1. Clone the workshop repo and navigate to the `example` directory

```bash
git clone https://github.com/Cambridge-ICCS/testing-workshop
cd testing-workshop/exmaple
```

2. Setup a virtual environment (optional step) and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. (Optional) To make it easy to import the Python module for exploration, set the `PYTHONPATH` to include the `src` directory:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
```

4. Make sure you can run the smoke tests to check all is working well:

```bash
pytest tests/smoke_test.py
```

## Unit tests

1. Run the unit tests in `test_energy_balance.py`

```bash
pytest tests/test_energy_balance.py
```

The `temperature_at_energy_balance` takes two (float) arguments, one for __albedo__ of the Earth (i.e., a value between 0 and 1) and one for the __emissivity__ (ratio of radiation actually emitted versus energy emitted if it were a true black body).

2. Write a unit test for `temperature_at_energy_balance` that
makes two input-output assertions based on some extremal points for which it is possible to work out what the behaviour without running the code.

3. Add a further test of `temperature_at_energy_balance` input-output behaviour by picking some other input values, running the code (i.e., in the repl) to see the output, and then codifying this in a test.

    Don't forget to run the `init()` function first when experimenting, but use the `setup` text fixture to have this done for you in the tests.

4. Turn the above three input-output tests into a 'parameterized' test (see `test_helpers_param.py` for an example) to avoid repetition.

5. (Bonus) Check the coverage of the whole test suite:

```bash
pytest tests/ --cov src
```

You can get a report on which lines are not visited by any tests with:

```bash
pytest tests/ --cov src --cov-report term-missing
```

Or if you prefer more visual report, you can try to generate HTML report
```bash
pytest tests/ --cov src --cov-report html
```
this will generate `htmlcov` folder where you can see the report in your browser by opening `htmlcov/index.html`

Choose a section of lines not covered by a test and write an additional test to increase the coverage. Verify that this has improved coverage aftwerwards.

## Property-based testing

1. The `energy_out` function (from the `energy_balance` module) determines
the energy radiated from the Earth as a function of its temperature (in Kelvin) assuming it is a black body emitter. What is a property that we can always expect of the output? Write a property-based test for this.

    Consider what strategy (generator) to use and how you can provide suitable inputs to the test.

The `plot_temperature_vs_emissivity()` and `plot_temperature_vs_albedo()` functions generate matplotlib plots and use a custom `linspace` function
in `helpers.py` where `linspace(x, y, n)` generates a NumPy of `n` floating
point values from `x` to `y` inclusive, evenly spaced. Now for the `linspace` function:


2. Write some post-condition-style property-based tests that relate values in the output to the input arguments. Hint: think about whether arguments should appear in the output, and where, and how the size of the output relates to the arguments.

3. Think of what a valid output should look like for `linspace`. Codify
this as a property based test.

4. Consider what happens when the first two arguments are flipped and
from this create a further general property-based test for linspace. Hint: you
may also need the `np.flip` function which reverse an array.

## Extension: Doctests demo and exercise

1. A 'doctest' is a kind of comment that contains an example that is then machine-checked as a test. Navigate to `example/src/doctest_demo.py` to see an example, with explanation, and an in situ exercise.
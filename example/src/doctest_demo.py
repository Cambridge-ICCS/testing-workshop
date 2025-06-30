from numbers import Number


def square_me_with_doctest(num: Number) -> Number:
    """This function calculates a square of a number.

    But in reality it is meant to show off a useful subclass of testing:
    🎉 Doctests! 📜✅

    Introduction
    ------------

    Have you ever wondered how packages such as Numpy ensure that there examples
    (like the one here: https://numpy.org/doc/stable/reference/generated/numpy.tanh.html)
    are up to date? The doctest are the answer.

    But what are doctests really. They are a feature of a testing framework
    such as `pytest` that allows to run all code example snippets and compare
    them against the reference output. For example below:
    >>> square_me_with_doctest(2)
    5

    well... except the example is wrong. Let us detect it with `pytest`!
    If you try to run `pytest doctest_demo.py` you will notice that nothing
    happens.

    This is because `pytest` does not run doctests by default. We need to add an
    extra flag to tell it to scan doctest for code snippets and run them.

    Try `pytest --doctest-modules doctest_demo.py` and fix the example above.

    If you want to avoid typing it each time you can add it as a fixed option
    in your `pytest.ini` configuration. Visit the file in the root directory
    and uncomment relevant lines.

    How to write doctest compatible examples
    ----------------------------------------

    The full specifications are available in Python documentation
    (https://docs.python.org/3/library/doctest.html)

    In short each time we write `>>>` (python REPL prompt) together with `...`,
    if it is considered expression spans multiple lines, a code snippet and will
    be run as part of the doctests.

    So this will execute:
    >>> if True:
    ...     2 * 10
    ... else:
    ...     0
    20

    But these will not
    >> 2 * 10
    18
    ... 2 * 2
    5

    We can also switch off a snippet explicitly (e.g. to show invalid use) like
    this:
    >>> 3 + 3 # doctest: +SKIP
    7

    Note that the output must be exactly what you will get in REPL! So e.g. with
    Numpy > 2.0 we need to be careful since:
    >>> import numpy as np
    >>> square_me_with_doctest(np.float64(1.01))
    np.float64(1.0201)

    Or generally with not round numbers:
    >>> 1/3
    0.3333333333333333

    which in practice would be quite annoying. Hence it is possible to fix that
    using the `ELLIPSIS` marker (...) to ignore part of the output like this:
    >>> 1/3 # doctest: +ELLIPSIS
    0.33...3

    Note that the doctest environment is persistent between snippets in the
    same docstring. We have already imported `numpy` so the following will work:
    >>> np.sqrt(4.0)
    np.float64(2.0)

    Last but not least we can test exceptions:
    >>> square_me_with_doctest("5")
    Traceback (most recent call last):
        The details of the stack in the traceback are ignored in a doctest!
        We can put anything we want here but the best-practice is the ELLIPSIS:
        ...
    ValueError: Argument `num` in not a <class 'numbers.Number'> but <class 'str'>

    Exercises
    ---------
    1) Write a doctest for the following python expression
    `[i for i in range(2)]` below:
    #
    # REPLACE HERE WITH YOUR ANSWER
    #

    2) Finish the following doctest:
    # Uncomment and replace ???
    # >>> raise RuntimeError("An exception")
    # ???

    3) Use ELLIPSIS to check a very long doctest output:
    # Uncomment and replace ???
    # >>> [i for i in range(1000)] # doctest: +ELLIPSIS
    # ???

    Summary
    -------
    - Code snippets in the docstrings can be run as tests. These are called
      `doctests`
    - To run they usually need to be explicitly enabled
      (pytest `--doctest-modules` option)
    - They run code snippets in docstring and compare text output against
      a reference as if run in REPL.
    - To handle problematic outputs (e.g. very long, containing blank lines)
      there are customisation options available. Refer to Python documentation
      for help: https://docs.python.org/3/library/doctest.html
    """
    if not isinstance(num, Number):
        raise ValueError(f"Argument `num` in not a {Number} but {type(num)}")
    return num * num

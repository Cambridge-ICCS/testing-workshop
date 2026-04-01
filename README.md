<img src="https://cambridge-iccs.github.io/assets/images/iccs-logo.png"  width="70%" align="left" style='clear:both'>


<br><br><br><br>

# Workshop on Correctness and Testing

![GitHub](https://img.shields.io/github/license/Cambridge-ICCS/Summer-School-Julia-Tutorial)

This is an intensive 2h30 minute workshop on correctness and testing for scientific software, using Python as the demonstration language with the `pytest` framework. It assumes that the attendees have some programming skills, but are not necessarily Python experts. There is some emphasis on scientific computing, with the example being a simple 0D Energy Balance Model (EBM). It would therefore be beneficial if you have some experience in this field, though not strictly necessary.

This material was first delivered at the 2025 ICCS summer school, see the [part 1](https://www.youtube.com/watch?v=iBra9Fv3jvc&list=PL3PByZO-B6dODVXyQcfKEDnIldqReFryp&index=18) and [part 2 videos](https://www.youtube.com/watch?v=4qc3UOtIRu4&list=PL3PByZO-B6dODVXyQcfKEDnIldqReFryp&index=21).

## Contents

- [Learning Objectives](#learning-objectives)
- [Teaching material](#teaching-material)
- [Preparation and prerequisites](#preparation-and-prerequisites)
- [Installation and setup](#installation-and-setup)
- [License information](#license)
- [Contribution Guidelines and Support](#contribution-guidelines-and-support)

## Learning objectives

1. Understand a high-level overview of verification and validation in the context of computational science;
2. Explain the purpose and limitations of testing, including why testing cannot guarantee the absence of bugs but still increases confidence in code.
3. Write basic automated unit tests using pytest, including covering edges cases, invalid inputs, and considering the role of numerical representation;
4. Apply testing best practices, including parameterisation, fixtures, negative tests, and Test-Driven Development (TDD).
5. Understand integration and end-to-end tests, recognising common interface issues and trade-offs in testing strategies.
6. Write property-based tests with Hypothesis to generate diverse inputs and define meaningful properties.
7. Select and combine appropriate testing approaches to improve reliability, support refactoring, and diagnose errors in scientific software.

## Teaching material

### Slides

The slides are included in this repository.

### Examples and exercises

The `example` folder provides a small 0-dimensional Energy Balance Model for a planet (with its main configuration being for Earth). See 
`example/README.md` for instructions on its usage. It contains a test suite in the `example/tests` directory which is used for demonstration and is the source material for the exercises in `exercises.md`, which also provides setup instructions.

### Worked solutions

Coming soon

### Session structure of 2025 course

Session 1 - 1h
- 10 minute intro about correctness and testing
- 50 minutes explaining concepts about unit testing including
     * Parameterised tests
     * Fixtures
     * Negative tests
     * Approximation and floating point
     * TDD
     * Code coverage

Session 2 - 1h30
- 20 minute unit test exercises
- 40 minutes lecture
    - Integration and end-to-end tests
    - Property-based testing
- 30 minutes exercises (property-based test exercises)

## Preparation and prerequisites

### Prerequisites

- Basic programming knowledge
- At least beginner experience in Python, e.g., understanding of
            - Basic mathematical operations
            - Writing and running scripts/programs
            - Writing and using functions

The examples require Python 3.11 and above, and will use pytest. See
the [installation and setup instructions below](#installation-and-setup).

### Preparation

The workshop exercises involve writing Python code and running tests, so you will need to already have a text editor or IDE (Integrated Development Environment) setup and ready to use. The examples and exercises all use Python 3.

If you require assistance or further information with any of these please reach out to
us before the session.

## Installation and setup

1. You can obtain the code for the exercises by cloning this repository locally:
  ```
  git clone https://github.com/Cambridge-ICCS/testing-workshop.git
  ```

2. Setup a virtual environment and install the requirements, e.g.

```
cd example
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

3. You can then run the provided tests by running:

```
pytest tests
```

The examples and exercises will build from this setup.

## License

The code materials in this project are licensed under the [MIT License](LICENSE).

## Contribution Guidelines and Support

If you spot an issue with the materials please let us know by
[opening an issue](https://github.com/Cambridge-ICCS/testing-workshop/issues)
here on GitHub clearly describing the problem.

If you are able to fix an issue that you spot, or an
[existing open issue](https://github.com/Cambridge-ICCS/testing-workshop/issues)
please get in touch by commenting on the issue thread.

Contributions from the community are welcome.
To contribute back to the repository please first
[fork it](https://github.com/Cambridge-ICCS/testing-workshop/fork),
make the necessary changes to fix the problem, and then open a pull request back to
this repository clearly describing the changes you have made.
We will then preform a review and merge once ready.

If you would like support using these materials, adapting them to your needs, or
delivering them please get in touch either via GitHub or via
[ICCS](https://github.com/Cambridge-ICCS).


<img src="https://cambridge-iccs.github.io/assets/images/iccs-logo.png"  width="50%" align="left" style='clear:both'>


<br><br><br><br>

# Workshop on Correctness and Testing

![GitHub](https://img.shields.io/github/license/Cambridge-ICCS/Summer-School-Julia-Tutorial)

This is an intensive 2h30 minute workshop on correctness and testing for scientific software, using Python as the demonstration language with the `pytest` framework. It assumes that the attendees have some programming skills, but are not necessarily Python experts. There is some emphasis on scientific computing, with the example being a simple 0D Energy Balance Model (EBM). It would therefore be beneficial if you have some experience in this field, though not strictly necessary.

The slides are included in this repository.

This material was first delivered at the 2025 ICCS summer school.

## Learning objectives

1. Understand a high-level overview of verification and validation in the context of computational science;
2. Explain the purpose and limitations of testing, including why testing cannot guarantee the absence of bugs but still increases confidence in code.
3. Write basic automated unit tests using pytest, including covering edges cases, invalid inputs, and considering the role of numerical respresentation;
4. Apply testing best practices, including parameterisation, fixtures, negative tests, and Test-Driven Development (TDD).
5. Understand integration and end-to-end tests, recognising common interface issues and trade-offs in testing strategies.
6. Write property-based tests with Hypothesis to generate diverse inputs and define meaningful properties.
7. Select and combine appropriate testing approaches to improve reliability, support refactoring, and diagnose errors in scientific software.

## Session structure

### Session 1 - 1h
- 10 minute intro about correctness and testing
- 50 minutes explaining concepts about unit testing including
     * Parameterised tests
     * Fixtures
     * Negative tests
     * Approximation and floating point
     * TDD
     * Code coverage

### Session 2 - 1h30
- 20 minute unit test exercises
- 40 minutes lecture
    - Integration and end-to-end tests
    - Property-based testing
- 30 minutes exercises (property-based test exercises)

## Example and exercises

The `example` folder provides a small 0-dimensional Energy Balance Model for a planet (with its main configuration being for Earth). See `example/README.md` for instructions on its usage. It contains a test suite in the `example/tests` directory which is used for demonstration and is the source material for the exercises in `exercises.md`, which also provides setup instructions.

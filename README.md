<img src="https://cambridge-iccs.github.io/assets/images/iccs-logo.png"  width="50%" align="left" style='clear:both'>


<br><br><br><br>

# Workshop on Correctness and Testing

![GitHub](https://img.shields.io/github/license/Cambridge-ICCS/Summer-School-Julia-Tutorial)

This is an intensive 2h30 minute workshop on correctness and testing for scientific software, using Python as the demonstration language with the `pytest` framework. It assume that the attendees have programming skills, but not necessarily Python experts. There is some emphasis on scientific computing, with the example being a simple energy balance model (EBM), so it would be beneficial if you have some experience in this field as well though not strictly necessary. 

This material was first delivered at the 2025 ICCS summer school.

## Session 1 - 1h
- 10 minute intro about correctness and testing
- 50 minutes explaining concepts about unit testing including
     * Parameterised tests
     * Fixtures
     * Negative tests
     * Approximation and floating point
     * TDD
     * Code coverage

## Session 2 - 1h30
- 20 minute unit test exercises
- 20 minutes talking about integration tests
- 20 minutes introduction to property based testing
- 30 minutes property-based test exercises

## Example and exercises.

The `example` folder provides a small 0-dimensional Energy Balance Model for a planet (with its main configuration being for Earth). See `example/README.md` for instructions on its usage. It contains a test suite in the `example/tests` directory which is used for demonstration and is the source material for the exercises in `exercises.md`, which also provides setup instructions.

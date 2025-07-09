# ADASS2025webtest


## Title: Testing for Robust and Reproducible Research Software with Python and Pytest

## Main Topic Description:

This tutorial will provide a hands-on introduction to automating unit testing in Python using the industry-standard pytest framework. Participants will learn how to design software components that are easily testable, write effective unit tests using pytest to ensure software robustness and maintainability, and generate and utilize code coverage metrics to verify the comprehensiveness of their test suite. The session will emphasize how these practices contribute to a more reliable software stack that enables reproducible research.

## Primary Learning Objectives:

Upon completion of this tutorial, participants will be able to:

1.  Design software components in Python that facilitate effective unit testing.
2.  Write comprehensive unit tests for Python code using the pytest framework.
3.  Create and interpret code coverage metrics in Python to ensure thorough testing of their software.

## Detailed Tutorial Structure:

The tutorial will combine brief explanations with active, hands-on exercises.

    Introduction to Automated Testing in Python: Briefly introduce the importance of automated unit testing for robust and reproducible research in Python. Introduce the pytest framework, highlighting its key features and benefits.
    Designing for Testability in Python (Aim 1): Discuss principles of software design in Python that make unit testing easier. This section will cover topics such as modularity, separation of concerns, and dependency injection with Python-specific examples. Hands-on exercises will involve refactoring simple Python code snippets to improve their testability.
    Writing Effective Unit Tests with pytest (Aim 2): This section will focus on the practical aspects of writing unit tests using pytest. Participants will learn how to write test functions, use pytest's assertion methods, implement parameterization for testing various inputs, and handle exceptions in tests. Hands-on exercises will guide participants through writing tests for provided Python modules.
    Measuring Code Coverage in Python (Aim 3): Introduce the concept of code coverage and demonstrate how to use tools (e.g., `coverage.py`) to generate coverage reports. Participants will learn how to interpret these reports to identify untested parts of their Python code and how to use this information to improve their test suite. Hands-on exercises will involve running tests with coverage measurement and analyzing the results.

Length of Tutorial: 90 minutes to 120 minutes

module 1: design for testability (20 min)

    slides (10 min)
    adass_00_design_for_testability_ex.ipynb (5 min)
    adass_01_typehint_ex.py (5 min)

module 2: write tests (45 min)

    slides (5 minutes)
    pytest_01_ex.py (5 min)
    pytest_02_fixtures_ex.py (5 min)
    pytest_03_skipxfail_ex.py (5 min)
    pytest_04_requests_ex.py (5 min)
    pytest_05_intro_selenium.ipynb (10 min)
    pytest_06_selenium_exercises.py (10 min)

module 3: coverage (20 min)

    Slides (5 minutes)
    coverage_00/test_temperature_ex.py (5 minutes)
    coverage_01/calculator_legacy.py (10 minutes)

## Tutorial Materials

    Powerpoint: https://docs.google.com/presentation/d/1AATZfG2WemKUFUtp_c5Jn7tqgA_qVaizep65A2pUJPY/edit?usp=sharing
    Code Exercises: https://github.com/Smithsonian/adass2025-tutorial-pytest

## List of What Participants Will Need

    Wifi capable laptop in any operating system that can run python 3.  Exercises are tested on MacOS and Linux.
    Code exercise repository: https://github.com/Smithsonian/adass2025-tutorial-pytest
    Python3 and pre-installed python packages (listed in code repository)
    

POC
Gregory Ciccarelli
gregory.ciccarelli@cfa.harvard.edu

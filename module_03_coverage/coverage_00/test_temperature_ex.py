import pytest
from temperature import classify_temperature

"""
Introduction to Test Coverage with coverage.py

Test coverage measures how much of your code is executed while running tests.
The `coverage.py` tool can help identify untested parts of your code.
"""

# Exercise: Run coverage before writing additional tests
# to identify which parts of the code are untested
#
# >> coverage run -m pytest test_temperature_ex.py
# >> coverage report
# >> coverage html
# Using a browser, open htmlcov/index.html


# Exercise: Extend the test to cover all parts of the code
# Verify coverage.
@pytest.mark.parametrize(
    "temp, expected",
    [
        (-5, "freezing"),  # < 0
    ],
)
def test_classify_temperature(temp, expected):
    assert classify_temperature(temp) == expected

# -------------------------------
# Pytest Answers
# -------------------------------
# pytest -rA pytest_01_sln.py

import pytest
from pytest_01_ex import add


def test_add():
    assert add(2, 3) == 5


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 2),
        (0, 5, 5),
        (-1, -1, -2),
    ],
)
def test_add_param(a, b, expected):
    assert add(a, b) == expected

# test_calculator_sln.py

import pytest
from calculator_sln import calculate, add, divide


def test_add():
    assert calculate("add", 2, 3) == 5


def test_sub():
    assert calculate("sub", 5, 2) == 3


def test_mul():
    assert calculate("mul", 3, 4) == 12


def test_div():
    assert calculate("div", 10, 2) == 5


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("div", 10, 0)


def test_mod():
    assert calculate("mod", 10, 3) == 1


def test_mod_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("mod", 10, 0)


def test_invalid_operation():
    with pytest.raises(KeyError):
        calculate("power", 2, 3)


def test_add_direct():
    assert add(100, 200) == 300


def test_div_throws_right_exception_message():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(1, 0)


@pytest.mark.parametrize(
    "op,a,b,result",
    [
        ("add", 1, 2, 3),
        ("sub", 5, 3, 2),
        ("mul", 4, 5, 20),
        ("mod", 7, 4, 3),
    ],
)
def test_all_ops(op, a, b, result):
    assert calculate(op, a, b) == result

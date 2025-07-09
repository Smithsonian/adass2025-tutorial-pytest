# Covering test cases for the legacy calculator

import pytest
from calculator_legacy import calculate


def test_add():
    assert calculate("add", 2, 3) == 5


def test_sub():
    assert calculate("sub", 5, 2) == 3


def test_mul():
    assert calculate("mul", 3, 4) == 12


def test_div():
    assert calculate("div", 10, 2) == 5


def test_div_by_zero():
    assert calculate("div", 10, 0) == "Cannot divide by zero"


def test_mod():
    assert calculate("mod", 10, 3) == 1


def test_mod_by_zero():
    assert calculate("mod", 10, 0) == "Modulo by zero"


def test_invalid_operation():
    assert calculate("power", 2, 3) == "Invalid operation"

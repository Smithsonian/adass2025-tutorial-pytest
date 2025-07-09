# calculator_sln.py

# ANSWERS
# 1. Design for testing: separation of concerns- we break the calculator method into independent methods
# 2. Design for testing: raise exceptions rather than return error strings
# 3. Design for testing: type hints
# 3. General design: Python does not have a concept of static class, and all of the methods are pure functions.
#    Therefore, though we could make this a class, put all the methods into the class and annotate with
#    @staticmethod, we get the same result without needing class boiler plate by placing the methods in a python module
#    Bonus:  What might be an example of calculator instance property that would making having a class a good idea?
#            A: Number of decimal points of precision
# 4. General design: Input validation.  Use an enum for denoting valid operations for type hint/ide support
#    and use the dictionary to perform operation validation.

# Note:  TypeError, KeyError, and ZeroDivisionError are Python built-in so they do not need to be imported.

from typing import Union
from enum import Enum


class Operation(Enum):
    ADD = "add"
    SUBTRACT = "sub"
    MULTIPLY = "mul"
    DIVIDE = "div"
    MODULO = "mod"


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulo by zero")
    return a % b


def calculate(
    operation: str, a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:
    """
    Perform basic arithmetic operations on two numbers.

    Args:
        operation: String representing the operation ('add', 'sub', 'mul', 'div', 'mod')
        a: First number
        b: Second number

    Raises:
        TypeError: If operands are not numbers
        KeyError: If the operation is not supported
        ZeroDivisionError: If attempting to divide or modulo by zero

    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numbers")

    operation_mapping = {
        Operation.ADD.value: add,
        Operation.SUBTRACT.value: subtract,
        Operation.MULTIPLY.value: multiply,
        Operation.DIVIDE.value: divide,
        Operation.MODULO.value: modulo,
    }

    if operation not in operation_mapping:
        raise KeyError(f"Operation '{operation}' not supported")

    return operation_mapping[operation](a, b)

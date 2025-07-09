# calculator_legacy.py
#
# See README for instructions


def calculate(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b
    elif operation == "mod":
        if b == 0:
            return "Modulo by zero"
        else:
            return a % b
    else:
        return "Invalid operation"

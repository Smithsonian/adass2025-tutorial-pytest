# Run mypy on this script.  Observe no errors.
# >> mpy adass_01_typehint_ex.py
#
# Run this script and observe the runtime error
# >> python adass_01_typehint_ex.py
#
# Add type hints to the arguments and return value of the method
#
# Re-run mypy and show that mypy detects an error


def legal_name(first, last):
    """Make greeting.

    Params:
        first (str)
        last (str)

    Returns:
        (str)
    """

    return "My legal name is: " + first + " " + last


legal_name(
    "Jane", 5
)  # This will NOT cause a Mypy error but it WILL cause a runtime error

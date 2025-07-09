# >> mypy adass_01_typehint_sln.py


def legal_name(first: str, last: str) -> str:
    return "My legal name is: " + first + " " + last


legal_name("Jane", 5)  # This will cause a Mypy error

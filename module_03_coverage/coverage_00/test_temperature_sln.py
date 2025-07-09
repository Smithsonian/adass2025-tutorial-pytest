import pytest
from temperature import classify_temperature


@pytest.mark.parametrize(
    "temp, expected",
    [
        (-5, "freezing"),  # < 0
        (10, "cold"),  # < 20
        (25, "warm"),  # < 30
        (35, "hot"),  # >= 30
    ],
)
def test_classify_temperature(temp, expected):
    assert classify_temperature(temp) == expected

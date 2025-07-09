import pytest


@pytest.fixture
def sample_data():
    return [10, 20, 30]


def test_data_sum(sample_data):
    assert sum(sample_data) == 60


def test_tmp_file(tmp_path):
    file = tmp_path / "output.txt"
    file.write_text("Chandra X-ray Data")
    assert file.read_text() == "Chandra X-ray Data"

# Exercise: Create a fixture function that returns a list of integers
# of sample data int for testing
# Call that fixture as part of the test
# The test should assert that the sum of the sample_data is the hand computed sum
#
# Bonus:  Place the sample_data fixture in conftest.py instead of in the test file
def sample_data():
    pass


def test_with_fixture(sample_data):
    pass


# Exercise: Write data to a temporary path/file create using the tmp_path fixture
# Read the temporary file and assert it contains the written data
def test_tmp_file(tmp_path):
    pass

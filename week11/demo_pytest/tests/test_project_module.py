import pytest

# Import the project_module from the my_project package located one level up
from ..my_project import project_module


# Test function to check if the fixture my_data returns the expected value
def test_something(my_data):
    # Assert that my_data is equal to 42
    assert my_data == 42


# Parameterized test for the rolling_average function
@pytest.mark.parametrize("values,expected_results", [
    (
            # First test case: input values and their expected rolling averages
            [1, 2, 3, 4, 5, 6],
            [2.0, 3.0, 4.0, 5.0],
    ),
    (
            # Second test case: input values and their expected rolling averages
            [-1, -2, -3, -4, -5, -6],
            [-2.0, -3.0, -4.0, -5.0],
    ),
])
def test_rolling_average(values, expected_results):
    # Call the rolling_average function from project_module with the given values and a period of 3
    result = project_module.rolling_average(values, 3)
    # Assert that the result matches the expected results
    assert result == expected_results
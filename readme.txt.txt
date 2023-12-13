Requirements/Libraries:

Python 3.x
pandas
requests
pytest
unittest.mock
os
datetime



Rocket Launch Report Generator

Functions Code:

get_data(url) -> This function takes a URL and retrieves data from the API.

Parameters:
  url: The URL of the API.
Returns:
  A DataFrame with data from the API.

transform_data(launches, rockets) -> This function transforms launches and rockets data.

Parameters:
  launches: DataFrame containing launch data.
  rockets: DataFrame containing rocket data.
Returns:
  Merged DataFrame containing launch dates and rocket names.

filter_by_date(df, year=None, month=None) -> This function filters data based on the provided year and/or month.

Parameters:
  df: DataFrame to be filtered.
  year: The year for filtering (optional).
  month: The month for filtering (optional).
Returns:
  DataFrame filtered by year and/or month.

generate_report(df, file_name, output_path=".") -> Generates a CSV report of the filtered DataFrame.

Parameters:
  df: DataFrame to be reported.
  file_name: Name of the CSV file.
  output_path: Output path for the CSV file (default: current directory).
Returns:
  CSV report file.

validation(file_path) -> Validates the existence of a file at the specified path.

Parameters:
  file_path: Path of the file to be validated.
Returns:
  Information about whether the file exists.

Main Code -> The main code implements a rocket launch report generator using SpaceX API.

Usage:
  generate_raport(file_name, output_path=".", year=None, month=None)

  file_name: Name of the CSV report file.
  output_path: Output path for the CSV file (default: current directory).
  year: The year for filtering (optional).
  month: The month for filtering (optional).

Example:
  generate_raport("rocket_launch_report", output_path=".", year=2022, month=4)

Tests Code

test_get_data_launches -> Test case for the get_data function with SpaceX launches API.

test_get_data_rockets -> Test case for the get_data function with SpaceX rockets API.

test_transform_data -> Test case for the transform_data function.

test_filter_by_date_datetime_format -> Test case for checking the datetime format after using filter_by_date.

test_generate_report -> Test case for the generate_report function.

test_validation -> Test case for the validation function.

How to Run Tests:

Run the tests using a pytest. Example: pytest tests.py

Error Handling: The code includes error handling for data retrieval, processing, and file operations to ensure robustness.

Note: This solution is designed to be generic, allowing code reuse and quick modification. Ensure the required dependencies are installed before running the code.

For more details, refer to the code and example usage provided.

# SpaceX Rocket Launch Report Generator

## Description

This project contains a script for generating reports based on data related to SpaceX rocket launches. The script utilizes functions from the `src.functions` module to create reports based on provided parameters such as date and CSV file name.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/petardaszymek/interview_task.git
    ```

2. Navigate to the project directory:

    ```bash
    cd project-name
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run in Bash

1. Open a terminal and navigate to the project directory:

    ```bash
    cd path/to/project
    ```

2. Run the `main.py` script, providing the necessary arguments:

    ```bash
    python main.py --file_name FILE_NAME --output_path OUTPUT_PATH --year YEAR --month MONTH
    ```

    Example:

    ```bash
    python main.py --file_name spacex_launches --output_path C:/Users/User/Desktop --year 2020
    ```

## Arguments

- `--file_name`: Name of the CSV file containing data about SpaceX rocket launches.
- `--output_path`: Path to the output directory (default is the current directory).
- `--year`: Year for the report (optional).
- `--month`: Month for the report (optional).

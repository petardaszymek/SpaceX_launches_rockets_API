import pytest
from unittest.mock import patch
import pandas as pd
from datetime import datetime
from src.functions import get_data, transform_data, generate_report, validation, filter_by_date


@patch('functions.requests.get')
def test_get_data_launches(mock_requests_get):
    mock_response = [{'key1': 'value1'}, {'key2': 'value2'}]
    mock_requests_get.return_value.json.return_value = mock_response

    result_df = get_data('https://api.spacexdata.com/v4/launches')

    mock_requests_get.assert_called_once_with('https://api.spacexdata.com/v4/launches')
    assert result_df.equals(pd.json_normalize(mock_response))


@patch('functions.requests.get')
def test_get_data_rockets(mock_requests_get):
    mock_response = [{'key1': 'value1'}, {'key2': 'value2'}]
    mock_requests_get.return_value.json.return_value = mock_response

    result_df = get_data('https://api.spacexdata.com/v4/rockets')

    mock_requests_get.assert_called_once_with('https://api.spacexdata.com/v4/rockets')
    assert result_df.equals(pd.json_normalize(mock_response))


@pytest.fixture
def example_launches():
    # Create a sample launches DataFrame for testing
    return pd.DataFrame({
        'static_fire_date_utc': ['2022-01-01T12:00:00.000Z', '2022-02-01T14:30:00.000Z'],
        'rocket': ['rocket_id_1', 'rocket_id_2']
    })


@pytest.fixture
def example_rockets():
    # Create a sample rockets DataFrame for testing
    return pd.DataFrame({
        'id': ['rocket_id_1', 'rocket_id_2'],
        'name': ['Falcon 9', 'Falcon Heavy']
    })


def test_transform_data(example_launches, example_rockets):
    result_df = transform_data(example_launches, example_rockets)

    assert isinstance(result_df, pd.DataFrame)
    assert result_df.columns.tolist() == ['static_fire_date_utc', 'name']
    assert len(result_df) == 2

    for date_str in result_df['static_fire_date_utc']:
        assert isinstance(date_str, datetime)

    assert all(result_df['static_fire_date_utc'].iloc[i] >= result_df['static_fire_date_utc'].iloc[i+1]
               for i in range(len(result_df)-1))


def test_filter_by_date_datetime_format():
    df = pd.DataFrame({
        'static_fire_date_utc': [datetime(2022, 1, 1), datetime(2022, 2, 1)],
        'other_column': ['A', 'B']
    })

    filtered_df = filter_by_date(df, year=2022, month=1)
    assert isinstance(filtered_df['static_fire_date_utc'].iloc[0], pd.Timestamp)
    assert isinstance(filtered_df['static_fire_date_utc'].iloc[1], pd.Timestamp)


def test_generate_report(tmp_path):
    df = pd.DataFrame({
        "static_fire_date_utc": [datetime(2023, 1, 1), datetime(2023, 2, 1)],
        "name": ["Falcon 9", "Falcon Heavy"]
    })

    file_name = "test_report"
    output_path = tmp_path
    result_df = generate_report(df, file_name, output_path)

    file_path = tmp_path / f"{file_name}.csv"
    assert file_path.exists()
    assert len(pd.read_csv(file_path)) == len(result_df)


def test_validation(capsys):
    with patch('sys.exit') as mock_exit:

        file_path_existing = "path/to/existing/file.csv"
        validation(file_path_existing)

        captured = capsys.readouterr()
        expected_message = f"There is no file at the path {file_path_existing}\n".strip()
        actual_message = captured.out.strip()

        assert not mock_exit.called
        assert actual_message == expected_message

        file_path_non_existing = "path/to/non_existing/file.csv"
        validation(file_path_non_existing)

        captured = capsys.readouterr()
        expected_message = f"There is no file at the path {file_path_non_existing}\n".strip()
        actual_message = captured.out.strip()

        assert not mock_exit.called
        assert actual_message == expected_message

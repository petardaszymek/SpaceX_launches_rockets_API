import requests
import pandas as pd
import os


def get_data(url):
    """
    This function takes an url and returns the data from the API
    :param url:
    :return: dataframe with data from api
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # check if the http request was succeed
        data = response.json()
        df = pd.json_normalize(data)
        return df
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.RequestException as e:
        print(f"There was an error retrieving data from {url}: {e}. Check your connection with internet.")


def transform_data(launches, rockets):
    """
    Transforms launches and rockets
    :param launches:
    :param rockets:
    :return: merged dataframe: launches and rockets
    """
    try:
        launches = launches[["static_fire_date_utc", "rocket"]]
        rockets = rockets[["id", "name"]]
        df = launches.merge(rockets, left_on="rocket", right_on="id")
        df = df[["static_fire_date_utc", "name"]]
        df = df[df['static_fire_date_utc'].notnull()]
        df['static_fire_date_utc'] = pd.to_datetime(df['static_fire_date_utc'], format='%Y-%m-%dT%H:%M:%S.%fZ')
        df = df.sort_values(by='static_fire_date_utc', ascending=False)
        df.reset_index(drop=True, inplace=True)
        return df
    except Exception as e:
        print(f"There was an error during processing: {e}. check the data structure and try again.")
        return None


def filter_by_date(df: pd.DataFrame, year=None, month=None):
    """
    Filter data
    :param df:
    :param year:
    :param month:
    :return: df filtered by year and month
    """
    condition_year = (df['static_fire_date_utc'].dt.year == int(year)) if year else True
    condition_month = (df['static_fire_date_utc'].dt.month == int(month)) if month else True
    return df.loc[condition_year & condition_month]


def generate_report(df: pd.DataFrame, file_name, output_path="."):
    """
    This function generates a report of the filtered dataframe
    :param df: pd.DataFrame
    :param file_name:
    :param output_path:
    :return: csv report file
    """
    try:
        file_path = os.path.join(output_path, f"{file_name}.csv")
        df.to_csv(file_path, index=False)
        print(f"Report saved at: {file_path}")
        return df
    except FileNotFoundError as e:
        print(f"Error: The specified directory '{output_path}' does not exist. {e}")
    except PermissionError as e:
        print(f"Error: You do not have permissions to save file in that directory '{output_path}'. {e}")
    except Exception as e:
        print(f"There was an error during generating report: {e}")


def validation(file_path):
    """
    This function validates the file path
    :param file_path:
    :return: info if file exists
    """
    file_exists = os.path.exists(file_path)
    if not file_exists:
        print(f"There is no file at the path {file_path}")
    else:
        print(f"File at the path {file_path} exists.")


def report(file_name, output_path=".", year=None, month=None):
    """
    This function generates a csv report
    :param file_name:
    :param output_path:
    :param year:
    :param month:
    :return: csv report
    """
    try:
        launches = get_data("https://api.spacexdata.com/v4/launches")
        rockets = get_data("https://api.spacexdata.com/v4/rockets")
        df = transform_data(launches, rockets)
        print("Data before filtering:")
        print(df.head())
        df = filter_by_date(df, year=year, month=month)
        print("Data after filtering:")
        print(df.head())
        generate_report(df, file_name=file_name, output_path=output_path)
        validation(os.path.join(output_path, f"{file_name}.csv"))
    except requests.RequestException as e:
        print(f"Error during data retrieval: {e}. Check your connection with internet.")
    except Exception as e:
        print(f"There was an error: {e}")

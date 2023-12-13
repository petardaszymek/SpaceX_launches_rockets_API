from src.functions import report


def main(file_name, output_path=".", year=None, month=None):
    report(file_name=file_name, output_path=output_path, year=year, month=month)


if __name__ == '__main__':
    main(file_name="csv2020", output_path="C:/Users/User/Desktop", year=2020)

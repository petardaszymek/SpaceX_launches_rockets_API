import argparse
import os
from functions import report


def main(file_name, output_path=".", year=None, month=None):
    print(f"file_name: {file_name}")
    print(f"output_path: {output_path}")
    print(f"year: {year}")
    print(f"month: {month}")
    report(file_name=file_name, output_path=output_path, year=year, month=month)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser is an object that analyses arguments from command-line')

    parser.add_argument('--file_name', type=str, help='Specify the file name')
    parser.add_argument('--output_path', type=str, default='.',
                        help='Specify the output path (default: current directory)')
    parser.add_argument('--year', type=int, help='Specify the year')
    parser.add_argument('--month', type=int, help='Specify the month')

    args = parser.parse_args()

    main(file_name=args.file_name,
         output_path=os.path.join(args.output_path),
         year=args.year,
         month=args.month)

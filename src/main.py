import argparse
from functions import report


def main(file_name, output_path=".", year=None, month=None):
    report(file_name=file_name, output_path=output_path, year=year, month=month)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some command-line arguments')

    parser.add_argument('--file_name', type=str, help='Specify the file name')
    parser.add_argument('--output_path', type=str, default='.',
                        help='Specify the output path (default: current directory)')
    parser.add_argument('--year', type=int, help='Specify the year')
    parser.add_argument('--month', type=int, help='Specify the month')

    args = parser.parse_args()

    main(file_name=args.file_name, output_path=args.output_path, year=args.year, month=args.month)
import csv
import sys
from tabulate import tabulate


def main():
    # Check for CLA:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Try to open the file and check for existence
    try:
        with open(sys.argv[1]) as fhand:
            reader = csv.DictReader(fhand)
            element_list = []
            header_list = reader.fieldnames
            for read in reader:
                element_list.append([v for k, v in read.items()])
            print(tabulate(element_list, headers=header_list, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit(f"File {sys.argv[1]} does not exist")


if __name__ == "__main__":
    main()

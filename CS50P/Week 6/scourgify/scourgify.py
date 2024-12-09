import csv
import sys


def main():
    # Check for CLA
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit(f"Reader file {sys.argv[1]} is not a CSV file.")
    if not sys.argv[2].endswith(".csv"):
        sys.exit(f"Writer file {sys.argv[2]} is not a CSV file.")

    # Open file and manage inexistence of the reader file
    try:    
        with open(sys.argv[1]) as fhand:
            reader = csv.reader(fhand)
            new_csv_list = [["first", "last", "house"]]
            reader.__next__()
            # for each full name in the file split it into first name and last name and add it to the final list
            for elem in reader:
                (last, first) = elem[0].replace('"', '').replace(" ", "").split(',')
                new_csv_list.append([first, last, elem[1]])
            # Open a new csv file to write the new values
            with open(sys.argv[2], "w") as fwrite_hand:
                writer = csv.writer(fwrite_hand)
                for row in new_csv_list:
                    writer.writerow(row)
            
                
    # File not existent
    except FileNotFoundError:
        sys.exit("Could not read {sys.argv[1]}, file missing.")


if __name__ == "__main__":
    main()

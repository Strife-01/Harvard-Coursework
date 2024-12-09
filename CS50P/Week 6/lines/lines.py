import sys


def main():
    # Check CLA
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    # Open the file and check if it exists
    try:
        curr_line = 0
        lines = 0
        with open(sys.argv[1]) as fhand:
            # Iterate the file and count the lines that are not blank or start with #
            for line in fhand:
                curr_line += 1
                line = remove_spaces(line)
                if line.startswith('#'):
                    continue
                elif len(line) < 1:
                    continue
                lines += 1

    # Handle non existent file
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    # Print the lines
    print(f"The python file {sys.argv[1]} has exactly {lines} lines of code.")


def remove_spaces(string):
    return "".join([char for char in string if char not in [" ", "\n", "\t"]])


if __name__ == "__main__":
    main()

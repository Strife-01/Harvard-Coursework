def main() :
    height = get_int("Height: ")
    print_pyramid(height, height)


def get_int(string) :
    input_int = None
    while True :
        input_int = input(string)
        try :
            input_int = int(input_int)
            break
        except :
            print("Enter an integer number...")
            continue
    return input_int


def print_pyramid(curr_height, innitial_height) :
    if curr_height == 0 :
        return
    print_pyramid(curr_height - 1, innitial_height)
    printable_space = innitial_height - curr_height
    print(' ' * printable_space + '#' * (innitial_height - printable_space))


main()

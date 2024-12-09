import string
CHARACTERS = string.punctuation + " "


def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("VALID")
    else:
        print("INVALID")


def is_valid(plate):
    length = len(plate)
    if not (2 <= length <= 6):
        return False
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False
    if length != len([char for char in plate if char not in CHARACTERS]):
        return False
    if num_in_mid(plate):
        return False
    if first_num_0(plate):
        return False
    return True


def num_in_mid(strg):
    for char in strg[:-1]:
        if char.isnumeric() and not strg[-1].isnumeric():
            return True
    return False


def first_num_0(strg):
    nums = False
    for char in strg:
        if char.isnumeric() and char != '0':
            return False
        elif char.isnumeric() and char == '0':
            return True


if __name__ == "__main__":
    main()

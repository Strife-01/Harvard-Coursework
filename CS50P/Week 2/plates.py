def main() :
    plate = input("Plate: ").upper()
    if is_valid(plate) : print("Valid")
    else : print("Invalid")


def is_valid(s) :
    if len(s) < 2 or len(s) > 6 : return False
    if s.isalnum() is False or s[0:2].isalpha() is False : return False
    if s[2:-1].isnumeric() is True and s[-1].isnumeric() is False : return False
    for char in s :
        if char.isnumeric() : 
            if char == "0" : return False
            else : break
    return True


main()

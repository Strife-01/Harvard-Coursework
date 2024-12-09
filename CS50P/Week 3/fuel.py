def main() :
    fuel = get_fraction()
    percentage = int(100 * fuel[0] / fuel[1])
    if percentage <= 1 : percentage = 'E'
    elif percentage >= 99 : percentage = 'F'
    else : percentage = str(percentage) + '%'
    print(f"{percentage}")


def get_fraction() :
    while True :
        fraction = input("Fraction: ")
        fraction_comp = fraction.split('/')
        try :
            numerator = int(fraction_comp[0])
            denominator = int(fraction_comp[1])
        except IndexError : pass
        except ValueError : pass
        else :
            if denominator != 0 :
                return [numerator, denominator]
            else : pass


main()

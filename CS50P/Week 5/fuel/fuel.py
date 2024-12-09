def main():
    fraction = input("Fraction X/Y: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    # get the individual fraction components
    elements = fraction.split('/')
    numerator = elements[0]
    denominator = elements[1]

    # convert them into integer
    try:
        numerator = int(numerator)
    except:
        return "NUMERATOR_NOT_A_NUMBER"

    try:
        denominator = int(denominator)
    except:
        return "DENOMINATOR_NOT_A_NUMBER"
    
    # create the percentage and return it
    return numerator * 100 // denominator


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

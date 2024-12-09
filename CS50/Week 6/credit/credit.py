import re


def main() :
    number = get_string("Card number: ")
    card_type = get_type(number)
    if is_valid(card_type, number) == True : print(card_type)
    else : print("INVALID")


def get_string(string) :
    return input(string)


def get_type(number) :
    if re.fullmatch('^5[1-5][0-9]{14}$', number) != None : return 'MASTERCARD'
    elif re.fullmatch('^3[4|7][0-9]{13}$', number) != None : return 'AMEX'
    elif re.fullmatch('^4[0-9]{12}$', number) != None : return 'VISA'
    elif re.fullmatch('^4[0-9]{15}$', number) != None : return 'VISA'
    else : return 'INVALID'


def is_valid(card_type, card_number) :
    match card_type :
        case 'INVALID' : return False
        case 'VISA' : return True if digit_sum(card_number) % 10 == 0 else False
        case 'MASTERCARD' : return True if digit_sum(card_number) % 10 == 0 else False
        case 'AMEX' : return True if digit_sum(card_number) % 10 == 0 else False


def digit_sum(card_number) :
    card_number = int(card_number)
    sum_1 = 0
    sum_2 = 0
    while card_number > 0 :
        num_1 = card_number % 10
        sum_1 += num_1

        card_number //= 10

        num_2 = (card_number % 10) * 2
        num_2 = num_2 if num_2 <= 9 else num_2 % 10 + num_2 // 10
        sum_2 += num_2

        card_number //= 10
    return sum_1 + sum_2


main()

change = {
    "quarters" : 25,
    "dimes" : 10,
    "nickels" : 5,
    "pennies" : 1,
        }


def main() :
    change_num = int(get_float("Change: ") * 100)
    nr_coins = get_coins(change_num)
    print(nr_coins)


def get_float(string) :
    number = None
    while True:
        number = input(string)
        try :
            number = float(number)
            if number < 0 : continue
            break
        except : continue
    return number


def get_coins(change_num) :
    quarters = get_nr_coins(change_num, change["quarters"])
    change_num -= quarters * change["quarters"]
    dimes = get_nr_coins(change_num, change["dimes"])
    change_num -= dimes * change["dimes"]
    nickels = get_nr_coins(change_num, change["nickels"])
    change_num -= nickels * change["nickels"]
    pennies = get_nr_coins(change_num, change["pennies"])
    nr_coins = quarters + dimes + nickels + pennies
    return nr_coins


def get_nr_coins(change_num, change_obj) :
    nr_coins = 0
    change = change_num
    while change >= change_obj :
        nr_coins += 1
        change -= change_obj
    return nr_coins


main()

def main() :
    groceries = get_dict()
    for (k, v) in sorted(groceries.items()) :
        print(v, k.upper())


def get_dict() :
    dictionary = dict()
    while True :
        try :
            inpt = input()
        except EOFError : return dictionary
        except KeyboardInterrupt : return dictionary
        else : 
            if inpt.isalnum() : dictionary[inpt] = dictionary.get(inpt, 0) + 1
            else : continue


main()

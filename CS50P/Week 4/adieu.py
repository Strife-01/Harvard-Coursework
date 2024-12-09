#!/usr/bin/python


import sys


def main() :
    names = get_names()
    otp = "Adieu, adieu, to"
    if len(names) == 1 : otp += " " + names[0]
    elif len(names) == 2 : otp += " " + names[0] + " and " + names[1]
    elif len(names) > 2 :
        for name in names[:-1] :
            otp += " " + name + ","
        otp += " and " + names[-1]
    else : sys.exit("NO_NAMES_FOUND")
    print(otp)


def get_names() :
    names = []
    while True :
        try :
            name = input("Name: ")
            if len(name) < 1 : continue
            names.append(name)
        except EOFError : break
    return names


if __name__ == "__main__" :
    main()

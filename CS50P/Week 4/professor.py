#!/usr/bin/python


import random
import sys


LEVELS = [1, 2, 3]
SIGNS = ["+", "-", "*", "/", "//", "%"]
PROBLEMS = 10
TRIES_PER_PROBLEM = 3


def main():
    level = get_level()
    sign = get_sign()
    problem = 0
    score = 0
    while problem < PROBLEMS:
        trie = 0
        win = True
        x = generate_integer(level)
        y = generate_integer(level)
        answer = get_answer(x, y, sign)
        if answer == None:
            continue
        while trie <= TRIES_PER_PROBLEM:
            if trie == TRIES_PER_PROBLEM:
                win = False
                break
            try:
                inpt = int(input(f"{x} {sign} {y} = "))
            except ValueError:
                print("EEE")
                trie += 1
            except EOFError:
                sys.exit("\nExit Game")
            else:
                trie += 1
                if inpt == answer:
                    score += 1
                    break
                else:
                    print("EEE")
        if win == False:
            print(f"{x} {sign} {y} = {answer}")
        problem += 1
    print(score)


def get_level():
    while True:
        try:
            inpt = int(input("Level: "))
            if inpt in LEVELS:
                return inpt
            else:
                continue
        except ValueError:
            continue
        except EOFError:
            sys.exit("\nExit Game")


def get_sign():
    while True:
        inpt = input("Chose between + - * / // %: ")
        if inpt in SIGNS:
            return inpt
        else:
            continue


def generate_integer(nr_digits):
    if nr_digits == 1:
        low = 0
    else:
        low = 10 ** (nr_digits - 1)
    high = 10**nr_digits
    return random.randrange(low, high)


def get_answer(x, y, sign):
    if sign == "+":
        return x + y
    if sign == "-":
        return x - y
    if sign == "*":
        return x * y
    if sign == "/":
        try:
            return x / y
        except:
            return None
    if sign == "//":
        try:
            return x // y
        except:
            return None
    if sign == "%":
        try:
            return x % y
        except:
            return None


if __name__ == "__main__":
    main()

#!/usr/bin/python


from random import randrange as rr
import sys


def main() :
    upper_bound = get_int() + 1
    answer = rr(1, upper_bound)
    while True :
        try : guess = int(input("Guess: "))
        except ValueError : continue
        except EOFError : sys.exit("\nEXIT GAME")
        else :
            if guess < answer : print("Too small!")
            elif guess > answer : print("Too large!")
            else :
                print("Just right!")
                break


def get_int() :
    while True :
        try : return int(input("Lever: "))
        except ValueError : continue
        except EOFError : sys.exit("\nEXIT GAME")

if __name__ == "__main__" : main()

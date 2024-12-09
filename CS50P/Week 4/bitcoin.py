#!/usr/bin/python


import json
import requests
import sys


def main():
    if len(sys.argv) == 2 and is_float(sys.argv[1]):
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        print(
            f'${(float(r["bpi"]["USD"]["rate"].translate(str.maketrans("", "", ","))) * float(sys.argv[1])):,.4f}'
        )


def is_float(num):
    try:
        num = float(num)
        return num
    except:
        return False


if __name__ == "__main__":
    main()

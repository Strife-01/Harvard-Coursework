#!/usr/bin/python


import sys
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(string):
    if ip := re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", string):
        ip_comp = ip.groups()
        for comp in ip_comp:
            if not 0 <= int(comp) <= 255:
                return False
    else:
        return False
    return True


if __name__ == "__main__":
    main()

#!/usr/bin/python3
import re


def main() :
    curr_time = input("What time is it? ")
    time = convert(curr_time)
    if 7.00 <= time <= 8.00 : print("breakfast time")
    elif 12.00 <= time <= 13.00 : print("lunch time")
    elif 18.00 <= time <= 19.00 : print("dinner time")


def convert(time) :
    time_str = re.findall("\d{1,2}:\d{1,2}", time)
    s_f = re.findall("p\.m\.", time)
    if len(time_str) > 0 :
        content = time_str[0].split(':')
        if len(s_f) > 0 : return float(content[0]) + 12 + float(content[1]) / 60
        else : return float(content[0]) + float(content[1]) / 60


if __name__ == "__main__" :
    main()

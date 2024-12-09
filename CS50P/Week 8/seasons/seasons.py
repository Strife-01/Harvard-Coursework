#!/usr/bin/python


from datetime import date
from datetime import timedelta
import inflect
import re
import sys


def main():
    if birth_date := re.match(r"(\d{4}-\d{2}-\d{2})", input("Enter birthday in yyyy-mm-dd format: ")):
        diff = date.today() - date.fromisoformat(birth_date.string)
        p = inflect.engine()
        print(f"{p.number_to_words(int(diff.days) * 24 * 60)} minutes")
    else:
        raise ValueError("Date in the wrong format")


if __name__ == "__main__":
    main()

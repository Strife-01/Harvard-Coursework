import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    words = re.split(r"[^a-z0-9]+", s, maxsplit=0, flags=re.IGNORECASE)
    for word in words:
        if word.lower() == "um":
            count += 1
    return count


if __name__ == "__main__":
    main()

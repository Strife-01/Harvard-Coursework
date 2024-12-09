def main():
    ipt = input("Text: ")
    print(shorten(ipt))


def shorten(word):
    return "".join([letter for letter in word if letter not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'i', 'O', 'U']])


if __name__ == "__main__":
    main()

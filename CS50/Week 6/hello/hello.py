def main() :
    name = input("What's your name? ")
    if len(name) < 1 : name = 'world'
    print(f"Hello, {name}.")


main()

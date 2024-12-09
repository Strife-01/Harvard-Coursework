MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main() :
    total = 0
    while True :
        try : total += MENU[input("Item: ").title()]
        except KeyError : pass
        except EOFError : 
            print()
            break
        except KeyboardInterrupt :
            print()
            break
    print(f"Total: {total}")


main()

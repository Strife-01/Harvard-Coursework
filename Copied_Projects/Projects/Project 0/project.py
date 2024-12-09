import csv


def main():
    while True:
        menu()
        break


def menu():
    # Prompt the user for an option until valid
    while True:
    
        # The app's feature list
        OPTIONS = ("p", "t", "d", "s", "r", "y")

        # Formated option string
        CHAR_NUM = 60

        # User's menu selection
        print("WHAT DO YOU WANT TO DO?")
        print(r"(If you haven't already, make your termianl window big, so that you can see what's to come..)")
        print(format("To register a NEW PRODUCT, type", f".<{CHAR_NUM}s"), "P")
        print(format("To book a NEW TRADE, type", f".<{CHAR_NUM}s"), "T")
        print(format("To get DETAILS of a PRODUCT, type", f".<{CHAR_NUM}s"), "D")
        print(format("To SEARCH for TRADES, type", f".<{CHAR_NUM}s"), "S")
        print(format("To generate a PORTFOLIO REPORT, type", f".<{CHAR_NUM}s"), "R")
        print(format("To get the YIELD of a product given a price, type", f".<{CHAR_NUM}s"), "Y")

        # Get user's choice
        choice = input("Your choice: ").lower()

        # Check user's input
        if choice not in OPTIONS:
            print("Please select a valid option...")
            continue
        else:
            break
        
    match choice:
        case "p":
            register_new_product()
        case "t":
            book_new_trade()
        case "d":
            get_details_of_product()
        case "s":
            search_trades()
        case "r":
            generate_portfolio_report()
        case "y":
            get_yield_of_product()
        case _:
            ...


def register_new_product():
    ...


def book_new_trade:
    ...


def get_details_of_product():
    ...


def search_trades():
    ...


def generate_portfolio_report():
    ...


def get_yield_of_product():
    ...


if __name__ == "__main__":
    main()

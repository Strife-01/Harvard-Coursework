COKE_PRICE = 50 


def main() :
    amount_due = COKE_PRICE
    while amount_due > 0 :
        print(f"Amount Due: {amount_due}")
        amount_curr = get_coin()
        amount_due -= amount_curr
    print("Change Owed: 0")


def get_coin() :
    accepted_coins = [5, 10, 25]
    while True :
        coin = input("Insert Coin: ")
        try : 
            coin = int(coin)
        except : continue
        if coin not in accepted_coins : continue
        break
    return coin


main()

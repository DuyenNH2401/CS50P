amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    in_coin = int(input("Insert Coin: "))
    if in_coin == 25 or in_coin == 10 or in_coin == 5:
        amount_due -= in_coin
else: print(f"Change Owed: {-amount_due}")

if __name__ == '__main__':
    
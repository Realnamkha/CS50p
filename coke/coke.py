print('Amount Due : 50')
amount = 50
amount_inserted = int(input("Insert Coint :"))
amount_accepted = [25,10,5]
for amount_inserted in amount_accepted:
    amount = amount - amount_inserted
    print(f"Amount Due:{amount}")


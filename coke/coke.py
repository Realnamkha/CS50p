amount_due = 50
amount_inserted = int(input("Insert Coint :"))
amount_accepted = [25,10,5]
while amount_due>=0:
    if amount_inserted in amount_accepted:
        amount_due = amount_due - amount_inserted
        print(f"Amount Due:{amount}")


amount_due = 50
amount_accepted = [25,10,5]
while amount_due>0:
    print(f"Amount Due: {amount_due}")
    amount_inserted = int(input("Insert Coint :"))
    if amount_inserted in amount_accepted:
        amount_due = amount_due - amount_inserted
if amount_due<=0:
    print(f"Change Owed: {amount_due * -1}")


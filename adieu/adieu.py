import inflect
p = inflect.engine()
while True:
    try:
        user = input("NAME : ")

    except EOFError:
            break
print(f"\nAdieu, adieu, to {user}")
import inflect
p = inflect.engine()
while True:
    try:
        user = input("NAME : ").split("\n")

    except EOFError:
            break
print(f"\nAdieu, adieu, to {user[0] ,user[1], user[2]}")
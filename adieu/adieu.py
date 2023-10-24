import inflect
p = inflect.engine()
user = []
while True:
    try:
        user += input("NAME : ").split("\n")

    except EOFError:
            break

if len(user) == 1:
        print(f"Adieu, adieu, to {user[0]}")
elif len(user) == 2:
        print(f"Adieu, adieu, to {user[0]} and {user[1]}")
else:
    farewell = f"Adieu, adieu, to {', '.join(user[:-1])}, and {user[-1]}!"
    farewell = farewell.replace(", ", ", " * (len(user) - 2))
    print(farewell)
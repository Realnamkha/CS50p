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
    farewell = f"Adieu, {', '.join(names[:-1])}, and {names[-1]}!"
    farewell = farewell.replace(", ", ", " * (len(names) - 2))
    print(farewell)
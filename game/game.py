import random
while True:
    try:
        Level = int(input("Enter a positive number"))
        if(Level<0):
            continue
        number = random.randint(1, Level)
    except ValueError:
        pass


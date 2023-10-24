import random
while True:
    try:
        n = int(input("Enter a positive number"))
        if(n<0):
            continue
    except ValueError:
        pass
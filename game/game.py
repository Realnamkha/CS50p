import random
import sys
level = -1
while (level<0):
    try:
        level = int(input("Level :"))
    except ValueError:
        pass

while True:
    try:
        number = random.randint(1, level)
        Guess = int(input("Guess: "))
        if(Guess<0):
            continue
        if(Guess < number):
            print("Too small!")
        elif(Guess > number):
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()
    except ValueError:
        pass


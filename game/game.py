import random
import sys
while True:
    try:
        Level = int(input("Enter a positive number"))
        if(Level<0):
            continue
        number = random.randint(1, Level)
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


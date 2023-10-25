import random


def main():
    level=get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level :"))
            if ((level == 1) or (level == 2) or (level == 3)):
                break
        except ValueError:
            pass
    return level


def generate_integer(level):
    chance = 1
    score = 0
    for _ in range(10):
        if (level == 1):
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif (level == 2):
            x = random.randint(10,99)
            y = random.randint(10,99)
        else:
            x = random.randint(9,999)
            y = random.randint(9,999)
        while (True):
            print(f"{x} + {y} = ",end=" ")
            z = input()
            if (str(x+y) == z):
                score += 1
                break
            elif ((str(x+y) != z) and (chance !=3)):
                print("EEE")
                chance = chance + 1
                print(chance)
            else:
                print("EEE")
                print(f"{x} + {y} = {x+y}")
                chance = 1
                break

    print("Score : {score}")
if __name__ == "__main__":
    main()
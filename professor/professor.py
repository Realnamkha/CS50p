import random


def main():
    ...


def get_level():
    while True:
        try:
            level = int(input("Level :"))
            if ((level == 1) or (level == 2) or (level == 3)):
                break
        except ValueError:
            pass


def generate_integer(level):
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
        while True:
            chance = 3
            print(f"{x} + {y} = ",sep=" ")
            z = int(input())
            if (x+y == z):
                score += 1
                break
            elif (x+y != z):
                chance -= 1
                if (chance == 3):
                    print(f"{x} + {y} = {x+y} ",sep=" ")

if __name__ == "__main__":
    main()
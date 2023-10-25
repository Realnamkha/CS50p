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
    # X = random.randint(0,9)
    # Y = random.randint(0,9)
    # print(f"{X} + {Y} = ")
    # Z = int(input())
    # if (X+Y == Z):
    #     score += 1
    # else:
    #     continue

if __name__ == "__main__":
    main()
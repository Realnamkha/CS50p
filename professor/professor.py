import random


def main():
    ...


def get_level():
    level = -1
    while (level<0):
        try:
            level = int(input("Level :"))
        except ValueError:
            pass


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
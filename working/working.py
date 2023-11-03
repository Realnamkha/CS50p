import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.fullmatch(r"[0-9]|1[1-2] (AM)? to [0-9]|1[1-2] (PM)?")


...


if __name__ == "__main__":
    main()

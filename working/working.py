import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.fullmatch(r"[0-9]|1[1-2]:[0-5][0-9] AM to [0-9]|1[1-2][0-5][0-9] PM")


...


if __name__ == "__main__":
    main()

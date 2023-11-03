import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s=s.strip()
    matches = re.fullmatch(r"((0?[1-9]|1[0-2]):[0-5][0-9] [AP][M]) to ((0?[1-9]|1[0-2]):[0-5][0-9] [AP][M])",s)
    if matches:
        time1 = matches.group(1)
        time2 = matches.group(3)
        if "AM" in time1:
            
    else:
        return ValueError

...


if __name__ == "__main__":
    main()

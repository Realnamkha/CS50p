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
        if "AM" in time1 and "PM" in time2:
            time1 = time1[:-2].strip()
            time2 = time2[:-2].strip()
            hours,minutes = time2.split(":")
            hours = int(hours) + 12
            time2 = f"{hours}:{minutes}"
            return f"{time1} to {time2}"
        else:
            time2 = time2[:-2].strip()
            time1 = time1[:-2].strip()
            hours,minutes = time1.split(":")
            hours = int(hours) + 12
            time1 = f"{hours}:{minutes}"
            return f"{time1} to {time2}"

    else:
        raise ValueError:
            return f"value Error"

...


if __name__ == "__main__":
    main()

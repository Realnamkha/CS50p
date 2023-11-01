import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    print(s)
    matches = re.search(r"^https?://(www.)?youtube\.com/embed/([A-Za-z0-9])$", s, re.IGNORECASE)
    if matches:
        print(matches.group(2))


if __name__ == "__main__":
    main()

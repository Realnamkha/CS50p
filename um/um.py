import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    x = re.search(r'\bum\b', s,re.IGNORECASE)

    if x:
        print("Match found:", x.group())
    else:
        print("No match found")


if __name__ == "__main__":
    main()

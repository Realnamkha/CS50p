import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    if "um" in s:
        count +=1
    return count


if __name__ == "__main__":
    main()

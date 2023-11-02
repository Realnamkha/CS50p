import re
import sys
from bs4 import BeautifulSoup


def main():
    print(parse(input("HTML: ")))


def parse(s):
    soup = BeautifulSoup(s, 'html.parser')
    iframe_element = soup.find('iframe')
    src_value = iframe_element.get('src')
    matches = re.search(r"^https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9]+)$", src_value, re.IGNORECASE)
    if matches:
        print(f"https://youtu.be/{matches.group(1)}")


if __name__ == "__main__":
    main()

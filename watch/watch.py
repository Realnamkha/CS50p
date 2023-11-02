import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # soup = BeautifulSoup(s, 'html.parser')
    # iframe_element = soup.find('iframe')
    # src_value = iframe_element.get('src')
    matches = re.search(r"https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9]+)", s, re.IGNORECASE)
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return f"None"


if __name__ == "__main__":
    main()

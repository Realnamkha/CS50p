import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # soup = BeautifulSoup(s, 'html.parser')
    # iframe_element = soup.find('iframe')
    # src_value = iframe_element.get('src')
    matches = re.search(r"<iframe.*?src=['\"](https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9]+))['\"].*</iframe>", s, re.IGNORECASE)
    if matches:
        return f"https://youtu.be/{matches.group(2)}"
    else:
        return f"None"


if __name__ == "__main__":
    main()

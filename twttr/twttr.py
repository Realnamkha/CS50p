def main():
    string = input("Enter the string ").strip()
    print(shorten(string))


def shorten(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    word = ""
    for char in word:
        if char not in vowels:
            word +=char
    return word


if __name__ == "__main__":
    main()

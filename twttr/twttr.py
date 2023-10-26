def main():
    string = input("Enter the string ").strip()
    print(shorten(string))

def shorten(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    new_word = ""
    for char in word:
        if char not in vowels:
            new_word +=char
    return new_word


if __name__ == "__main__":
    main()

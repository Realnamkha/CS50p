def main():
    Greetings = input("Enter your greetings: ")
    print(value(Greetings))

def value(Greetings):
    Greetings = Greetings.strip().lower()
    if Greetings.startswith("hello"):
        return "$0"
    elif Greetings.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()

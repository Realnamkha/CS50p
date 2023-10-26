def main():
    Greetings = input("Enter your greetings: ").lower().strip()
    print(value(Greetings))

def value(Greetings):
    if Greetings.startswith("hello"):
        return "$0"
    elif Greetings.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()

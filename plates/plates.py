def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for char in s:
        if (char[0] and char[1]) == ['A'-'Z','a'-'z]


main()

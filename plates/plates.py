def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha():
        return True
    if(6<=len(s)<=2):
        return True
    for char in s:
        if char.isnumeric():
            if char[0] == 0:
                return False

main()


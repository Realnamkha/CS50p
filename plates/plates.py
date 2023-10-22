def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = False
    if (2<=len(s)<=6):
        if s.isalpha():
            valid = True
        elif s.isalnum() and s[:2].isalpha():
                for char in s[2:]:
                    if char.isdigit():
                        first_num = s.index(char)

                        if s[first_num:].isdigit() and char != '0':
                            valid = True
                        else:
                            valid = False
    return valid


if __name__ == "__main__":
    main()
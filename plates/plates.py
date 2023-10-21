def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def first_num(s):
    for character in s:
        if character.isnumeric():
            if character=='0':
                return False
            break


def is_valid(s):
    valid = False
    if len(s) > 1 and len(s) < 7:
        start = s[0:2]
        if s.isalpha():
            valid = True
        elif s.isalnum() and start.isalpha():
            if not s[-1].isalpha():
                for character in s[2:]:
                    if character.isalpha():
                        continue
                    elif(first_num(s) == True):
                        valid = True

                    elif character.isdigit():
                        valid = True
                    break
    return valid


if __name__ == "__main__":
    main()
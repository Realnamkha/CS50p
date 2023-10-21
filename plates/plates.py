def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def first_num(s):
    first_num=len(s)-1
    for character in s:
        if character.isnumeric():
            # check if first number is zero
            if character=='0':
                return False
            first_num = s.index(character)
            break
        return first_num

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
                    elif character.isdigit() and character != "0":
                        valid = True
                    break
    return valid


if __name__ == "__main__":
    main()
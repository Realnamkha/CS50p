def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = False
    if (6<=len(s)<=2):
        valid = True

    elif not s.isalnum():
        valid = False

    elif (s[0].isalpha() and s[1].isalpha()):
        valid = True

    first_num=len(s)-1
    for character in s:
        if character.isnumeric():
            if character=='0':
                valid = False
            first_num = s.index(character)
            break
    for character in s:
        if s.index(character)<= first_num:
            pass
        else:
            if character.isalpha():
                valid = False
    return valid


main()

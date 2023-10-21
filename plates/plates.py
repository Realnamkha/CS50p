def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if(6<=len(s)<=2):
        start = s[:2]

        if s.isalpha():
            return True
        elif s.isalnum() and start.isalpha():
            if not s[-1].isalpha():
                for char in s[2:]:
                      if char.isalpha():
                        continue
                      elif char.isnumeric()


main()


from datetime import date, datetime
import inflect
import sys
import re

p = inflect.engine()

class Time:
    def __init__(self, target_date):
        self.target_date  = target_date

    def __str__(self):
        # prints out the output at the end

    # operator overload
    def __sub__(self, other):
        # perform the subtraction and return the result

    @staticmethod
    def validate_date(target_date):
        date = target_date.strip()
        if check := re.search(r"^([0-9]{4})\-([0-9]{2})\-([0-9]{2})$",date):
            year = int(check.group(1))
            month = int(check.group(2))
            day = int(check.group(3))
            if month <= 12 and day <= 31 :
                return True
            else:
                sys.exit("Invalid date format")
        else :
            sys.exit("Invalid date format")

    @classmethod
    def get(cls):
        birth_date = input("Enter Your DOB :")
        valid = validate_date(birth_date)
        # if valid, pass in that user input the cls, otherwise exit using sys.exit() with an error message
        # Remember datetime.strptime allows you to turn a string into a DateTime object to make it easier for math operations

def main():
    then = Time.get()

    # gets the current date so no need to ask the user
    now = Time(date.today())
    print(now - then)

if _name_ == "__main__":
    main()

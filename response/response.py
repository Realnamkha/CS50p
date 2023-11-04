from validator_collection import validators, checkers, errors
import sys


def main():
    print(check_valid(input("Enter your email address: ")))


def check_valid(email_address):
    try:
        email_address = validators.email(email,allow_empty = True)
        is_email_address = checkers.is_email(email_address)
    except errors.EmptyValueError:
        sys.exit("Invalid")
    except errors.InvalidEmailError:
        sys.exit("Invalid")

if __name__ == "__main__":
    main()

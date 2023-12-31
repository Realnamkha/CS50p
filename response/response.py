from validator_collection import validators, checkers, errors
import sys


def main():
    print(check_valid(input("Enter your email address: ")))


def check_valid(email_address):
    try:
        email_address = validators.email(email_address,allow_empty = True)
        is_email_address = checkers.is_email(email_address)
        if is_email_address:
            return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()

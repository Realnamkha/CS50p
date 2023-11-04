from validator_collection import validators, checkers, errors
import sys


def main():
    print(check_valid(input("Enter your email address: ")))


def check_valid(email):
    email_address = validators.email(email,allow_empty = True)

if __name__ == "__main__":
    main()

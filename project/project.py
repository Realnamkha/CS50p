import sys
import csv

def record_expense():
    expense_amount = input("Enter the amount spent :")
    week_day = input("Enter the day of expenditure :")
    month = 
    print("Please Select the Category ")
    print("1.1 Food")
    print("1.2 Stationary")
    print("1.3 Travel")
    print("1.4 Entertainment")
    print("1.5 Others")


def view_expense():
    print("View_expense")


def delete_expense():
    print("Delete expense")

def main():
    while True:
        print("Welcome to Expense Tracker")
        print("1. Record Expense ")
        print("2. View Expense ")
        print("3. Delete Expense ")
        print("4. Exit ")

        choice = input("Enter your choice\n")

        match choice:
            case "1":
                record_expense()
                break
            case "2":
                view_expense()
                break
            case "3":
                delete_expense()
                break
            case "4":
                sys.exit("System exited ")
            case _:
                print("Enter a valid choice")

if __name__ == "__main__":
    main()

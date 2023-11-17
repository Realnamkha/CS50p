import sys
import csv

def record_expense():
    expense_amount = input("Enter the amount spent :")
    week_day = input("Enter the day of expenditure :")
    print("***Categories*** ")
    print("1 Food")
    print("2 Stationary")
    print("3 Travel")
    print("4 Entertainment")
    print("5 Others")
    category_input = input("Please select the category (1-5): ")
    if category_input == "1":
        category = "Food"
    elif category_input == "2":
        category = "Stationary"
    elif category_input == "3":
        category = "Travel"
    elif category_input == "4":
        category = "Entertainment"
    elif category_input == "5":
        category = "Others"
    else:
        print("Invalid Selection")

    with open("records.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["expense_amount", "week_day", "category"])
        writer.writeheader()
        writer.writerow({"expense_amount": expense_amount, "week_day": week_day,"category":category})

def view_expense():
    print("***View_Expenses***")
    with open("records.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_expense = r
    print("1 Total Expenses :",)
    print("2 Stationary")


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

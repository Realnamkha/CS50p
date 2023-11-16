import sys
def record_expense():
    print("record_expense")


def view_expense():
    print("View_expense")


def delete_expense():
    print("Delete expense")

def main():
        print("Welcome to Expense Tracker")
        print("1. Record Expense ")
        print("2. View Expense ")
        print("3. Delete Expense ")
        print("4. Exit ")
    while True:
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
            case "_":
                print("Enter a valid choice")

if __name__ == "__main__":
    main()

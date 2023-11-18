import sys
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from prettytable import PrettyTable
def record_expense():
    expense_amount = input("Enter the amount spent :").strip()
    week_day = input("Enter the day of expenditure :").lower().strip()
    print("***Categories*** ")
    print("1 Food")
    print("2 Stationary")
    print("3 Travel")
    print("4 Entertainment")
    print("5 Others")
    category_input = input("Please select the category (1-5): ").strip()
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
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({"expense_amount": expense_amount, "week_day": week_day,"category":category})

    main()

def view_expense():
    print("***View_Expenses***")
    with open("records.csv") as file:
        reader = csv.DictReader(file)
        total_expense = 0
        expense_by_category = {}
        for row in reader:
            expense_amount = int(row["expense_amount"])
            total_expense += expense_amount
            category = row["category"]
            expense_by_category[category] = expense_by_category.get(category, 0) + expense_amount
    print(f"Total Expenses :{total_expense}")
    print("Expense by Category:")
    for category, category_expense in expense_by_category.items():
            print(f"{category}: {category_expense}")

    main()

def delete_expense():
    amount, category, day = input("Enter the amount to be deleted, category, and day (separated by spaces): ").split()
    rows_to_keep = []
    with open("records.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (row["expense_amount"]==amount and row["week_day"]==day and row["category"]==category ):
                continue
            else:
                rows_to_keep.append(row)
    fieldnames = reader.fieldnames
    with open("records.csv", mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(rows_to_keep)
        print("Deleted successfully")
    main()

def view_stats():
    df = pd.read_csv('records.csv')
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
    sns.barplot(x='week_day', y='expense_amount', data=df, hue='category', ax=axes[0, 0])
    axes[0, 0].set_title('Expense by Week Day')


    sns.barplot(x='category', y='expense_amount', data=df, hue='category', ax=axes[0, 1])
    axes[0, 1].set_title('Expense by Category')


    sns.boxplot(x='category', y='expense_amount', data=df, ax=axes[1, 0])
    axes[1, 0].set_title('Expense Distribution by Category')


    sns.histplot(df['expense_amount'], bins=20, kde=True, ax=axes[1, 1])
    axes[1, 1].set_title('Expense Distribution')


    plt.tight_layout()
    plt.show()

    main()
def main():
    while True:
        menu_table = PrettyTable()
        menu_table.field_names = ["Option", "Description"]

        menu_table.add_row(["1", "Record Expense"])
        menu_table.add_row(["2", "View Expense"])
        menu_table.add_row(["3", "Delete Expense"])
        menu_table.add_row(["4", "View Stats"])
        menu_table.add_row(["5", "Exit"])
        print("Welcome to Expense Tracker")
        print(menu_table)

        choice = input("Enter your choice\n").strip()

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
                view_stats()
                break
            case "5":
                sys.exit("System exited ")
            case _:
                print("Enter a valid choice")

if __name__ == "__main__":
    main()

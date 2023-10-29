import sys
import csv
from tabulate import tabulate
menu = []
try:
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        if (file_name[-4:] == ".csv"):
            with open(file_name) as file:
                 reader = csv.DictReader(file)
                 for row in reader:
                    menu.append({"Regular Pizza": row["Regular Pizza"],
                                 "Small": row["Small"],
                                 "Large":row["Large"]})

            print(tabulate((menu),headers="keys",tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")
    else:
        sys.exit("More or few arguments")
except FileNotFoundError:
    sys.exit("File does not exist")


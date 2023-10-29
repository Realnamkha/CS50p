import sys
from tabulate import tabulate
menu = []
try:
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        if (file_name[-4:] == ".csv"):
            with open(file_name) as file:
                 reader = csv.DictReader(file)
                for row in reader:
                    menu.append({"pizza": row["Regular Pizza"], "small": row["Small"]},{"large":row["Large"]})

        else:
            sys.exit("Not a CSV file")
    else:
        sys.exit("More or few arguments")
except FileNotFoundError:
    sys.exit("File does not exist")

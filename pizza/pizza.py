import sys
from tabulate import tabulate
try:
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        if (file_name[-4:] == ".csv"):
            with open(file_name) as file:
                lines = file.readlines()

        else:
            sys.exit("Not a CSV file")
    else:
        sys.exit("More or few arguments")
except FileNotFoundError:
    sys.exit("File does not exist")

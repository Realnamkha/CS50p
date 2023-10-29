import sys
import csv
from tabulate import tabulate
def get_filename(arguments):
    if len(arguments) != 2:
        if len(arguments) < 2:
            exit('Too few command-line arguments')
        else:
            exit('Too many command-line arguments')
    else:
        return sys.argv[1]


def check_csv(file_name):
     if (file_name[-4:] != ".csv"):
         sys.exit("Not a csv file")

def main():
    file_name = get_filename(sys.argv)
    check_csv(file_name)
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            headers = list(next(reader))
            menu = []
            for row in reader:
                menu.append([row[0],row[1],row[2]])
        print(tabulate((menu),headers,tablefmt="grid"))
    except FileNotFoundError:
            sys.exit("File does not exist")

if __name__ == '__main__':
    main()

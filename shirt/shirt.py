import sys
import csv

def get_filename(arguments):
    if len(arguments) != 3:
        if len(arguments) < 3:
            sys.exit('Too few command-line arguments')
        else:
            sys.exit('Too many command-line arguments')
    else:
         return [sys.argv[1],sys.argv[2]]


def check_csv(file_name):
     if (file_name[-4:] != ".csv"):
         sys.exit("Not a csv file")

import sys
import csv

def get_filename(arguments):
    if len(arguments) != 3:
        if len(arguments) < 3:
            exit('Too few command-line arguments')
        else:
            exit('Too many command-line arguments')
    else:
        return sys.argv[1]

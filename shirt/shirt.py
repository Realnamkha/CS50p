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
     file_name = file_name.lower()
     if (file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png")):
         pass
     else:
         sys.exit("File name not correct extension")

def check_extension(file_name):
    index = file_name.find(".")

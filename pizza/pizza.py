import sys
try:
    if len(sys.argv) == 2 and (file_name[-4:] == ".csv")::
        file_name = sys.argv[1]
    else:
        sys.exit("More or few arguments")
except FileNotFoundError:
    sys.exit("File does not exist")

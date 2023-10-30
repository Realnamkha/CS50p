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


def check_extension(file_name):
     file_name = file_name.lower()
     if (file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png")):
         pass
     else:
         sys.exit("File name not correct extension")

def check_extension(input_name,output_name):
    index1 = input_name.find(".")
    index2 = output_name.find(".")

    if (input_name[index1:] != output_name[index2:]):
        sys.exit("Input and Output extensions are not equal")


def main():
    input_name,output_name = get_filename(sys.argv)
    check_extension(input_name)
    check_extension(output_name)
    try:
        with open(input_name) as file:
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



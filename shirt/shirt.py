import sys
import csv
import os
from PIL import Image,ImageOps

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

def check_equal(input_name,output_name):
    index1 = input_name.find(".")
    index2 = output_name.find(".")

    if (input_name[index1:] != output_name[index2:]):
        sys.exit("Input and Output extensions are not equal")


def main():
    input_name,output_name = get_filename(sys.argv)
    check_extension(input_name)
    check_extension(output_name)
    check_equal(input_name,output_name)
    try:
        muppet = Image.open(input_name)
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        exit('Input does not exist')

    size = shirt.size
    muppet = ImageOps.fit(muppet, size)
    muppet.paste(shirt, shirt)
    muppet.save(output_name)
if __name__ == '__main__':
    main()



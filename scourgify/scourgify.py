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

def main():
    read_file,write_file = get_filename(sys.argv)
    first_names=[]
    last_names=[]
    houses=[]
    try:
        with open(read_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last , first = row["name"].split(',')
                first_names.append(first.strip())
                last_names.append(last.strip())
                houses.append(row["house"])
    except FileNotFoundError:
        exit('File does not exist')


    with open(write_file,"w") as file:
           writer = csv.DictWriter(file, fieldnames=["first","last","house"])
           writer.writeheader()
           for student in range(len(houses)):
                    writer.writerow({"first": first_names[student],"last": last_names[student],"house": houses[student]})

if __name__ == '__main__':
    main()

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
    students = []
    try:
        with open(read_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last , first = row["name"].split(',')
                row["first"] = first
                row["last"] = last
                students.append(row)
    except FileNotFoundError:
        exit('File does not exist')


    with open(write_file,"w") as file:
           writer = csv.DictWriter(file, fieldnames=["first","last","house"])
           writer.writeheader()
           for student in students:
                    writer.writerow({"first": student['first'],"last": student['last'],"house": student['house']})

if __name__ == '__main__':
    main()

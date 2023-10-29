import sys
import csv

# def get_filename(arguments):
#     if len(arguments) != 3:
#         if len(arguments) < 3:
#             sys.exit('Too few command-line arguments')
#         else:
#             sys.exit('Too many command-line arguments')
#     else:
#          return sys.argv[1]

def main():
    # file_name = get_filename(sys.argv)
    students = []
    with open("before.csv") as file:
         reader = csv.DictReader(file)
         for row in reader:
             last , first = row["name"].split(',')
             row["first"] = first
             row["last"] = last
             students.append(row)

    for student in students:
            print(f"{student['first']} |{student['last']} | {student['house']}")
    # with open("after.csv") as file:
    #        writer = csv.DictWriter(file, fieldnames=["first","last","house"])
    #        writer.writerow({"first": student['], "house": house})
if __name__ == '__main__':
    main()

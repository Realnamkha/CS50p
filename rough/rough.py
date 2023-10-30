students = []

with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

print(students)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")

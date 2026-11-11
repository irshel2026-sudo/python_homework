subjects = {
    'math': {'George': 85, 'Salome': 78, 'David': 92},
    'physics': {'George': 90, 'David': 75, 'Salome': 88},
    'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}

students = {}
for subject, grades in subjects.items():
    for student, grade in grades.items():
        students.setdefault(student, {})[subject] = grade

print(students)

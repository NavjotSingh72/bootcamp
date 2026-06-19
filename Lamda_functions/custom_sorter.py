students = [
    {"Name": "Farhan", "gpa": 5.5},
    {"Name": "Moin", "gpa": 8.8},
    {"Name": "Navjot", "gpa": 9.9},
    {"Name": "Vansh", "gpa": 7.5},
]

top_3 = sorted(students, key=lambda s: s["gpa"], reverse=True)[:3]

for student in top_3:
    print(student)


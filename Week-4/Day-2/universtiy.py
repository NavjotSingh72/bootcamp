class University:
    def __init__(self, student, teacher, course):
        self.student = student
        self.teacher = teacher
        self.course = course

    def display_info(self):
        print(f"Student : {self.student}")
        print(f"Teacher : {self.teacher}")
        print(f"Course  : {self.course}")

        courses = ["B.Tech", "BA", "BSc"]

        data = {}
        data["student"] = self.student
        data["teacher"] = self.teacher
        data["course"] = self.course

        print(data)
        print(courses)


u1 = University("Navjot", "Rahul Sir", "B.Tech")
u1.display_info()
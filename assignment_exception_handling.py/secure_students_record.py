class Student:
    total_students = 0   

    def __init__(self, roll_no, marks_list, grade):
        self.__roll_no = roll_no          
        self._grade = grade              
        self.marks = marks_list           

        Student.total_students += 1

    @property
    def marks(self):
        return self.__marks_list

    @marks.setter
    def marks(self, marks_list):
        for mark in marks_list:
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100")
        self.__marks_list = marks_list

    @property
    def gpa(self):
        avg_marks = sum(self.__marks_list) / len(self.__marks_list)
        return avg_marks / 10

    @classmethod
    def count(cls):
        return cls.total_students


s1 = Student(101, [80, 90, 85], "A")
s2 = Student(102, [70, 75, 80], "B")

print("GPA of Student 1:", s1.gpa)
print("GPA of Student 2:", s2.gpa)

print("Total Students:", Student.count())
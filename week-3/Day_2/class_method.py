class Employee:
    company = "KRM Corp"        
    _count = 0            
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        Employee._count += 1

    @classmethod
    def get_count(cls):         
        return f"{cls.company} has {cls._count} employees"

    @staticmethod
    def validate_dept(dept):    
        valid = ["CSE", "ECE", "MBA", "MCA"]
        return dept in valid

e1 = Employee("Alice", "CSE")
e2 = Employee("Bob", "ECE")

print(Employee.get_count())


print(Employee.validate_dept("CSE"))
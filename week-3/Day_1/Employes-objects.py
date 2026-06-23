class Employee:
    def __init__(self, name, department="General", bonus=0):
        self.name = name
        self.department = department
        self.bonus = bonus

    def annual_summary(self):
        total_pay = 30000 + self.bonus
        print("Name:", self.name)
        print("Department:", self.department)
        print("Total Pay:", total_pay)
        print("-" * 30)


employe1 = Employee("Navjot", "IT", 500000)


employe2 = Employee("Moin", "Cleaning_department")


employe3 = Employee("Farhan")

employe1.annual_summary()
employe2.annual_summary()
employe3.annual_summary()
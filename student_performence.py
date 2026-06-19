def student_report(name, marks):
    print("\n----- Student Report -----")
    print("Name :", name)
    print("Marks :", marks)

def add_bonus(marks):
    marks = marks + 5
    print("\nInside Function Marks :", marks)

def sum_marks(n):
    if n == 1:
        return 1
    return n + sum_marks(n - 1)

def square(x):
    return x * x

def cube(x):
    return x ** 3

def apply_operation(func, value):
    return func(value)

name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

student_report(name, marks)

add_bonus(marks)
print("Outside Function Marks :", marks)

n = int(input("\nEnter a number for recursive sum: "))
print("Recursive Sum =", sum_marks(n))

print("\nChoose Operation:")
print("1. Square")
print("2. Cube")

choice = int(input("Enter Choice: "))
num = int(input("Enter Number: "))

if choice == 1:
    operation = square
else:
    operation = cube

result = apply_operation(operation, num)

print("\nResult =", result)
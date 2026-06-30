def student_report(name, mark):
    print("\n----- Student Report -----")
    print("Name :", name)
    print("mark :", mark)
def add_bonus(mark):
    mark = mark + 5
    print("Inside Mark :", mark)
def sum_mark(n):
    if n == 1:
        return 1
    return n + sum_mark(n - 1)
def square(x):
    return x * x
def cube(x):
    return x ** 3
    

name = input("Enter Student Name: ")
mark = int(input("Enter mark: "))

student_report(name, mark)

add_bonus(mark)
print("Outside Function mark :", mark)

n = int(input("number for recursive sum: "))
print("Recursive Sum =", sum_mark(n))


print("Choose Operation:")
print("1. Square")
print("2. Cube")

choice = int(input("Choice: "))
num = int(input("Number: "))

if choice == 1:
    
    print(square(num))

else:
    print(cube(num))
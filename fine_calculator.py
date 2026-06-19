c=int(input("number of students: "))


for i in range(c):
    a=input("Enter your name: ")
    b=int(input("Enter number of days: "))
    
    fine=0

    if b<=5:
        fine+=5
    elif 6<=b<=10:
        fine+=10
    else:
        fine+=15

    print(f"Total fine for students is: {fine}")
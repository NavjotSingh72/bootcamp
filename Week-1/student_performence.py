marks = int(input("Enter marks: "))

if marks >= 40:
    status="pass"
    if marks >= 90:
        print("Distinction")
    elif marks >= 75:
        print("First Divisio")
    elif marks >= 60:
        print("Second Division")
    else:
        print("Third Division")
else:
    print("Fail")
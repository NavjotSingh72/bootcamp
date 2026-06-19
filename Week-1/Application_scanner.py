age = int(input("Enter age: "))
degree = input("Enter degree (B.Tech/MCA): ")
cgpa = float(input("Enter CGPA: "))


if age >= 21 and age <= 40:
    if degree == "B.Tech" or degree == "MCA":
        if cgpa >= 7.0:
            print("Interview Shortlisted")
        else:
            print("Rejected: CGPA is below 7.0")
    else:
        print("Rejected: Degree is not eligible")
else:
    print("Rejected: Age is not between 21 and 40")
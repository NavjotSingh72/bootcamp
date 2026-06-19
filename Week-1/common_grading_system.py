percentage = float(input("Enter Percentage: "))

if percentage >= 90 and percentage <= 100:
    grade = "A+"
    cgpa = "10"
elif percentage >= 80:
    grade = "A"
    cgpa = "9"

elif percentage >= 70:
    grade = "B+"
    cgpa = "8"

elif percentage >= 60:
    grade = "B"
    cgpa = "7"

elif percentage >= 50:
    grade = "C"
    cgpa = "6"

elif percentage>= 40:
    grade = "F"
    cgpa = "4"

print("Grade =", grade)
print("CGPA=",cgpa)
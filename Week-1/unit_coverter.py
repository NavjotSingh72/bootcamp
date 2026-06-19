print("Unit Converter")

category = input("Enter category (length/weight/temp): ")
value = float(input("Enter value: "))
from_unit = input("From unit: ")
to_unit = input("To unit: ")

if category == "length":
    if from_unit == "meter" and to_unit == "ft":
        result = value * 3.28084
    elif from_unit == "ft" and to_unit == "m":
        result = value * 0.3048
    else:
        result = None

elif category == "weight":
    if from_unit == "kg" and to_unit == "lb":
        result = value * 2.20462
    elif from_unit == "lb" and to_unit == "kg":
        result = value * 0.453592
    else:
        result = None

elif category == "temp":
    if from_unit == "C" and to_unit == "F":
        result = (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        result = (value - 32) * 5/9
    else:
        result = None

else:
    result = None

if result != None:
    print(value, from_unit, "=", round(result, 2), to_unit)
else:
    print("Conversion not available")
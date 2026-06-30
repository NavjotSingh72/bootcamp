def convert(c):
    return (c * 9/5) + 32
c=float(input("Enter the temperature in Celsius: "))
f=convert(c)
print(f"{c} celsius to fahrenheit is {f}")

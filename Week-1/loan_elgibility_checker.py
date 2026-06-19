salary = float(input("Enter your monthly income: "))
current_emi = float(input("Enter your existing EMI: "))

if salary >= 30000:
    if current_emi < (0.4 * salary):
        print("Eligible for loan")
    else:
        print("High debt burden")
else:
    print("Income too low")
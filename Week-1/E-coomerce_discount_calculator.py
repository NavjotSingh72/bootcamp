total = float(input("Enter cart total: "))
premium = input("Are you a Premium member? (yes/no): ")

if total > 5000:
    discount = 15

    if premium == "yes":
        discount = discount + 5
else:
    discount = 5

discount_amount = total * discount / 100
final_price = total - discount_amount

print("Original Price =", total)
print("Discount =", discount, "%")
print("Final Price =", final_price)
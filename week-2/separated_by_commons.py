numbers = input("Enter numbers separated by commas: ")

total = sum(int(num.strip()) for num in numbers.split(","))

print("The sum is:", total)
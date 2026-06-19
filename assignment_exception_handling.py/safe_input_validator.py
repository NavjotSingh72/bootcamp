class NegativeNumberError(Exception):
    pass

def get_positive_int():
    while True:
        try:
            num = int(input("Enter a positive integer: "))

            if num < 0:
                raise NegativeNumberError("Negative numbers are not allowed!")

            return num

        except ValueError:
            print("Invalid input! Please enter an integer.")

        except NegativeNumberError as e:
            print(e)


number = get_positive_int()
print("Valid number entered:", number)


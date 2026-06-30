def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    
    return cleaned_text == cleaned_text[::-1]


user_input = input("Enter text to check if it's a palindrome: ")


if is_palindrome(user_input):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")

def fibbonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_number)
        return fib_sequence
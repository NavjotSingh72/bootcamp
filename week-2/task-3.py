secret_number = 15

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Correct!")

elif guess < secret_number:
    difference = secret_number - guess
    print("Too low")
    print("You are", difference, "below the number")

else:
    difference = guess - secret_number
    print("Too high")
    print("You are", difference, "above the number")
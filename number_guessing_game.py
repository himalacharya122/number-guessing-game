import random

print("Welcome to the number guessing game!")

number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess (1-100): "))
    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")
    else:
        print("You got it! The number was", number)
        break

print("Thank you for playing!")
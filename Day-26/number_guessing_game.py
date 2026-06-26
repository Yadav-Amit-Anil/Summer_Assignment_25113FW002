#program to create number guessing game
print("==== Number Guessing Game ====")
import random
number = random.randint(1,10)
attempts = 0
while True:
    guess = int(input("Enter your guess number:"))
    attempts += 1
    if guess == number:
        print("congratulations! you guessed the correct number.")
        print("you guessed it in",attempts,"attempt(s)")
        break
    elif guess>number:
        print("Too high! try again.")
    else:
        print("Too low! try again.")
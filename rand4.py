import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("🎯 Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = input("Take a guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"🎉 You got it in {attempts} tries! The number was {number_to_guess}.")
            break

guess_the_number()


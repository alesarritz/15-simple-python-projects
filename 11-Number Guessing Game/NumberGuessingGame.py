import random
from art import logo


def NumberGuessingGame(secret_number, attempts):
    if attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess != secret_number:
            print("Too ", "high." if guess > secret_number else "low.")
            NumberGuessingGame(secret_number, attempts - 1)
        else:
            print(f"You got it! The answer was {secret_number}.")
    else:
        print("You've run out of guesses, you lose.")


print(logo, "\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
NumberGuessingGame(random.randint(1, 100), 10 if difficulty == 'easy' else 5)

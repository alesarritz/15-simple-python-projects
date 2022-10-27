import Hangman_art as art
import Hangman_words as words
import random

chosen_word = random.choice(words.word_list)
hangman = -1
guessing = []

for i in range(0, len(chosen_word)):
    guessing.append("_")

print(art.logo)

# Keep looping until the user looses all the lives or wins
while abs(hangman) < len(art.stages) and "_" in guessing:
    guess = input("Guess a letter: ").lower()
    win_point = False  # Flag used to check if the user has to lose a life

    # Special case the user guesses the entire word
    if guess == chosen_word:
        print("Excellent! You won!")
        print(guess)
        print(art.stages[hangman])
        break

    # Check if the letter was already guessed or not
    if guess in guessing:
        print("Letter already used!")
        win_point = True
    else:
        for i in range(0, len(chosen_word)):
            if guess == chosen_word[i]:  # If guess is right
                win_point = True
                guessing[i] = guess

    if win_point is False:  # If guess is wrong, the user loses a life
        hangman -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    # Print the word with dashes and the art
    print(f"{' '.join(guessing)}")
    print(art.stages[hangman])

# Out of the loop, check if the user won or not
if "_" not in guessing:
    print("Great job! You won!")
if abs(hangman) == len(art.stages):
    print("GAME OVER!\n")

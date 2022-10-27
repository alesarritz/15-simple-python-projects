import random
import art
from game_data import data


def HigherVsLower(score, a):
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")

    b = random.choice(data)
    while b == a:  # Avoid comparing one person with themselves
        b = random.choice(data)

    vs = {'A': a, 'B': b}
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if answer in vs and ((answer == 'A' and vs['A']['follower_count'] > vs['B']['follower_count']) or
                         (answer == 'B' and vs['B']['follower_count'] > vs['A']['follower_count'])):
        HigherVsLower(score + 1, b)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")


HigherVsLower(0, random.choice(data))

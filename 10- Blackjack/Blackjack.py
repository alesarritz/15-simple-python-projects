############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def sumCards(hand):
    sum_cards = 0
    for card in hand:
        sum_cards += card
    return  sum_cards


def getCards(is_dealer):
    hand = [random.choice(cards), random.choice(cards)]
    while sumCards(hand) < 17 and is_dealer:
        hand.append(random.choice(cards))

    if sumCards(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

    return hand


def currentSituation(your_hand, dealer_hand):
    your_score = sumCards(your_hand)
    print(f"Your cards: {your_hand}, current score: {your_score}")
    print(f"Computer's first card: {dealer_hand[0]}\n")
    if your_score >= 21:
        finalSituation(your_hand, dealer_hand)
    else:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            your_hand.append(random.choice(cards))
            currentSituation(your_hand, dealer_hand)
        else:
            finalSituation(your_hand, dealer_hand)


def finalSituation(your_hand, dealer_hand):
    your_score = sumCards(your_hand)
    dealer_score = sumCards(dealer_hand)
    print(f"Your final hand: {your_hand}, final score: {your_score}")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")
    if your_score > 21:
        print("You went over! You lose.\n")
    elif your_score == dealer_score:
        print("Draw!\n")
    elif your_score == 21:
        print("Magic 21! You win.")
    elif your_score > dealer_score or dealer_score > 21:
        print("Great! You win.\n")
    else:
        print("Bust! You lose.\n")
    blackjack()


def blackjack():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        print(logo)
        your_cards = getCards(is_dealer=False)
        dealer_cards = getCards(is_dealer=True)
        currentSituation(your_cards, dealer_cards)


if __name__ == "__main__":
    blackjack()

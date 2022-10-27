from art import logo


if __name__ == "__main__":
    print(logo)
    print("Welcome to the secret auction program.")

    finish = False
    auction_data = {}
    while finish is False:
        name = input("What's your name?: ")
        bid = int(input("What's your bid?: $"))

        auction_data[name] = bid

        isFinished = input("Are there any other bidders? type 'yes' or 'no': ").lower()
        if isFinished != 'yes':
            finish = True

    max_bid = 0
    winner = ""
    for k in auction_data.keys():
        if auction_data[k] > max_bid:
            max_bid = auction_data[k]
            winner = k
    print(f"The winner is {winner} with a bid of ${max_bid}.")

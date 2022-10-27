from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cryptoFunction(message, to_shift):
    crypto_word = ""
    for c in message:
        if c in alphabet:
            crypto_word += alphabet[(alphabet.index(c) + to_shift) % 26]
        else:
            crypto_word += c
    return crypto_word


if __name__ == "__main__":
    print(logo)

    finish = False
    while finish is False:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26

        if direction == 'encode':
            print(f"Here's the encoded result: {cryptoFunction(text, shift)}")
        elif direction == 'decode':
            shift *= -1
            print(f"Here's the decoded result: {cryptoFunction(text, shift)}")
        else:
            print("Wrong command. Try again.")
            continue

        isFinished = input("Type 'yes' if you want to go again. Otherwise 'no'.\n").lower()
        if isFinished != 'yes':
            finish = True

from art import logo

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

operations = {"+": add, "-": sub, "*": mul, "/": div}

if __name__ == "__main__":
    print(logo)

    finish = False
    skip = False
    result = 0
    first = 0
    while finish is False:
        if skip is False:
            first = float(input("What's the first number?: "))
        op = input("+\n-\n*\n/\nPick an operation: ")
        second = float(input("What's the next number?: "))

        if op in operations:
            result = operations[op](first, second)
        else:
            print("Invalid operator!")
            continue

        print(f"{first} {op} {second} = {result}")
        isFinished = input(f"Type:\n-'yes' to continue calculating with {result}\n-'no' to start a new "
                           f"calculation\n-'end' to exit\n").lower()

        if isFinished == 'end':
            finish = True
        elif isFinished == 'yes':
            skip = True
            first = result
        else:
            skip = False

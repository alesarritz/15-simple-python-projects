import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves = {'0': rock, '1': paper, '2': scissors}

print("Welcome to Rock, Paper, Scissor!")
yourMove = input("Choose your move - Rock:0, Paper:1, Scissor:2 -> ")
if yourMove in ['0','1','2']:
    print(moves[yourMove])
    print("Computer move:")
    computerMove = str(random.randint(0, 2))
    print(moves[computerMove])

    if yourMove == computerMove:
        print("Same idea folks!")
    elif yourMove == '0':
        if computerMove == '2':
            print("You won champ!")
        else:
            print("Next time loser!")
    elif yourMove == '1':
        if computerMove == '0':
            print("You won champ!")
        else:
            print("Next time loser!")
    else:
        if computerMove == '1':
            print("You won champ!")
        else:
            print("Next time loser!")
else:
    print("Invalid number loser!")

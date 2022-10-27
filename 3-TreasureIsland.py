print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
story = {
    '0': "You're at a crossroad. Where do you want to go?\nType 'left' or 'right'.\n",
    '1': {
        'right': "Fall into a hole.\nGAME OVER.",
        'left': "You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a "
                "boat.\nType 'swim' to swim across.\n",
    },
    '2': {
        'swim': "Attacked by trout.\nGAME OVER",
        'wait': "You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one "
                "blue.\nWhich colour do you choose?\n",
    },
    '3': {
        'red': "Burned by fire.\nGAME OVER",
        'blue': "Eaten by beasts.\nGAME OVER",
        'other': "You chose a door that doesn't exist.\nGAME OVER",
        'yellow': "You found the treasure! You Win!",
    },
}

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# Level 0
level0 = input(story['0'])
# Level 1
if level0 == 'left':
    level1 = input(story['1']['left'])
    if level1 == 'wait':
        level2 = input(story['2']['wait'])
        if level2 == 'yellow':
            print(story['3']['yellow'])
        elif level2 == 'red':
            print(story['3']['red'])
        elif level2 == 'blue':
            print(story['3']['blue'])
        else:
            print(story['3']['other'])
    else:
        level2 = input(story['2']['swim'])
        exit(0)
else:
    level1 = input(story['1']['right'])
    exit(0)




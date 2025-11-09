import random

player = input()
computer = random.randint(0,2)

if computer == 0:
    computer = "Keo"
if computer == 1:
    computer = "Bua"
if computer == 2:
    computer = "Bao"

if player == "Keo":
    if computer == "Keo":
        print("Draw")
    elif computer == "Bua":
        print("Computer win")
    else:
        print("Player win")

if player == "Bua":
    if computer == "Bua":
        print("Draw")
    elif computer == "Bao":
        print("Computer win")
    else:
        print("Player win")

if player == "Bao":
    if computer == "Bao":
        print("Draw")
    elif computer == "Keo":
        print("Computer win")
    else:
        print("Player win")
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCRISSORS = 3

playagain = True

while playagain:

    playerchoice = input("""
    Enter:
    1 for rock
    2 for paper
    3 for scrissors
    """)

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3.")

    computerchoise = random.choice("123")
    computer = int(computerchoise)

    print("You chose: " + str(RPS(player)).replace("RPS.", ""))
    print("Computer chose: " + str(RPS(computer)).replace("RPS.", ""))

    if player == computer:
        print("It's a tie!")
    elif player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    else: print("Python wins!")

    playagain = input('\nPlay again? \nY for Yes\nQ for Quit\n')
    if playagain.lower() == "y":
        continue
    else: 
        print("\nThank you for playing!")
        playagain = False
sys.exit("Bye!")
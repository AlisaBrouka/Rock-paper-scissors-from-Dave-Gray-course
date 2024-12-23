# @Author AlisaBrouka
# rock-paper-scissors game, playing in console, can accept arguments
import sys
import random
from enum import Enum

def rps(name = "PlayerOne"):

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():

        nonlocal name
        nonlocal game_count 
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCRISSORS = 3

        playerchoice = input(f"""{name}, enter:
        1 for rock
        2 for paper
        3 for scrissors
        """)

        if playerchoice not in "123":
            print(f"{name}, please enter 1, 2 or 3.")
            return play_rps()

        player = int(playerchoice)

        if player < 1 or player > 3:
            sys.exit("You must enter 1, 2 or 3.")

        computerchoise = random.choice("123")
        computer = int(computerchoise)

        print(
            f"{name}, you chose: {str(RPS(player)).replace("RPS.", "").title()}"
            )
        print(
            f"Computer chose: {str(RPS(computer)).replace("RPS.", "").title()}"
            )

        # function in function
        def decide_winner(player, computer):

            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == computer:
                return "It's a tie!"
            elif player == 1 and computer == 3:
                player_wins += 1
                return f"{name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}, you win!"
            else: 
                python_wins += 1
                return f"Python wins! \n Sorry, {name}"

        game_result = decide_winner(player, computer)
        print(game_result)
        
        game_count += 1

        print(f"\n Game count: {game_count}")
        print(f"\n {name}'s wins: {player_wins}")
        print(f"\n Python wins: {python_wins}")

        print(f"\nPlay again, {name}?")
        while True:
            playagain = input('\nY for Yes\nQ for Quit\n')
            if playagain .lower() not in ['y', 'q']:
                continue
            else: 
                break
        if playagain.lower() == "y":
            return play_rps()
        else: 
            print("\nThank you for playing!")
            sys.exit(f"Bye, {name}!")

    return play_rps

# needs argument name to start the file
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
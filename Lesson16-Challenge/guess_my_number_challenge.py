
import sys
import random
from enum import Enum


def gmnc(name='PlayerOne'):

    game_count = 0
    player_wins = 0
    # print(f"{num} divded by 4.52 is {num / 4.52:.2%}") - will need this to print percentage

    def play_gmnc():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}... guess my number... is it 1, 2 or 3... ಠ_ಠ\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, I said 1, 2 or 3... ಥ_ಥ")
            return play_gmnc()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name}, you chose {playerchoice}.")
        print(
            f"I chose {computerchoice}"
        )

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal percentage
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name}, you win (╯°□°）╯︵ ┻━┻"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}, you win (╯°□°）╯︵ ┻━┻"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}, you win (╯°□°）╯︵ ┻━┻"
            elif player == computer:
                return "It's a Draw"
            else:
                return f"Too bad {name} you lost - I win (❁´◡`❁)"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"\nGame Count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        if game_count > 0:
            percentage = player_wins/game_count
            print(f"\nPercentage: {percentage: 2%}")
        else:
            print(f"\nPercentage: N/A")

        print(f"\nPlay again {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gmnc()
        else:
            print("Thanks for Playing!")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else:
                return
    return play_gmnc


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="provides a personalised game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guess_my_number_challenge = gmnc(args.name)
    guess_my_number_challenge()

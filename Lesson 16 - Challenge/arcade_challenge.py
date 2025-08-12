import sys
from guess_my_number_challenge import gmnc
from rps8_challenge import rps


def arcade_challenge(name='PlayerOne'):

    playerchoice = input(
        f"\n{name} Welcome to the Arcade!\n\n"
        f"Choose your game:\n"
        f"1 for rock, paper sicissors\n"
        f"2 for guess my number\n"
        f"and 'x' to quit\n")

    if playerchoice.lower() not in ["1", "2", "x"]:
        print(f"\n{name}, Please select 1, 2 or x")
        return arcade_challenge(name)

    if playerchoice == "1":
        rps(name)()
        arcade_challenge(name)

    elif playerchoice == "2":
        gmnc(name)()
        arcade_challenge(name)
    elif playerchoice.lower() == "x":
        sys.exit(f"Bye {name}!")


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

    arcade_challenge = arcade_challenge(args.name)
    arcade_challenge()

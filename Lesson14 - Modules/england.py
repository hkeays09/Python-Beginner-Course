from random import choice

Capital = "London"

bird = "Pigeon"

flower = "Poppy"

song = "Sweet Caroline"


def randomfunfact():
    funfacts = [
        "London has the big ben.",
        "Manchester is the home of the band called Oasis",
        "England is part of the United Kingdom which is made up for four countries",
        "Harry Potter takes place in England"
    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()



name = "Dave"
count = 1


def another():
    colour = "blue"
    # count += 1 cannot modify global varbiles from a function definition in this way.
    global count  # line 10 and 11 is how you do it.
    count += 1
    print(count)

    def greeting(name):
        nonlocal colour  # How to modify variables in another function. Not using global makes it so that you create a new variable/or it wont be able to work at all
        colour = "red"
        print(colour)
        print(name)

    greeting("Dave")


another()

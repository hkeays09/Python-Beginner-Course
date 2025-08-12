def hello_world():
    print("Hello World!")  # defining the function


hello_world()  # calling the function


# def sum(num1, num2):
#     print(num1 + num2)  # paramets are num1 and num2


# # sum(2, 3)  # arguments are 2 and 3
# sum(1, 7)  # arguments are 1 and 7
# sum(100, 3)  # arguments are 100 and 3

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum()
print(total)


# makes it a tuple and as many data points as you want - multiple unknown items
def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


# How to put dictionaries (Keys = variables) into the parameter definition (arugments) = (KeywordArguments = Kwargs) ** is how you call them.
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")

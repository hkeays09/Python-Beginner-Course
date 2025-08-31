from functools import reduce
def squared(num): return num * num
# sqaured = lambda num : num * num


print(squared(2))


def addTwo(num): return num + 2
# addTwo = lambda num : num + 2


print(addTwo(12))


def sum_total(a, b): return a + b
# sum = lambda a,b : a + b


print(sum_total(10, 8))


###############################
# most often used inside another function when you don't want to save them for later

def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

################################

# Takes one or more funtions as its argument or returns a function as th result.


numbers = [3, 7, 12, 18, 20, 21]

sqaured_nums = map(lambda num: num * num, numbers)

print(list(sqaured_nums))

#########################


# could use a if/for loop but this is much clearner
odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))


numbers = [1, 2, 3, 4, 5, 1]

# a built in function can make this easy
total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)

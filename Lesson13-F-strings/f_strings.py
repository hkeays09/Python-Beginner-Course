person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)  # %s method
print(message)

message = "\n{} has {} coins left.".format(person, coins)  # format 1 method
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)  # format 2 method
print(message)

message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person
)  # format method 3
print(message)

player = {'person': 'Dave', 'coins': 3}


message = "\n{person} has {coins} coins left.".format(
    **player)  # format method 4
print(message)

# All above methods are old.

# f strings! This is the way

message = f"\n{person} has {coins} coins left."  # f string method
print(message)

message = f"\n{person} has {2*5} coins left."  # f string method using integers
print(message)

# f string method using .lower method
message = f"\n{person.lower()} has {2*5} coins left."
print(message)

# f string method using dictionary
message = f"\n{player['person']} has {2*5} coins left."
print(message)

# You can pass formatting options

num = 10
# the .2f is what formattes the answer 2 2 decimal places.
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divded by 4.52 is {num / 4.52:.2%}")

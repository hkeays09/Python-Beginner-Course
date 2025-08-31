import os

# r = Read
# a = append
# w = write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")
# print(f.read())
# print(f.read(5))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()  # important to close to see changes and more.

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file that doesn't exist
f = open("names.txt", "a")
f.write("\nNeil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, also creates the file if it does not exist

f = open("name_list.txt", "w")
f.close()

# Creates a file, but returns an error if it already exists

if not os.path.exists("harry.txt"):
    f = open("harry.txt", "x")
    f.close()

# Delete a file

# avoid an error if it doesn't exist

if os.path.exists("harry.txt"):
    os.remove("harry.txt")
else:
    print("The file you want to delete doesn't exist")


with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)

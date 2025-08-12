# Dictionaries - store values in key-value pairs
band = {
    "vocals": "plant",
    "guitar": "page",
}

band2 = dict(vocals="plant", guitar="page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tup;es
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "coverdale"
band.update({"bass": "JPJ"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "bonham"
print(band)
print(band.popitem())  # removes the last item added (key value pair as tuple)
print(band)

# Delete and clear

band["drums"] = "bonham"
del band["drums"]  # delete a specific key
print(band)

band2.clear()
print(band2)

del band2  # delete the entire dictionary

# copy dictionaries

# band2 = band  # This creates a reference, not a copy
# print("badcopy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

# correct way to copy
band2 = band.copy()
band2["drums"] = "Dave"
print("goodcopy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("goodcopy2!")
print(band3)

# nested dictionaries

member1 = {
    "name": "plant",
    "instrument": "vocals",
}
member2 = {
    "name": "page",
    "instrument": "guitar",
}
band = {
    "member1": member1,
    "member2": member2,
}
print(band)
print(band["member1"]["name"])  # nesting down

# sets - final data collection type

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))  # using the set constructor function

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicates allowed with sets
nums = {1, 2, 2, 3, 4, 4, 5}  # duplicates are ignored
print(nums)

# true is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# adding and removing elements to a set

nums.add(8)
print(nums)

# Add eelements from another set to another
morenums = {5, 6, 7, 8}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictionaries

# Merge two sets to create a new set
one = {1, 2, 3}
two = {3, 4, 5}
mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# remove only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)

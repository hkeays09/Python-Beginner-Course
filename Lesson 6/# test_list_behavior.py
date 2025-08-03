# test_list_behavior.py

print("Creating list a...")
a = [1, 2]
print("Assigning b = a...")
b = a

print("\nUsing a += [3] (in-place)...")
a += [3]

print("a:", a)
print("b:", b)

print("\nResetting a and b...")
a = [1, 2]
b = a

print("\nUsing a = a + [3] (creates new list)...")
a = a + [3]

print("a:", a)
print("b:", b)

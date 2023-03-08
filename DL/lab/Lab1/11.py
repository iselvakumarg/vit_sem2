# Write a python program to remove duplicates from tuple.

def remove_duplicates(t):
    return tuple(set(t))

print(remove_duplicates((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

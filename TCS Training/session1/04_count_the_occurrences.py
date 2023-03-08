"""
Write the program to count the nunmber of occurrences of a given element in an array of integers
arr = [4, 2, 1, 3, 4, 5, 4, 7, 8, 4]
element = 4
"""

arr = [4, 2, 1, 3, 4, 5, 4, 7, 8, 4]
n = len(arr)
target = 4
count = 0
for i in range(n):
    if arr[i] == target:
        count = count + 1

print(f"The Occurences of the target element {target} is {count}")
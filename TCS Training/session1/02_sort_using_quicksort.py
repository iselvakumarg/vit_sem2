"""
You are given an array of integers, your task is to implement a program to sort the array in ascending order using the quicksort algorithm

Sample Input: [64, 25, 12, 22, 11]
"""

# Partititon Function to divide the data based on the pivot

def partition(arr: list[int], low: int, high: int) -> int: 
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] # swap the high with low
    arr[i+1], arr[high] = arr[high], arr[i+1] # swap pivot with the high element
    return i+1 # return the pointer where the process stops


def quick_sort(arr: list[int], low: int, high: int) -> None:
    if low < high:
        pp = partition(arr, low, high)

        quick_sort(arr, low, pp-1) # left of pivot
        quick_sort(arr, pp+1, high) # right of pivot

array = [64, 25, 12, 22, 11]
print(f'Unsorted data is {array}')

n = len(array)

quick_sort(array, 0, n-1)

print(f'Sorted array is {array}')

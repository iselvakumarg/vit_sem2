"""
Find the Second largest Element in the Array
"""

arr = [3, 7, 1, 9, 4, 5]
arr1 = [3, 2]
arr2 = [2]

k = 2

def second_largest(arr: list[int], k: int) -> int:
    n = len(arr)
    if n >= k:
        arr.sort(reverse=True)
        print(f"The Sorted Array is : {arr}")
        return arr[k-1]
    else:
        print("The array data is not sufficient")

print(f"The Second largest Element is : {second_largest(arr, k)}")
arr = [5, 3, 9, 1, 7]

high = arr[0]
low = arr[0]

for i in range(len(arr)):
    if arr[i] > high:
        high = arr[i]

    if arr[i] < low:
        low = arr[i]

print(f"The largest value in the array is : {high}, The Smallest value in the array is : {low}")
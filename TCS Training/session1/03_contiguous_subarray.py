arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def kadane(arr : list[int]) -> int:
    n = len(arr)
    currentSum = 0
    maxSum = arr[0]

    for i in range(n):
        if currentSum < 0:
            currentSum = 0
        currentSum = currentSum + arr[i]
        if currentSum > maxSum:
            maxSum = currentSum
        
    return maxSum

print(f"Max Subarray sum is : {kadane(arr)}")
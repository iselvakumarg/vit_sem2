"""
Given a nunmber N, the task is to check whether it is unique number or not
"""

n = input("Enter the Number: ")
arr = []
nu = False

for i in n:
    if i in arr:
        nu = True
        break
    else:
        arr.append(i)
    
if nu:
    print(f"{n} is not a unique number")
else:
    print(f"{n} is a unique number")        
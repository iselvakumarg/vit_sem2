"""
Find the 15th term of the series?
0,0,7,6,14,12,21,18, 28
"""

n = int(input())
a, b = 0, 0

for i in range(1, n+1):
    if i % 2 !=0:
        a += 7
    else:
        b += 6
    
if n%2 !=0:
    print(f"The {n}th element of the series is {a-7}")
else:
    print(f"The {n}th element of the series is {b-6}")
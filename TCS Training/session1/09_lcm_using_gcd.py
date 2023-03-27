"""
Write a program using GCD to find the LCM of two numbers
Input: 72 
120
Sample Ouput: 360
"""
a = 72
b = 120

def gcd(a, b):
    result = min(a, b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result

lcm = (a * b) / gcd(a, b)

print(lcm)
print(gcd(a, b))
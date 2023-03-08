"""
Perform palindrome without using in-build how to reverse string

Input: MALAYALAM
"""

string = "MALAYALAM"
n = len(string)
for i in range(n):
    if string[i] == string[n-i-1]:
        valid = True
    else: valid = False

if valid:
    print("String is palindrome")
else:
    print("String is not plaindrome")
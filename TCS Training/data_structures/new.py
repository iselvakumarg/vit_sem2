"""
Sum of digits in the given number until it get a single digit. No looping, recursion and function
"""

# x = 3242

# a = str(x)
# print(type(a))

# a = a.split()
# print(a)

# y = int(a[0][0]) + int(a[0][1]) + int(a[0][2]) + int(a[0][3])
# print(y)

# y = str(y)
# z = y.split()
# print(z)

# b = int(z[0][0]) + int(z[0][1])
# print(b)

x = 965322

# if x % 9 == 0:
#     print(9)
# else:
#     print(x % 9)

x1 = x // 1000
#print(x1)

x2 = (x // 100) % 10
#print(x2)

x3 = (x // 10) % 10
#print(x3)

x4 = (x % 10)
#print(x4)

y = x1 + x2 + x3 + x4
#print(y)

z = ((y // 10) % 10) + (y % 10)
# print(f"Sum of {x} is : {z}")

sum = 9 if x % 9 == 0 else (x % 9)
print(sum)
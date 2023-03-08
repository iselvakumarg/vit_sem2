n = int(input("Enter the nth term: "))

def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))
    
if n <= 0:
    print("The Fibonacci output is 0")
else:
    print(fibo(n))
    
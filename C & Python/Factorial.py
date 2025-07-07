

def factorial(n):
    if n < 0:
        return "No factorial for negative numbers."
    if n <= 1:
        return 1
    return n * factorial(n - 1)
    
print(factorial(5))
print(factorial(-3))


def factorial(n):
    if n < 0:
        return "No factorial for negative numbers."
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def safe_factorial(n):
    if n > 1000:
        raise RecursionError("Number too large — risk of stack overflow.")
    return factorial(n)

print("Factorial of 5:", safe_factorial(5))
print("Factorial of 0:", safe_factorial(0))
print("Factorial of -3:", safe_factorial(-3))
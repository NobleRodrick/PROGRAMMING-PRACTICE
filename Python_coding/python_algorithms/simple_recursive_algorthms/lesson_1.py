# Program to calculate the factorial of a number iteratively

def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

print(iterative_factorial(5))
    
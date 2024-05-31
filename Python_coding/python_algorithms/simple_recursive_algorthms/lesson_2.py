def recursive_factorial(n):
    if n == 1:
        return n
    else:
        temp = recursive_factorial(n -1)
        temp = temp * n
    return temp

print(recursive_factorial(5))

def recur_factorial(n):
    if n == 1: return n
    else: return n * recur_factorial(n - 1)
    
print(recur_factorial(5))
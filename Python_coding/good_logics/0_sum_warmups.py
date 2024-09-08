def sum1(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    final_sum = 0
    for x in range(n+1):
        final_sum += x
        
    return final_sum


def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    return (n*(n+1))/2


first = sum1(5)
second =sum2(5)

print(first, second)
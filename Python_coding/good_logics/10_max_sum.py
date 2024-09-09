"""
Take an array with positive and negative integers and
find the maximum sum of that array
"""
def largest(arr):
    if len(arr) == 0:
        return print('Too small array')
    
    max_sum = current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(current_sum, max_sum)
        
    return max_sum

print(largest([-2, -3, 4, -1, -2, 1, 5, -3]))

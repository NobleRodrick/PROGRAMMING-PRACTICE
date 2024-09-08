"""
Array pair sum
Given an integer array, output all  the unique pairs that sum up to a specific value k
so  the input:
pair_sum([1,3,2,2],4)
would return 2 pairs: 1,3 and 2,2
"""

def pair_sum(array, k):
    if len(array) < 2:
        return print("Too small")
    
    seen = set()
    output = set()
    
    for num in array:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    return len(output)
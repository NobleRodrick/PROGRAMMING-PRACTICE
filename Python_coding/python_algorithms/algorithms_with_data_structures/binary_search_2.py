def binary_search_recursive(arr, target, low, high):
    """_summary_ Perform a binary search on a sorted array recursively

    Args:
        arr (array): List of elements to search through(must be sorted)
        target (str/char/int): The element to search for
        low (int): the lower index of the array slice
        high (int): the upper index of the array slice
        return: the index of the target element if found, otherwise -1.
    """
    # Base case: If the pointers have crossed, the target is not in the array
    if low > high:
        return -1
    # Calculate the mid index
    mid = (low + high)//2
    
    # if the target is found, return the mid index
    if arr[mid] == target:
        return mid
    
    # If the target is less han the mid element, search for the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    
    # If the target is greater than the mid element, search in the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, high)
    

def binary_search(arr, target):
    """Wrapper function for the recursive search

    Args:
        arr (array): List of elements to search through(must be sorted)
        target (any): The element to search for
        return: the index of the target element if found, otherwise -1
    """
    return binary_search_recursive(arr, target, 0, len(arr) - 1)


# usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 0, 10]
target = 7

result_recursive = binary_search(arr, target)
print("Recursive result: ", result_recursive)
    
    
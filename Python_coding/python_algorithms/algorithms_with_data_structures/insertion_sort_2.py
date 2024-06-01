def insertion_sort_recursive(arr, n=None):
    """Perform insertion sort on a list recursively

    Args:
        arr : The list of elements to be sorted
        n: Current length of the list to be sorted. Defaults to None.
        return: Sorted list
    """
    # Initialize n on the first call
    if n is None:
        n = len(arr)
    
    # Base case: if the list has one or no element, it is already sorted
    if n <= 1:
        return arr
    
    # Sort the first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    # Insert the nth element into the correct position
    key = arr[n - 1]
    j = n - 2
    
    # Shift elements of arr[0..n-2] that are greater than key to one position ahead of their current position
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        
    # Place the key element at the correct position
    arr[j + 1] = key
    
    return arr

# Example
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort_recursive(arr.copy())
print("Sorted array:", sorted_arr)
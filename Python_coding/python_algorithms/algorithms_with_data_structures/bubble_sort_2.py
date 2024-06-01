def bubble_sort_recursive(arr, n=None):
    """Perform bubble sort on a list recursively

    Args:
        arr : The list of elements to be sorted
        n : length of the portion of the list to be sorted
        return: Sorted list
    """
    # Initialize n on the first call
    if n is None:
        n = len(arr)
    
    # Base case: if the array length is 1, it is already sorted
    if n == 1:
        return arr
    
    # Traverse the array and perform a pass of bubble sort
    for i in range(n - 1):
        # Swap if the element found is greater than the next element
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            
    # Recursively call bubble_sort_recursive to sort the rest of the array
    bubble_sort_recursive(arr, n - 1)
    
    return arr


# usage
arr = [64, 34, 25, 12, 22, 11, 90]

sorted_recursive = bubble_sort_recursive(arr.copy())
print("Recursive sorted array:", sorted_recursive)
def bubble_sort_iterative(arr):
    """Perform bubble sort on a list iteratively

    Args:
        arr: list of elements to be sorted
        return: sorted list
    """
    n = len(arr) # get the length of the array
    
    # Traverse through all elements in the array
    for i in range(n):
        # Track if any swaps where made in this pass
        swapped = False
        
        # Last i elements are already in place, so we dont't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps were made, the array is already sorted
        if not swapped:
            break
        
    return arr


# Implementation
arr = [64, 34, 25, 12, 22, 11, 90]

sorted_iterative = bubble_sort_iterative(arr.copy())
print("Iterative sorted array:", sorted_iterative)

    
    
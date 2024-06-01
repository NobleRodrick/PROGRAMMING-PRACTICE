def binary_search_iterative(arr, target):
    """Perform a binary search on a sorted array iteratively.
    
    : param arr: List of elements to search through(must be sorted).
    : param target: The element to search for.
    : return: The index of the target element if found, otherwise -1.
    """
    #initialize the low and high pointers
    low = 0
    high = len(arr) - 1
    
    #loop until the pointers meet
    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2
        
        #if the target is found, return the mid index
        if arr[mid] == target:
            return mid
        #if the target is less than the mid, narrow the search to the left half of the array
        elif arr[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result_iterative = binary_search_iterative(arr, target)
print("Iterative result: ", result_iterative)
     

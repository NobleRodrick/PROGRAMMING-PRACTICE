def insertion_sort_2d(arr):
    """Perform insertion sort on each row of a 2- dimensional list. 

    Args:
        arr : 2-dimensional list of elements to be sorted.
        return: 2-dimensional list with each row sorted
    """
    # Function to perform insertion sort on a single row
    def insertion_sort_row(row):
        n = len(row)
        for i in range(1, n):
            key = row[i]
            j = i - 1
            while j >= 0 and row[j] > key:
                row[j + 1] = row[j]
                j -= 1
            row[j + 1] = key
    
    # Apply insertion sort to each row
    for row in arr:
        insertion_sort_row(row)
        
    return arr

# usage
arr_2d = [
    [12, 11, 13, 5, 6],
    [3, 7, 2, 8, 4],
    [9, 14, 10, 1, 15]
]

sorted_arr_2d = insertion_sort_2d(arr_2d)
print("Sorted 2D array:")
for row in sorted_arr_2d:
    print(row)
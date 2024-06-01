# Insertion sort is a simple and efficient comparison-based sorting algorithm. It works similarly to the way you might sort playing cards in your hands
# The array is visually split into a sorted and unsorted part
# Values from the unsorted part are picked and placed at the correct position in the sorted part

# How the insertion works
#1 start with the first element, consider it as sorted
#2 Pick the next element
#3 Compare the Picked element with the elements in the sorted part
#4 Shift all elements in the sorted part that are greater than the picked elements to the right
#5 Insert the picked element into its correct position
#6 Repeat steps 2 and 5 until the whole array is sorted

def  insertion_sort(arr):
    """Perform insertion sort on a list

    Args:
        arr : list of elements to be sorted
        return: sorted list
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i] # The current element to be inserted in the sorted part
        
        # Move elements of arr[0..i-1], that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # shift element to the right
            j -= 1
        arr[j + 1] = key # Place the key element at the correct position
        
    return arr

#example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr.copy())
print("Sorted array:", sorted_arr)
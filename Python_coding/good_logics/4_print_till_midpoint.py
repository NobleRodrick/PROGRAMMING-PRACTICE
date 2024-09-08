def comp(lst):
    """
    This function prints the first item 0(1) it is a constant
    Then is prints the first half of the list 0*(n/2)
    then prints a string 20 times 0(10) it is a constant
    """
    print(lst[0])
    
    midpoint = len(lst) // 2
    
    for val in lst[:midpoint]:
        print(val)
        
    for x in range(10):
        print("number")
        
        
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
comp(lst)
        
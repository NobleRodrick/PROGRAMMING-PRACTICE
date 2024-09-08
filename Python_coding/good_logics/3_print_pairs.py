def func_quad(lst):
    """
    print pairs for every item in the list    """
    for item_1 in lst:
        for item_2 in lst:
            print(item_1, item_2)
            
lst = [1, 2, 3, 4, 5]
func_quad(lst)
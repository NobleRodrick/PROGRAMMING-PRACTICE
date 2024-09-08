def matcher(lst, match):
    """
    Given a list, return a boolean indicating if each item is in the list
    """
    for item in lst:
        if item == match:
            return True
    return False
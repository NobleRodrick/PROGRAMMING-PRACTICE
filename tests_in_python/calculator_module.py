def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Fuction"""
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError("Can't divide by zero")
    return x / y
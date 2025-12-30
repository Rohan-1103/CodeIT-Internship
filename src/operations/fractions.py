from fractions import Fraction

def add_fractions(a, b):
    """Adds two fractions."""
    return a + b

def subtract_fractions(a, b):
    """Subtracts two fractions."""
    return a - b

def multiply_fractions(a, b):
    """Multiplies two fractions."""
    return a * b

def divide_fractions(a, b):
    """Divides two fractions."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

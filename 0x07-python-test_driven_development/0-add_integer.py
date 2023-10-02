#!/usr/bin/python3
# 0-add_integer.py
"""A function that adds 2 integers"""


def add_integer(a, b=98):
    """Returns addition of two integers, a and b
    If floats, a and b are casted to int before addition

    Exception:
        TypeError: If a or b is not integer and not float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

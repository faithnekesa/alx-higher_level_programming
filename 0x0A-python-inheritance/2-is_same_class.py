#!/usr/bin/python3
"""Defines class that checks the objects"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): Object being checked
        Class (type): Class to match the type of obj to
    Returns:
        True if the object is exactly an instance of the specified class
        Otherwise False
    """
    if type(obj) == a_class:
        return True
    return False

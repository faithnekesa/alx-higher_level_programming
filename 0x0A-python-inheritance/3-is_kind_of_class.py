#!/usr/bin/python3
"""Defines class that checks the objects"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is an instance of
        or if the object is an instance of a class that inherited from
        the specified class ; otherwise False

    Args:
        obj (any): Object being checked
        Class (type): Class to match the type of obj to
    Returns:
        True if the object is exactly an instance of the specified class
        Otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False

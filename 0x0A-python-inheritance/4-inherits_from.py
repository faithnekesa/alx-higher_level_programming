#!/usr/bin/python3
"""Defines a class that checks object inheritance"""


def inherits_from(obj, a_class):
    """Checks if an object obj is an inherited instance of a class

    Args:
        obj (any): Object being checked
        a_class (type): Class being matched to the type of obj
    Returns:
        True if the object is an instance of a class that inherited
        Otherwise, False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

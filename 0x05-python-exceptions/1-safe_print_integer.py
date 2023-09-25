#!/usr/bin/python3

def safe_print_integer(value):
    """A function that prints an integer with "{:d}".format()
    Args:
        value Can be any type (integer, string, etc.)

    Returns:
        Returns True if value has been correctly printed (it means the value
        is an integer)
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

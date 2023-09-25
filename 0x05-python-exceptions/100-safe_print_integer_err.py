#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """A function that prints an integer using "{:d}".format()

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        Returns True if value has been correctly printed
        (it means the value is an integer)
        Otherwise: Returns False and prints in stderr the error
        precede by Exception
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

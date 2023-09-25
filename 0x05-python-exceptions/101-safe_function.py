#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """A function that executes a function safely
    Args:
        fct: Pointer to the function being executed
        args: Arguments for fct.

    Returns:
        Result of the function
        Otherwise, returns None if something happens during the function
        and prints in stderr the error precede by Exception:
    """
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result

#!/usr/bin/python3
"""Function that prints a square with the character # """


def print_square(size):
    """A function that prints a square with the character #
    Args:
        size (int): Height/width of the square
    exception:
        TypeError: If size is a float and is less than 0
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

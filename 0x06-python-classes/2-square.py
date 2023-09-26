#!/usr/bin/python3
"""define the class Square"""


class Square:
    """Representing the square."""

    def __init__(self, size=0):
        """a class Square that defines a square by: (based on 1-square.py)

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

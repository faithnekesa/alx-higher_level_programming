#!/usr/bin/python3
"""define the class Square"""


class Square:
    """Representing the square"""

    def __init__(self, size=0):
        """Defining the class Square based on 2-square.py

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns:
            The current area of the square.
        """
        return (self.__size * self.__size)

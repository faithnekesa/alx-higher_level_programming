#!/usr/bin/python3
"""define the class Square"""


class Square:
    """Defining the square based on 3-square.py"""

    def __init__(self, size=0):
        """Initializing a new square

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter and setter method for size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns:
            The current square area"""
        return (self.__size * self.__size)

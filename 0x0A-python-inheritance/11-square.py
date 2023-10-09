#!/usr/bin/python3
"""Defines a subclass of the rectangle; Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square instance

        Args:
            size (int): Size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

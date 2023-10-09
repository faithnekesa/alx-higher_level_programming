#!/usr/bin/python3
"""Defines Rectangle class which inherits from 7-base_geometry.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using 7-base_geometry.py"""

    def __init__(self, width, height):
        """Intialize a rectangle instance

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

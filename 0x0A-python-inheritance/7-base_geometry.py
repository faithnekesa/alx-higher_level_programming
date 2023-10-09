#!/usr/bin/python3
"""Defines a base class BaseGeometry"""


class BaseGeometry:
    """Represents base geometry class"""

    def area(self):
        """Empty function for area"""
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        """Function that validates a parameter as an int

        Args:
            Name (str): Name of the parameter
            Value (int): Parameter being validated
        Exception:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

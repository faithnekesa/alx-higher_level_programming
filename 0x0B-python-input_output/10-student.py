#!/usr/bin/python3
"""Definition of Student Class"""


class Student:
    """Represent the class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of the student

        If attrs is a list of strings, only attr names in this
        list to be retrieved. Otherwise retrieve all attributes

        Args:
            attribute (list): (Optional) Attributes being represented
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

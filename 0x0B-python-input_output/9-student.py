#!/usr/bin/python3
"""Definistion of Student Class"""


class Student:
    """Represent the class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student

        Args:
            first_name (str): First name of the student
            last_name (str):Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representation of the student"""
        return self.__dict__

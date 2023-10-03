#!/usr/bin/python3
"""Unit tests for function max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unit tests for max_integer([..])"""

    def test_ordered_list(self):
        """Validate an ordered list of ints"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Validate un-ordered list of ints"""
        unordered = [1, 3, 4, 3]
        self.assertEqual(max_integer(unordered), 4)
        
    def test_empty_list(self):
        """Validate when a list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_maxAt_begginning(self):
        """Validate a list with max value at the beginning"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)    
    
    def test_one_element_list(self):
        """Validate list with a one element"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Validate with a list of floats"""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_intsAnd_floats(self):
        """Validate a list with ints and floats"""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)
        
    def test_listOf_strings(self):
        """Validate a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_string(self):
        """validate a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_empty_string(self):
        """Validate an empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()

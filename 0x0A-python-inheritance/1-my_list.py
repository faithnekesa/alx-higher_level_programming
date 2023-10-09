#!/usr/bin/python3
"""Define class MyList that inherits from List"""


class MyList(list):
    """Implements a print list function in ascending sort"""

    def print_sorted(self):
        """Function that prins a list in sorted ascending order."""
        print(sorted(self))

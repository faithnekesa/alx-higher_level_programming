#!/usr/bin/python3
"""Defines a function that writes a file"""


def write_file(filename="", text=""):
    """Function that writes a string to a UTF8 text file

    Args:
        filename (str): Name of the file to write to
        text (str): Text to write to the file
    Returns:
        The number of characters added to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

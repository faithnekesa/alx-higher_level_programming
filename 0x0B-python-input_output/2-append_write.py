#!/usr/bin/python3
"""Function that defines a file-appending function"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file

    Args:
        filename (str): Name of the file to write to
        text (str): Text to write to the file
    Returns:
        The number of characters added to the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

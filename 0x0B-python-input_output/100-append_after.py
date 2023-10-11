#!/usr/bin/python3
"""A function that inserts text after each line in a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text line to a file after each line containing a
    specific string

    Args:
        filename (str): Name of the file
        search_string (str): String being searched within the file
        new_string (str): String to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

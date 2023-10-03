#!/usr/bin/python3
# 5-text_indentation.py
"""A function that prints a text with 2 new lines """


def text_indentation(text):
    """A function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (string):Text being printed
    Raises:
        TypeError: If text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

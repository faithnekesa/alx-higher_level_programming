#!/usr/bin/python3
"""Function that deletes keys with a specific value
in a dictionary."""


def complex_delete(a_dictionary, value):
    listKeys = list(a_dictionary.keys())

    for dictValue in listKeys:
        if value == a_dictionary.get(dictValue):
            del a_dictionary[dictValue]

    return (a_dictionary)

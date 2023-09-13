#!/usr/bin/python3
"""function that returns the number of keys in a dictionary"""


def number_keys(a_dictionary):
    number = 0
    listKeys = list(a_dictionary.keys())

    for i in listKeys:
        number += 1

    return (number)

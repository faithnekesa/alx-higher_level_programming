#!/usr/bin/python3
"""Function that returns a new dictionary with all
values multiplied by 2"""


def multiply_by_2(a_dictionary):
    newDictionary = a_dictionary.copy()
    listKeys = list(newDictionary.keys())

    for i in listKeys:
        newDictionary[i] *= 2

    return (newDictionary)

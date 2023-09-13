#!/usr/bin/python3
"""Function that prints a dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    listOrder = list(a_dictionary.keys())
    listOrder.sort()
    for i in listOrder:
        print("{}: {}".format(i, a_dictionary.get(i)))

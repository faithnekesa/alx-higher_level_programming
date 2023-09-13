#!/usr/bin/python3
"""Function that adds all unique integers in a list
(only once for each integer)"""


def uniq_add(my_list=[]):
    uniqueList = set(my_list)
    number = 0

    for i in uniqueList:
        number += i

    return (number)

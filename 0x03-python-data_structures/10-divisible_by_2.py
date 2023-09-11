#!/usr/bin/python3
"""Function that finds all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):
    multis = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multis.append(True)
        else:
            multis.append(False)

    return (multis)

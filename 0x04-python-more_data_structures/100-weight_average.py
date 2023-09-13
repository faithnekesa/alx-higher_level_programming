#!/usr/bin/python3
""" function that returns the weighted average
of all integers tuple (<score>, <weight>)"""


def weight_average(my_list=[]):
    if not my_list:
        return 0

    thisNum = 0
    thisDen = 0

    for myTup in my_list:
        thisNum += myTup[0] * myTup[1]
        thisDen += myTup[1]

    return (thisNum / thisDen)

#!/usr/bin/python3
"""Create a function def roman_to_int(roman_string): that
converts a Roman numeral to an integer."""


def toSubtract(listNum):
    toSub = 0
    maxList = max(listNum)

    for n in listNum:
        if maxList > n:
            toSub += n

    return (maxList - toSub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    romNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(romNum.keys())

    number = 0
    lastRomNum = 0
    listNum = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if romNum.get(ch) <= lastRomNum:
                    number += toSubtract(listNum)
                    listNum = [romNum.get(ch)]
                else:
                    listNum.append(romNum.get(ch))

                lastRomNum = romNum.get(ch)

    number += toSubtract(listNum)

    return (number)

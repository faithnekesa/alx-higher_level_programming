#!/usr/bin/python3

def safe_print_division(a, b):
    """a function that divides 2 integers and prints the result
    Args:
        a (int)
        b (int)
    Return: value of the division, otherwise: None
    """
    try:
        divisionVal = a / b
    except (TypeError, ZeroDivisionError):
        divisionVal = None
    finally:
        print("Inside result: {}".format(divisionVal))
    return (divisionVal)

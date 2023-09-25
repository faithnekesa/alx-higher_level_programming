#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Bytecode function for power of and division
    """
    calculation = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                calculation += a ** b / i
        except:
            calculation = b + a
            break
    return (calculation)

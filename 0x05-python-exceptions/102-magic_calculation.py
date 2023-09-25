#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Bytecode function for power of and division
    """
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Error')
            else:
                res += a ** b / i
        except Exception as e:
            res = b + a
            print("Exception: {}".format(e), file=sys.stderr)
            break
    return (res)

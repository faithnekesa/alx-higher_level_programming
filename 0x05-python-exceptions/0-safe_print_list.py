#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list
    Args:
        my_list (list): List to print elements from
        x (int): Number of elements to print from the list
    Return:
        Real number of elements printed
    """
    num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num += 1
        except IndexError:
            break
    print("")
    return (num)

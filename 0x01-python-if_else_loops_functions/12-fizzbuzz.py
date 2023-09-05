#!/usr/bin/python3
def fizzbuzz():
    """Print the numbers from 1 to 100.Separater is space
    Print Fizz for multiples of 3
    Print Buzz for multiples of 5
    Print FizzBuzz for multiples of 3 and 5
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")

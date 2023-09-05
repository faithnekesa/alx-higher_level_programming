#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mydigit = abs(number) % 10
if number < 0:
    mydigit = -mydigit
print("Last digit of {} is {} and is ".format(number, mydigit), end="")
if mydigit > 5:
    print("greater than 5")
elif mydigit == 0:
    print("0")
else:
    print("less than 6 and not 0")

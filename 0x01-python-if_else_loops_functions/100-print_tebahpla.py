#!/usr/bin/python3
# Print the alphabet in reverse order alternating upper- and lower-case
index = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - index)), end="")
    #check if index is 0, if yes set it index to 32 which is space in ascii
    index = 32 if index == 0 else 0

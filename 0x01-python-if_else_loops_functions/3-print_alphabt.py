#!/usr/bin/python3
for x_letter in range(ord('a'), ord('z') + 1):
    if x_letter != ord('e') and x_letter != ord('q'):
        print("{:c}".format(x_letter), end="")

#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = - number
    ld = number % 10
    print("{}".format(ld), end="")
    return ld

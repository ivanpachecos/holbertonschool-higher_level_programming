#!/usr/bin/python3

def print_last_digit(number):
    no_sig = abs(number)
    print("{}".format(no_sig % 10), end="")    
#!/usr/bin/python3
"""
Function that read text of other file
"""


def read_file(filename=""):
    """
    Reads the content of a file and prints it to the console.
    """
    with open(filename, 'r') as f:
        text_readed = f.read()
        print("{}".format(text_readed), end="")

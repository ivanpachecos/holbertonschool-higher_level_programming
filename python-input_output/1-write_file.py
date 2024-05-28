#!/usr/bin/python3
"""
This script contains a function for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number
    of characters written.

    Example:
    >>> write_file("example.txt", "Hello, World!")
    13
    """
    with open(filename, 'w') as f:
        file_w = f.write(text)
        return file_w

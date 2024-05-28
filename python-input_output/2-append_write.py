#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8) and returns the 
number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a given text to the end of a specified file.
    
    Example:
        >>> append_write("example.txt", "Hello, World!")
        13
    """
    with open(filename, 'a', encoding='utf-8') as file:
        text_put = file.write(text)
        return text_put

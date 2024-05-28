#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8) and returns the 
number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a given text to the end of a specified file.

    Args:
        filename (str): The name of the file to which the text will be appended. Defaults to an empty string.
        text (str): The text to append to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    
    Example:
        >>> append_write("example.txt", "Hello, World!")
        13
    """
    with open(filename, 'a', encoding='utf-8') as file:
        text_put = file.write(text)
        return text_put

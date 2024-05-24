#!/usr/bin/python3
"""
This script contains a function to insert a newline followed by two spaces
after each occurrence of '.', '?', or ':' in the given text.
"""


def text_indentation(text):
    """
    Inserts a newline followed by two spaces after each occurrence
    of '.', '?', or ':' in the given text.

    Args:
        text (str): The input text.

    Returns:
        None. The function prints the modified text with the specified
        indentation.
    """

    if not isinstance(text, (str)):
        raise TypeError("text must be a string")
    
    characters = [".", ":", "?"]

    for char in characters:
        text = text.replace(char, char + "\n")
    
    print("{}".format(text), end="")

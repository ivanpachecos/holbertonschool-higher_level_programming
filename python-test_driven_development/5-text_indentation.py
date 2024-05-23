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

    tex1 = text.replace(".", ".\n")
    tex2 = tex1.replace("?", "?\n")
    tex3 = tex2.replace(":", ":\n")

    # Print the modified text
    print(tex3)

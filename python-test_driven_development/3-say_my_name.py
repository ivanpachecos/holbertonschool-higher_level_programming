#!/usr/bin/python3
"""
This module contains a function that prints a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed.
        Defaults to "".

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

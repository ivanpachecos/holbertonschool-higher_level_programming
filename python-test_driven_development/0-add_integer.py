#!/usr/bin/python3
"""
    This module provides an `add_integer` function that adds two
    numbers together.
    Functions:
        _add_integer(a, b=98): Returns the sum of `a` and `b`.
"""


def add_integer(a, b=98):
    """
        Adds two integers or floats and returns the sum as an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

#!/usr/bin/python3
"""
This module contains a function to convert a Python object
to a JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Returns:
    A JSON string representing the Python object.
    """
    using_js = json.dumps(my_obj)
    return using_js

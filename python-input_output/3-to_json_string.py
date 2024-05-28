#!/usr/bin/python3
import json
"""
This module contains a function to convert a Python object to a
JSON string.
"""


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.
    """
    using_js = json.dumps(my_obj)
    return using_js

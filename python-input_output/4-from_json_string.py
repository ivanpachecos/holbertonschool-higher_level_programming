#!/usr/bin/python3
"""
This module contains a function to Json string to a
Python object
"""
import json


def from_json_string(my_str):
    """
    Converts a Json string to python object
    """
    return json.loads(my_str)

#!/usr/bin/python3
"""
This script contains a function to load data from a JSON
file and deserialize it.
"""

import json


def load_from_json_file(filename):
    """
    Loads data from the specified JSON file and deserializes it.

    Args:
        filename (str): The name of the file from which the 
        JSON data will be loaded.

    Returns:
        any: The data deserialized from the JSON file. The type
        of the returned data depends
             on what was stored in the file.

    Example:
        data = load_from_json_file('data.json')
    """
    with open(filename, 'r') as file:
        return json.load(file)

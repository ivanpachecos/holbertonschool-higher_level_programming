#!/usr/bin/python3
"""
This script contains functions to serialize data to JSON format and save it to a file,
as well as to load data from a JSON file and deserialize it.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data to JSON format and saves it to the specified file.

    Args:
        data (any): The data to be serialized. It can be any data type supported by JSON.
        filename (str): The name of the file where the JSON data will be saved.

    Example:
        data = {'name': 'Alice', 'age': 30}
        serialize_and_save_to_file(data, 'data.json')
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads data from the specified JSON file and deserializes it.

    Args:
        filename (str): The name of the file from which the JSON data will be loaded.

    Returns:
        any: The data deserialized from the JSON file. The type of the returned data depends
             on what was stored in the file.

    Example:
        data = load_and_deserialize('data.json')
    """
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

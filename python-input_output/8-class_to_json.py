#!/usr/bin/python3
"""
function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean).
"""

import json


def class_to_json(obj):
    """ Converts a Python object into a JSON format. """
    json_conver = json.dumps(obj.__dict__)
    return json_conver

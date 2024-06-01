#!/usr/bin/python3
"""
This script provides functions to serialize a dictionary to an XML file
and deserialize an XML file back to a dictionary.

Functions:
    serialize_to_xml(dictionary, filename): Serializes a dictionary into an XML file.
    deserialize_from_xml(filename): Deserializes an XML file into a dictionary.
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The name of the file to write the XML data to.

    Example:
        data = {'name': 'John', 'age': '30', 'city': 'New York'}
        serialize_to_xml(data, 'data.xml')
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a dictionary.

    Args:
        filename (str): The name of the XML file to be deserialized.

    Returns:
        dict: The deserialized dictionary.

    Example:
        data = deserialize_from_xml('data.xml')
        print(data)  # Output: {'name': 'John', 'age': '30', 'city': 'New York'}
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text

    return data

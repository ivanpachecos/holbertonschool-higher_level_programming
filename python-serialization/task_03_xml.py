#!/usr/bin/python3
"""

"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    for key, valu in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(valu)

    tree = ET.ElementTree(root)
    with open(filename, 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}

    for child in root:
        data[child.tag] = child.text

    return data

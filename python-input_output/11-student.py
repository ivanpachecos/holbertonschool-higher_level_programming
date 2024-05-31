#!/usr/bin/python3
"""
class Student that defines a student
"""


class Student:
    """Class that defines a student with basic attributes"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        """
        if attrs is None:
            # If attrs is None, return a dictionary with all attributes.
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age,
            }

        # Initialize an empty dictionary to store filtered attributes.
        filtered_dict = {}
        for attr in attrs:
            # Check if the attribute name is a string and the attribute
            # exists in the instance.
            if isinstance(attr, str) and hasattr(self, attr):
                # Add the attribute and its value to the filtered dictionary.
                filtered_dict[attr] = getattr(self, attr)

        # Return the filtered dictionary.
        return filtered_dict

    def reload_from_json(self, json):
        """set atribute of key and value, replacing value"""
        for key, value in json.items():
            setattr(self, key, value)

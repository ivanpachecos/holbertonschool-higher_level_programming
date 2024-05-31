#!/usr/bin/python3
"""
This script defines a `CustomObject` class that can be serialized and
deserialized using Python's `pickle` module.
The class includes methods to display the object's information
serialize the object to a file, and deserialize the object from a file.
"""

import pickle
import os


class CustomObject:
    def __init__(self, name, age, is_student):
        """Initializes an instance of the CustomObject class"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's information."""
        print("Nombre: {}\nAge: {}\nIs student: {}"
                .format(self.name, self.age, self.is_student))
    
    def serialize(self, filename):
        """Serializes the object and saves it to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
    
    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file."""
        if os.path.getsize(filename) > 0:
            with open(filename, 'rb') as f_load:
                loaded_file = pickle.Unpickler(f_load)
                obj = loaded_file.load()
                return obj
        else:
            return None
